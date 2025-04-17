import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="muted", font_scale=1.2)
np.random.seed(42)

log_ret = np.random.normal(loc=0, scale=0.01, size=1000)
cond_vol = 10 + 3 * np.abs(log_ret) + np.random.normal(scale=0.2, size=1000)

plt.figure(figsize=(10, 6))
plt.hexbin(log_ret, cond_vol, gridsize=30, cmap="viridis", mincnt=1)
cb = plt.colorbar()
cb.set_label("Counts")
plt.title("Hexbin Plot: Synthetic Log Returns vs. Conditional Volatility", fontsize=16)
plt.xlabel("Log Returns", fontsize=14)
plt.ylabel("Conditional Volatility (%)", fontsize=14)
plt.tight_layout()
plt.show()
