```markdown
# Skin Effect — Reservoir Pressure Drawdown Notebook

This repository contains a Jupyter Notebook (Skin_effect.ipynb) that demonstrates the skin and skin-zone effect on reservoir pressure drawdown using a simple synthetic dataset and analytic equations. The notebook is intended for educational and exploratory use in petroleum reservoir engineering and shows how changes near the wellbore (skin and damaged zone) affect the radial pressure distribution.

Notebook (permalink):  
https://github.com/Nischhal9205/Python-and-ML-for-OIL-and-GAS-Industry/blob/a7c97fc4819695ece501512ab7bd4847499b490e/Skin_effect.ipynb

## What this does

- Generates synthetic reservoir/well parameters (permeability, flow rate, formation volume factor, viscosity, reservoir thickness, outer boundary pressure and radius, wellbore radius).
- Builds a radial pressure profile for an undamaged (ideal) well using the radial steady-state analytic formula.
- Simulates a damaged (skin-affected) well by introducing a skin-zone radius and an adjusted permeability in the skin zone, then plots the damaged pressure profile.
- Plots both pressure profiles together for an intuitive visualization of how skin and skin-zone radius impact drawdown near the wellbore.

## Key function

The notebook defines a function:

```python
def skin_effect(s, rs):
    ...
```

- s : skin factor (parameter present in the signature for compatibility/extension, but not used directly in the current implementation)
- rs: skin-zone radius (ft) — radius of the damaged zone around the wellbore

The function computes an effective permeability in the skin zone and generates a pressure profile from rw (wellbore radius) to rs (skin radius) for the damaged well, then plots it alongside the undamaged profile.

Example call in the notebook:
```python
skin_effect(5, 20)
```

## Requirements

The notebook uses standard Python data-science packages:

- Python 3.x
- numpy
- pandas
- matplotlib
- seaborn
- jupyter / JupyterLab (or Google Colab)

Install dependencies with pip if needed:
```bash
pip install numpy pandas matplotlib seaborn jupyter
```

## How to run

- Option 1 — Open in Google Colab:
  - The notebook includes a Colab badge/link at the top. Click it to open and run interactively in Colab (no local setup required).

- Option 2 — Run locally:
  1. Clone the repository.
  2. Install the dependencies listed above.
  3. Start Jupyter and open `Skin_effect.ipynb`:
     ```bash
     jupyter notebook Skin_effect.ipynb
     ```
  4. Run the notebook cells.

## Notes, assumptions & extensions

- The notebook currently generates synthetic random data (seeded for reproducibility). Replace those synthetic variables with measured reservoir/well data to explore real cases.
- The function signature contains a skin factor parameter `s` that is not used in the current computation — you can extend the implementation to explicitly incorporate `s` into the pressure equations if desired.
- The current calculation uses simplified and commonly used algebraic approximations for radial pressure drawdown (with constants shown in the notebook code). Validate and adapt formulas for more advanced modelling or field-calibrated analysis.
- The plotted axis limits are chosen for the synthetic values in the example. Adjust `plt.xlim` / `plt.ylim` in the notebook for other parameter ranges.

## Contributing

Contributions, improvements, and bug fixes are welcome. If you add functionality (e.g., true use of the skin factor, options for multiple damaged zones, or alternative plotting styles), please open a PR or issue in this repository.

## License

This repository does not specify a license. If you plan to reuse or distribute this code, please add an appropriate LICENSE file or contact the repository owner for clarification.

## Author / Contact

Repository: Nischhal9205/Python-and-ML-for-OIL-and-GAS-Industry  
Notebook author: Nischhal9205

If you need help adapting the notebook to field data or adding features (e.g., exporting plots, parameter sweeps, or automating sensitivity studies), open an issue or submit a pull request.
```
