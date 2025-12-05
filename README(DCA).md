# Decline Curve Analysis

This project demonstrates Decline Curve Analysis (DCA) using Python for the Oil and Gas industry. The code, written in a Jupyter Notebook, analyzes production data and fits an exponential decline model, providing both data visualization and cumulative production calculation.

## Overview

- **Purpose:**  
  To model oil and gas well production decline over time using exponential decline analysis, visualize production trends, and compute cumulative production.

- **Technology Used:**  
  - Python  
  - Numpy  
  - Pandas  
  - Matplotlib  
  - Jupyter Notebook

## Features

- Reads well production data (time and production rate).
- Applies exponential decline fitting to actual data.
- Visualizes:
  - Production Rate vs. Time.
  - Log-transformed Production Rate vs. Time.
  - Cumulative Production vs. Time.
- Calculates cumulative production using the fitted decline model.

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Libraries: `numpy`, `pandas`, `matplotlib`

Install dependencies with:
```bash
pip install numpy pandas matplotlib
```

### Usage

1. Clone or download this repository.
2. Open `Decline_Curve_Analysis.ipynb` in Jupyter Notebook.
3. Run all cells to see:
   - Data analysis and modeling.
   - Production and model fit plots.
   - Cumulative production trend.

## Code Summary

- **Data Input:**  
  Production rates and corresponding times are defined as numpy arrays.

- **Exponential Decline Model:**
  - Fits an exponential decline using logarithmic transformation.
  - Predicts and visualizes the modeled decline curve alongside actual data.

- **Cumulative Production:**
  - Calculates cumulative production using the decline curve analysis method.
  - Visualizes cumulative production against time.

- **Plotting:**
  - Actual vs. predicted production rates.
  - Log-transformed production rate.
  - Cumulative production.

## References

- Oil & Gas Production Decline Analysis (Arps' Decline Curve)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Numpy Documentation](https://numpy.org/)

## License

This project is provided for educational purposes.

---

**Author:**  
[github.com/Nischhal9205](https://github.com/Nischhal9205)
