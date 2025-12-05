# =====================================
# 📘 Anti-Overfitting XGBoost Pipeline
# =====================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from xgboost import XGBRegressor
from sklearn.multioutput import MultiOutputRegressor

# =====================================
# 1️⃣ Load and Clean Data
# =====================================
df = pd.read_csv(r"D:\Greenfield Energy\20250108-AI-HackathonData (1)\Final_organized_data_set\Low Pressure\278 Short String GL.csv")

# Drop irrelevant or text-heavy columns
df = df.drop(columns=["Comment", "date_time", "wax_cut", "PDC", "THP", "Water", "Sand"], errors='ignore')

# Convert non-numerics to numeric where possible
for col in df.columns:
    if col not in ["act_cat", "activity_impact"]:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Remove rows missing target values
df = df.dropna(subset=["oil_rate", "gas_rate"])

# =====================================
# 2️⃣ Feature and Target Setup
# =====================================
X = df.drop(columns=["oil_rate", "gas_rate", "choke", "bsw_percent", "h2s_conc"], errors='ignore')
y = df[["oil_rate", "gas_rate"]]

# Drop highly correlated features (>0.95)
corr = X.corr(numeric_only=True).abs()
upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
to_drop = [col for col in upper.columns if any(upper[col] > 0.95)]
X = X.drop(columns=to_drop)

# =====================================
# 3️⃣ Preprocessing Pipelines
# =====================================
categorical_cols = ["act_cat"]
numerical_cols = X.drop(columns=categorical_cols, errors='ignore') \
                  .select_dtypes(include=[np.number]).columns.tolist()

num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

cat_pipeline = Pipeline([
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", num_pipeline, numerical_cols),
    ("cat", cat_pipeline, categorical_cols)
])

# =====================================
# 4️⃣ Define Model
# =====================================
xgb_params = dict(
    objective='reg:squarederror',
    random_state=42,
    n_estimators=500,
    learning_rate=0.03,
    max_depth=4,
    subsample=0.6,
    colsample_bytree=0.6,
    reg_alpha=2,
    reg_lambda=4,
    min_child_weight=5,
    n_jobs=-1
)

base_xgb = XGBRegressor(**xgb_params)

pipeline = Pipeline([
    ("preprocess", preprocessor),
    ("model", MultiOutputRegressor(base_xgb, n_jobs=-1))
])

# =====================================
# 5️⃣ Train-Test Split
# =====================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =====================================
# 6️⃣ Cross-Validation (R² & MAE)
# =====================================
kf = KFold(n_splits=5, shuffle=True, random_state=42)
r2_scores, mae_scores = [], []

print("\n🔁 Cross-validation performance:")
for fold, (train_idx, val_idx) in enumerate(kf.split(X_train)):
    X_tr, X_val = X_train.iloc[train_idx], X_train.iloc[val_idx]
    y_tr, y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]
    pipeline.fit(X_tr, y_tr)
    y_val_pred = pipeline.predict(X_val)
    r2_fold = r2_score(y_val, y_val_pred)
    mae_fold = mean_absolute_error(y_val, y_val_pred)
    r2_scores.append(r2_fold)
    mae_scores.append(mae_fold)
    print(f"Fold {fold+1}: R² = {r2_fold:.3f}, MAE = {mae_fold:.3f}")

print(f"\n📊 Mean CV R²: {np.mean(r2_scores):.3f} ± {np.std(r2_scores):.3f}")
print(f"📊 Mean CV MAE: {np.mean(mae_scores):.3f} ± {np.std(mae_scores):.3f}")

# =====================================
# 7️⃣ Fit Final Model
# =====================================
pipeline.fit(X_train, y_train)

# =====================================
# 8️⃣ Predictions (Train & Test)
# =====================================
y_train_pred = pipeline.predict(X_train)
y_test_pred = pipeline.predict(X_test)

# --- Train Performance ---
train_oil_mae = mean_absolute_error(y_train["oil_rate"], y_train_pred[:, 0])
train_gas_mae = mean_absolute_error(y_train["gas_rate"], y_train_pred[:, 1])
train_oil_rmse = np.sqrt(mean_squared_error(y_train["oil_rate"], y_train_pred[:, 0]))
train_gas_rmse = np.sqrt(mean_squared_error(y_train["gas_rate"], y_train_pred[:, 1]))
train_oil_r2 = r2_score(y_train["oil_rate"], y_train_pred[:, 0])
train_gas_r2 = r2_score(y_train["gas_rate"], y_train_pred[:, 1])

