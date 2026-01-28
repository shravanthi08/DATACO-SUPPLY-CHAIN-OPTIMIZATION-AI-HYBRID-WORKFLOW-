
# 📂 Data Folder

This folder contains all datasets used in the **DataCo Supply Chain Optimization Project**.  
It is organized into subfolders to clearly separate the **raw source data** from the **cleaned and processed data** used in analysis.

---


## 🔹 Contents

### 1. `raw/`
- **DataCoSupplyChainDataset.csv**  
  - Original dataset downloaded from Kaggle: [Logistics Operations Database](https://www.kaggle.com/datasets/yogape/logistics-operations-database)  
  - Contains 53 columns with detailed supply chain records (orders, costs, profits, shipping, customer details).  
  - Used as the starting point for cleaning and schema reduction.

### 2. `cleaned/`
- **DataCoSupplyChain_Cleaned.csv**  
  - Reduced and cleaned dataset prepared for analysis.  
  - Key transformations:
    - Removed duplicates and missing values.  
    - Standardized cost and profit fields.  
    - Added derived field: `shipping_delay` (difference between order date and ship date).  
    - Reduced to ~10 essential columns for clarity and recruiter impact.  
  - This file is used in all notebooks (`EDA`, `Optimization`, `Scenario Simulations`, and `Dashboard Preparation`).

---

## ✅ Recruiter Signal
- Shows respect for **data lifecycle** (raw → cleaned).  
- Demonstrates ability to **document transformations** clearly.  
- Ensures reproducibility by keeping both original and cleaned versions.  

---
