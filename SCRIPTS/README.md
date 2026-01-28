# 📂 Scripts Folder

This folder contains **modular Python scripts** used in the **DataCo Supply Chain Optimization Project**.  
Unlike Jupyter notebooks (which show step‑by‑step exploration and storytelling), these scripts hold **reusable functions** for dataset loading, cleaning, analysis, optimization, scenario simulation, and visualization.  
They make the project more **production‑ready** and easier to reproduce.

## 📑 Structure
```markdown
scripts/
├── dataset_loading_and_cleaning.py
├── exploratory_data_analysis.py
├── optimization_modeling.py
├── scenario_simulation.py
└── visualization.py

### 1. dataset_loading_and_cleaning.py
- Functions to load raw dataset from `data/raw/`.
- Cleans data: removes duplicates, handles missing values, standardizes cost/profit fields.
- Creates derived field `shipping_delay`.
- Saves cleaned dataset to `data/cleaned/`.

### 2. exploratory_data_analysis.py
- Functions for descriptive statistics and visualizations.
- Charts: profit trends, shipping delays, cost vs sales, top customers, profit margins.
- Modular plotting functions for reuse across notebooks.

### 3. optimization_modeling.py
- Functions to build and run PuLP optimization model.
- Defines objective: minimize shipping costs.
- Adds constraints: demand fulfillment and deadlines.
- Returns optimized shipping quantities and total cost.

### 4. scenario_simulation.py
- Functions to simulate business scenarios:
  - Demand spike (+20%)
  - Supplier delay (+5 days)
  - Cost increase (+15%)
- Recalculates shipping quantities and costs for each scenario.

### 5. visualization.py
- Functions to generate final charts and export them to `results/`.
- Prepares recruiter‑friendly visuals for Tableau dashboard integration.
- Supports KPI cards and filters for storytelling.


- Shows ability to **productionize notebooks** into reusable scripts.
- Demonstrates clean separation of concerns (loading, analysis, optimization, visualization).
- Makes project reproducible and professional for recruiters and collaborators.



