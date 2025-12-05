# Petroleum Production Forecasting using XGBoost

This repository contains a robust pipeline for forecasting oil and gas production rates using the XGBoost machine learning algorithm. The workflow is designed to prevent overfitting and ensure reproducible, high-quality results — from data cleaning to evaluation and visualization.

## Features

- **Data Cleaning:** Handles missing values, drops irrelevant columns, and converts types.
- **Feature Selection:** Removes highly correlated features to prevent redundancy.
- **Pipeline Preprocessing:** Includes standard scaling and one-hot encoding for categorical data.
- **Multioutput Regression:** Simultaneously predicts both oil and gas rates.
- **Cross-Validation:** Uses k-fold to report metrics and diagnose overfitting.
- **Anti-Overfitting:** Regularization and early stopping strategies.
- **Performance Metrics:** Prints R², RMSE, and MAE for train and test sets.
- **Visualization:** Plots actual vs. predicted rates and residuals.

## Requirements

Install dependencies with:

```bash
pip install pandas numpy matplotlib scikit-learn xgboost
```

## Usage

1. **Prepare Data:** Place your CSV data file (example path in code, adjust as needed).
2. **Edit Path:** Update the `pd.read_csv` line with your correct file path.
3. **Run the Script:** Execute from terminal:
    ```bash
    python "Petroleum production forecasting using XGBoost.py"
    ```

## How It Works

1. **Load & Clean Data:** Reads the raw dataset, drops text-heavy and irrelevant columns, converts types, and removes rows with missing target values.
2. **Feature Engineering:** Drops features with high mutual correlation; sets up predictors and targets.
3. **Preprocessing Pipeline:** Applies median imputation, scaling, and one-hot encoding before modeling.
4. **Model Definition:** Configures an XGBoost regressor with strong anti-overfitting regularization.
5. **Train-Test Split:** Divides data into training and test sets.
6. **Cross-Validation:** Reports mean and fold-wise R² and MAE.
7. **Fit Final Model:** Trains on the full train set.
8. **Predictions:** Predicts on both train and test sets and prints metrics.
9. **Overfitting Check:** Flags overfitting if R² gap is significant.
10. **Plotting:** Shows scatter plots of actual vs. predicted rates and residual plots for residual diagnostics.

## Sample Output

```
🔁 Cross-validation performance:
Fold 1: R² = 0.85, MAE = 4.2
...
📊 Mean CV R²: 0.84 ± 0.02
🚨 Overfitting Check:
Oil R² gap: 0.08
✅ No significant overfitting detected.
```
(Your results will depend on your data.)

## Visualizations

- Actual vs. Predicted scatter plots for oil & gas rates (Train and Test)
- Residuals vs. predicted rates to analyze bias and variance

## Customization

- **File Path:** Change the dataset location as needed.
- **XGBoost Parameters:** Adjust `xgb_params` in the script for different model behaviors.
- **Feature Columns:** Modify dropped columns for your dataset.

## Contact

For questions or feedback, open an issue or reach out to [Nischhal9205](https://github.com/Nischhal9205).

---

**Disclaimer:** Example assumes correct file paths and data format; modify script to fit your context as needed.
