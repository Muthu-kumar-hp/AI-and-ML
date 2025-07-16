# ⚡ Electricity Usage Analysis per Apartment (July 2025)

This project simulates electricity usage for 20 apartments over a period of 30 days (July 2025). It performs data analysis, anomaly detection, and rich visualizations including 2D, 3D, and heatmaps using Python libraries like `pandas`, `matplotlib`, `seaborn`, and `numpy`.

---

## 📊 Project Features

- ✅ Simulation of electricity consumption data for 20 apartments
- ✅ Calculation of:
  - Total usage per apartment
  - Daily usage across all apartments
- ✅ Summary statistics & null check
- ✅ Visualizations:
  - Bar plot (total usage)
  - Line plot
  - Histogram
  - Pie chart
  - 3D bar plot
  - Heatmap
  - 3D wireframe
- ✅ Anomaly detection for high electricity usage
- ✅ Threshold based on:  
  `mean + 2 × standard deviation`

---

## 📁 File Structure

- `main.ipynb` — Main notebook with code and visualizations  
- `README.md` — This file  
- `requirements.txt` *(optional)* — Python package dependencies

---

## 📌 Data Generation Details

- **Apartments:** Aot_1 to Aot_20  
- **Dates:** July 1, 2025 to July 30, 2025  
- **Electricity Usage:** Random values from a normal distribution  
  - Mean = 20 kWh  
  - Standard deviation = 5  

---

## 🖼️ Visualizations Included

1. **Bar Graph** — Total usage per apartment  
2. **Line Plot** — Usage comparison  
3. **Histogram** — Distribution of electricity usage  
4. **Pie Chart** — Share of usage per apartment  
5. **3D Bar Plot** — Usage per apartment per day  
6. **Heatmap** — Usage pattern over time  
7. **3D Wireframe** — Apartment vs Date vs Usage  

---

## 🚨 Anomaly Detection

- Any reading where usage > `mean + 2*std` is marked as **high usage**
- Such entries are flagged in the dataset with `High_usage_flag = True`

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Programming Language |
| pandas | Data manipulation |
| numpy | Random number generation |
| matplotlib | Plotting library |
| seaborn | Statistical visualization |

---

## ▶️ How to Run

1. Clone or download this repository
2. Make sure the following Python libraries are installed:

```bash
pip install pandas numpy matplotlib seaborn
