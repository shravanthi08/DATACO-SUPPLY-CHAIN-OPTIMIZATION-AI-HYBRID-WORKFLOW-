# 📂 Jupyter Notebooks

This folder contains all Jupyter notebooks used in the **DataCo Supply Chain Optimization Project**.  
Each notebook represents a stage in the project lifecycle, combining **AI prompts** with **Python validation** for a hybrid workflow.

---

## 📑 Structure
```markdown
notebooks/
├── 01_data_loading_and_cleaning.ipynb
├── 02_exploratory_data_analysis.ipynb
├── 03_optimization_modeling.ipynb
├── 04_scenario_simulation.ipynb
└── 05_visualization_and_dashboard_preparation.ipynb

### 1. 01_data_loading_and_cleaning.ipynb
- Loads raw dataset from `data/raw/`.
- Cleans data: removes duplicates, handles missing values, standardizes cost/profit.
- Creates derived field `shipping_delay`.
- Saves cleaned dataset to `data/cleaned/`.

### 2. 02_exploratory_data_analysis.ipynb
- Performs descriptive statistics and visualizations.
- Charts include: profit trends, shipping delays, cost vs sales, top customers, profit margins.
- Provides recruiter‑friendly insights into supply chain performance.

### 3. 03_optimization_modeling.ipynb
- Builds a PuLP optimization model to minimize shipping costs.
- Defines constraints for demand fulfillment and deadlines.
- Outputs optimized shipping quantities and total cost.

### 4. 04_scenario_simulation.ipynb
- Tests model under different business scenarios:
  - Demand spike (+20%)
  - Supplier delay (+5 days)
  - Cost increase (+15%)
- Shows adaptability of the supply chain optimization model.

### 5. 05_visualization_and_dashboard_preparation.ipynb
- Prepares final charts and summary tables for Tableau dashboard.
- Exports visuals to `results/`.
- Ensures recruiter‑friendly storytelling with KPI cards and filters.

- Clear step‑by‑step workflow.
- Combines AI prompts + Python validation.
- Easy to follow technical depth and business insights.
- Demonstrates both technical execution and business storytelling.

