import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="muted", font_scale=1.2)

# Generate synthetic time series data
dates = pd.date_range(start="2020-01-01", periods=500, freq="D")
# Synthetic conditional volatility: sine wave plus noise
cond_vol = 10 + 2 * np.sin(np.linspace(0, 10 * np.pi, len(dates))) + np.random.normal(scale=0.5, size=len(dates))

df = pd.DataFrame({"Date": dates, "cond_vol": cond_vol})
df.set_index("Date", inplace=True)

plt.figure(figsize=(12, 6))
plt.plot(df.index, df["cond_vol"], color="dodgerblue", linewidth=2)
plt.title("Synthetic Conditional Volatility Time Series", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Volatility (%)", fontsize=14)
plt.tight_layout()
plt.show()
