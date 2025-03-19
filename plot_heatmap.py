import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set aesthetic style
sns.set(style="whitegrid", palette="muted", font_scale=1.2)
np.random.seed(42)

# Simulate data for 3 years (2020-2022) across 12 months
years = np.repeat([2020, 2021, 2022], 12)
months = np.tile(np.arange(1, 13), 3)
# Generate synthetic average conditional volatility values
avg_vol = np.random.uniform(low=8, high=15, size=len(years))

# Create a DataFrame with the simulated data
df = pd.DataFrame({
    "Year": years,
    "Month": months,
    "cond_vol": avg_vol
})

# Pivot the DataFrame: rows = Year, columns = Month, values = cond_vol
pivot_df = df.pivot(index="Year", columns="Month", values="cond_vol")

plt.figure(figsize=(12, 6))
sns.heatmap(pivot_df, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap: Monthly Average Synthetic Conditional Volatility", fontsize=16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Year", fontsize=14)
plt.tight_layout()
plt.show()
