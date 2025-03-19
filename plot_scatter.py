import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="muted", font_scale=1.2)
np.random.seed(42)

# Generate synthetic data for rolling and GARCH conditional volatility
rolling_vol = 12 + np.random.normal(scale=1, size=500)
# Synthetic conditional volatility correlated with rolling volatility
cond_vol = rolling_vol + np.random.normal(scale=0.5, size=500)

plt.figure(figsize=(10, 6))
plt.scatter(rolling_vol, cond_vol, alpha=0.6, color="mediumpurple", edgecolors="w", linewidth=0.5)
max_val = max(rolling_vol.max(), cond_vol.max())
plt.plot([0, max_val], [0, max_val], color="red", linestyle="--", linewidth=1, label="y=x")
plt.title("Scatter Plot: Synthetic GARCH vs. Rolling Volatility", fontsize=16)
plt.xlabel("20-Day Rolling Volatility (%)", fontsize=14)
plt.ylabel("GARCH Conditional Volatility (%)", fontsize=14)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
