# Well Log Interpretation using Python

## Overview

This project demonstrates a basic **petrophysical interpretation workflow** using well log data.
The script processes a well log dataset and performs common reservoir evaluation calculations such as **shale volume, porosity, water saturation, hydrocarbon saturation, and net pay estimation**.

The goal of this project is to show how **Python can be used for subsurface data analysis in petroleum engineering**.

---

## Features

* Load well log dataset using **Pandas**
* Compute **Shale Volume (Vsh)** from Gamma Ray logs
* Calculate **Density Porosity**
* Estimate **Total Porosity**
* Compute **Water Saturation (Sw)** using **Archie’s Equation**
* Determine **Hydrocarbon Saturation (Sh)**
* Identify **Net Pay zones**
* Estimate **Net Pay Thickness**
* Generate log plots and crossplots for analysis

---

## Dataset Requirements

The input dataset must be a CSV file named:

```
well_log_dataset.csv
```

It should contain the following columns:

| Column Name | Description              |
| ----------- | ------------------------ |
| Depth_m     | Depth in meters          |
| GR_API      | Gamma Ray log (API)      |
| RHOB_gcc    | Bulk density (g/cc)      |
| NPHI        | Neutron porosity         |
| RT_ohmm     | True resistivity (ohm-m) |

Example structure:

```
Depth_m,GR_API,RHOB_gcc,NPHI,RT_ohmm
1000,45,2.35,0.25,20
1001,50,2.40,0.22,18
```

---

## Petrophysical Calculations

### 1. Shale Volume

Shale volume is estimated using the Gamma Ray index:

```
Vsh = (GR - GR_min) / (GR_max - GR_min)
```

Where:

* GR_min = 20
* GR_max = 120

---

### 2. Density Porosity

```
Phi_d = (rho_ma - RHOB) / (rho_ma - rho_f)
```

Where:

* Matrix density (rho_ma) = 2.65 g/cc
* Fluid density (rho_f) = 1.0 g/cc

---

### 3. Total Porosity

```
Phi = (Phi_d + NPHI) / 2
```

---

### 4. Water Saturation (Archie Equation)

```
Sw = ((a * Rw) / (Phi^m * Rt))^(1/n)
```

Parameters used:

| Parameter | Value |
| --------- | ----- |
| a         | 1     |
| m         | 2     |
| n         | 2     |
| Rw        | 0.1   |

---

### 5. Hydrocarbon Saturation

```
Sh = 1 - Sw
```

---

### 6. Net Pay Identification

Net pay is identified using the following criteria:

* Vsh < 0.35
* Porosity > 0.10
* Water Saturation < 0.60

---

## Output

### 1. Interpreted Dataset

A new file is generated:

```
interpreted_results.csv
```

This file contains all computed parameters including:

* Vsh
* Porosity
* Water Saturation
* Hydrocarbon Saturation
* Net Pay Flag

---

### 2. Visualizations

The script generates the following plots:

1. Gamma Ray Log vs Depth
2. Porosity vs Depth
3. Water Saturation vs Depth
4. Density–Neutron Crossplot

These plots help in **reservoir characterization and lithology interpretation**.

---

## Installation

Install required Python libraries:

```bash
pip install pandas numpy matplotlib
```

---

## How to Run

1. Place the dataset file `well_log_dataset.csv` in the project folder.
2. Run the script:

```bash
python well_log_interpretation.py
```

3. The interpreted dataset and plots will be generated.

---

## Applications

This workflow is useful for:

* Basic **reservoir characterization**
* **Petrophysical evaluation**
* **Net pay estimation**
* Learning **Python for subsurface data analysis**
* Building **petroleum engineering data science portfolios**

---

## Future Improvements

Possible extensions to the project include:

* Reading **LAS well log files**
* Lithology classification
* Machine learning for **facies prediction**
* Interactive log visualization
* Multi-well reservoir evaluation

---

## Author

**Nischhal Kumar Sahu**
Petroleum Engineering
IIT (ISM) Dhanbad
