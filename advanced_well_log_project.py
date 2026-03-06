
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("well_log_dataset.csv")

# ---------------- PARAMETERS ----------------
GR_min = 20
GR_max = 120
rho_ma = 2.65
rho_f = 1.0
Rw = 0.1
a, m, n = 1, 2, 2

# ---------------- CALCULATIONS ----------------

# Shale Volume
df["Vsh"] = (df["GR_API"] - GR_min) / (GR_max - GR_min)

# Density Porosity
df["Phi_d"] = (rho_ma - df["RHOB_gcc"]) / (rho_ma - rho_f)

# Total Porosity
df["Phi"] = (df["Phi_d"] + df["NPHI"]) / 2

# Water Saturation (Archie)
df["Sw"] = ((a * Rw) / (df["Phi"]**m * df["RT_ohmm"]))**(1/n)
df["Sw"] = df["Sw"].clip(0,1)

# Hydrocarbon Saturation
df["Sh"] = 1 - df["Sw"]

# Net Pay Flags
df["PayFlag"] = (
    (df["Vsh"] < 0.35) &
    (df["Phi"] > 0.10) &
    (df["Sw"] < 0.60)
)

# Net Pay Thickness
net_pay = df[df["PayFlag"]==True]["Depth_m"].count()

print("Estimated Net Pay Thickness (m):", net_pay)

# Save interpreted results
df.to_csv("interpreted_results.csv", index=False)

# ---------------- PLOTS ----------------

# Gamma Ray Log
plt.figure()
plt.plot(df["GR_API"], df["Depth_m"])
plt.gca().invert_yaxis()
plt.xlabel("Gamma Ray (API)")
plt.ylabel("Depth (m)")
plt.title("Gamma Ray Log")
plt.show()

# Porosity Log
plt.figure()
plt.plot(df["Phi"], df["Depth_m"])
plt.gca().invert_yaxis()
plt.xlabel("Porosity")
plt.ylabel("Depth (m)")
plt.title("Porosity vs Depth")
plt.show()

# Water Saturation Log
plt.figure()
plt.plot(df["Sw"], df["Depth_m"])
plt.gca().invert_yaxis()
plt.xlabel("Water Saturation")
plt.ylabel("Depth (m)")
plt.title("Water Saturation vs Depth")
plt.show()

# Density-Neutron Crossplot
plt.figure()
plt.scatter(df["NPHI"], df["Phi_d"])
plt.xlabel("Neutron Porosity")
plt.ylabel("Density Porosity")
plt.title("Density-Neutron Crossplot")
plt.show()
