# EcoSim – Microeconomics Modeling & Policy Simulation (1B03 Prototype)

EcoSim is a **Python + Streamlit** prototype designed to simulate microeconomic models and policy interventions, aligned with the core knowledge points of **McMaster University DeGroote School of Business 1B03 Introductory Microeconomics** course.

---

## 1B03 Course Knowledge Summary

| Category | Knowledge Point | Description |
|----------|----------------|-------------|
| **Core Theory/Concepts** | Market equilibrium, supply & demand | Understanding how markets reach equilibrium under different conditions |
| | Price elasticity | How quantity demanded or supplied responds to price changes |
| | Cost structure | Understanding firm cost functions and their impact on supply |
| | Policy impact | Effects of taxation, subsidies, and price controls |
| **Skills Development** | Modeling & simulation | Build supply/demand models, simulate policies, and run sensitivity analysis |
| | Data handling | Import market data, clean and validate |
| | Visualization | Interactive charts, equilibrium points, scenario analysis |
| **Ethical/Environmental/Global** | Policy evaluation | Consider societal, ethical, and global impacts of policy interventions |
| **Analytical/Decision Skills** | Predict & optimize | Suggest optimal strategies based on simulation results |

> **Course Focus**: Combines theory and practical modeling skills, emphasizes quantitative analysis, policy simulation, and scenario testing.

---

## EcoSim Software Features

| Module | Feature | Corresponding Knowledge |
|--------|--------|------------------------|
| **Data Import** | Upload market prices, demand/supply data, and policy parameters (Excel/CSV) | Data handling skills |
| **Modeling Module** | Build supply/demand models, compute equilibrium, price elasticity, and cost analysis | Core theory (market equilibrium, elasticity, cost structure) |
| **Policy Simulation** | Simulate taxation, subsidies, and price controls | Policy impact & evaluation |
| **Sensitivity Analysis** | Test different parameter changes on market outcomes | Analytical/decision skills |
| **Visualization** | Interactive charts, curves, highlight equilibrium points | Visualization skills |
| **Prediction & Optimization** | Predict effects of policies and suggest optimal strategies | Analytical/decision skills |

---

## Technology Stack

- **Data Processing**: Pandas, NumPy  
- **Mathematical Modeling**: SciPy, SymPy  
- **Visualization**: Matplotlib, Plotly  
- **Frontend Interface**: Streamlit  

---

## Usage Instructions

1. **Install Dependencies**
```python
pip install streamlit pandas numpy matplotlib plotly scipy sympy
```
2. Run EcoSim
```python
streamlit run eco_sim.py
```
3. Workflow
Data Import: Upload Excel/CSV with Price, Demand, Supply columns.

Modeling Module: Compute market equilibrium, price elasticity, and supply analysis.

Policy Simulation: Adjust taxes, subsidies, or price controls, and see equilibrium shifts.

Visualization: View interactive supply/demand curves with original and adjusted equilibria.

Sensitivity Analysis: Test how parameter changes affect market outcomes and policy impact.

4. code
```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="EcoSim - Microeconomics Simulator", layout="wide")

st.title("EcoSim: Microeconomics Modeling & Policy Simulation")

# 1. Data Import
st.header("1. Import Market Data")
uploaded_file = st.file_uploader("Upload CSV with columns: Price, Demand, Supply", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:", data.head())
else:
    st.info("Please upload a CSV file with Price, Demand, and Supply columns.")
    data = pd.DataFrame({'Price':[10,20,30], 'Demand':[100,80,60], 'Supply':[50,70,90]})

# 2. Modeling Module
st.header("2. Supply & Demand Modeling")
price = data['Price']
demand = data['Demand']
supply = data['Supply']

# Find approximate equilibrium
equilibrium_idx = (np.abs(demand - supply)).idxmin()
eq_price = price[equilibrium_idx]
eq_quantity = (demand[equilibrium_idx] + supply[equilibrium_idx]) / 2

st.write(f"Approximate Equilibrium Price: {eq_price}")
st.write(f"Approximate Equilibrium Quantity: {eq_quantity}")

# 3. Policy Simulation
st.header("3. Policy Simulation")
tax = st.slider("Select per-unit tax", 0, 20, 0)
subsidy = st.slider("Select per-unit subsidy", 0, 20, 0)

adjusted_supply = supply - tax + subsidy
equilibrium_idx_adj = (np.abs(demand - adjusted_supply)).idxmin()
eq_price_adj = price[equilibrium_idx_adj]
eq_quantity_adj = (demand[equilibrium_idx_adj] + adjusted_supply[equilibrium_idx_adj]) / 2

st.write(f"Adjusted Equilibrium Price: {eq_price_adj}")
st.write(f"Adjusted Equilibrium Quantity: {eq_quantity_adj}")

# 4. Visualization
st.header("4. Visualization")
fig, ax = plt.subplots()
ax.plot(price, demand, label="Demand")
ax.plot(price, supply, label="Original Supply")
ax.plot(price, adjusted_supply, label="Adjusted Supply (Tax/Subsidy)")
ax.scatter([eq_price], [eq_quantity], color='red', label="Original Equilibrium")
ax.scatter([eq_price_adj], [eq_quantity_adj], color='green', label="Adjusted Equilibrium")
ax.set_xlabel("Price")
ax.set_ylabel("Quantity")
ax.legend()
st.pyplot(fig)

# 5. Sensitivity Analysis (simple)
st.header("5. Sensitivity Analysis")
price_change = st.slider("Test Price Change (%)", -50, 50, 0)
new_demand = demand * (1 - price_change/100)
st.line_chart(pd.DataFrame({'Original Demand': demand, 'New Demand': new_demand}))

st.success("EcoSim modules loaded successfully. You can now explore equilibrium and policy impacts interactively!")

```