# --- Test Performance ---
test_oil_mae = mean_absolute_error(y_test["oil_rate"], y_test_pred[:, 0])
test_gas_mae = mean_absolute_error(y_test["gas_rate"], y_test_pred[:, 1])
test_oil_rmse = np.sqrt(mean_squared_error(y_test["oil_rate"], y_test_pred[:, 0]))
test_gas_rmse = np.sqrt(mean_squared_error(y_test["gas_rate"], y_test_pred[:, 1]))
test_oil_r2 = r2_score(y_test["oil_rate"], y_test_pred[:, 0])
test_gas_r2 = r2_score(y_test["gas_rate"], y_test_pred[:, 1])

# =====================================
# 9️⃣ Results Summary
# =====================================
print("\n📋 Performance Summary")
print(f"Train → Oil R²: {train_oil_r2:.3f}, RMSE: {train_oil_rmse:.3f}, MAE: {train_oil_mae:.3f}")
print(f"Train → Gas R²: {train_gas_r2:.3f}, RMSE: {train_gas_rmse:.3f}, MAE: {train_gas_mae:.3f}")
print(f"Test  → Oil R²: {test_oil_r2:.3f}, RMSE: {test_oil_rmse:.3f}, MAE: {test_oil_mae:.3f}")
print(f"Test  → Gas R²: {test_gas_r2:.3f}, RMSE: {test_gas_rmse:.3f}, MAE: {test_gas_mae:.3f}")

# =====================================
# 🔍 Overfitting Check
# =====================================
print("\n🚨 Overfitting Check:")
print(f"Oil R² gap: {train_oil_r2 - test_oil_r2:.3f}")
print(f"Gas R² gap: {train_gas_r2 - test_gas_r2:.3f}")
if (train_oil_r2 - test_oil_r2 > 0.1) or (train_gas_r2 - test_gas_r2 > 0.1):
    print("⚠️ Possible overfitting detected — consider reducing model complexity.")
else:
    print("✅ No significant overfitting detected.")

# =====================================
# 🔢 Plotting Section
# =====================================

def plot_actual_vs_pred(actual, predicted, title, xlabel, ylabel, color):
    plt.figure(figsize=(8, 5))
    plt.scatter(actual, predicted, alpha=0.6, color=color)
    plt.plot([actual.min(), actual.max()], [actual.min(), actual.max()], 'r--', lw=2)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# --- Actual vs Predicted (Train) ---
plot_actual_vs_pred(y_train["oil_rate"], y_train_pred[:, 0],
                    "Actual vs Predicted Oil Rate (Train)", "Actual Oil Rate", "Predicted Oil Rate", "green")
plot_actual_vs_pred(y_train["gas_rate"], y_train_pred[:, 1],
                    "Actual vs Predicted Gas Rate (Train)", "Actual Gas Rate", "Predicted Gas Rate", "purple")

# --- Actual vs Predicted (Test) ---
plot_actual_vs_pred(y_test["oil_rate"], y_test_pred[:, 0],
                    "Actual vs Predicted Oil Rate (Test)", "Actual Oil Rate", "Predicted Oil Rate", "blue")
plot_actual_vs_pred(y_test["gas_rate"], y_test_pred[:, 1],
                    "Actual vs Predicted Gas Rate (Test)", "Actual Gas Rate", "Predicted Gas Rate", "orange")

# --- Residual Plots ---
oil_residuals = y_test["oil_rate"] - y_test_pred[:, 0]
gas_residuals = y_test["gas_rate"] - y_test_pred[:, 1]

plt.figure(figsize=(8, 5))
plt.scatter(y_test_pred[:, 0], oil_residuals, alpha=0.6, color='blue')
plt.axhline(0, color='red', linestyle='--')
plt.title("Residuals vs Predicted Oil Rate (Test)")
plt.xlabel("Predicted Oil Rate")
plt.ylabel("Residuals")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(y_test_pred[:, 1], gas_residuals, alpha=0.6, color='orange')
plt.axhline(0, color='red', linestyle='--')
plt.title("Residuals vs Predicted Gas Rate (Test)")
plt.xlabel("Predicted Gas Rate")
plt.ylabel("Residuals")
plt.show()
