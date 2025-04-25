import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.rcParams['font.family'] = 'NanumGothic' 

df = pd.read_csv("data_filled.csv", header=None, names=["year", "amount_per_person"])
df = df.sort_values(by="year")

df["amount_per_person"] = pd.to_numeric(df["amount_per_person"], errors="coerce") / 10000

plt.figure(figsize=(14, 6))
plt.plot(df["year"], df["amount_per_person"], color='orange', marker='o', markersize=3, linewidth=2)

plt.title("연도별 1인당 월평균 연금 수령 추이", fontsize=14)
plt.xlabel("연도", fontsize=12)
plt.ylabel("1인당 월평균 연금 (만원)", fontsize=12)

plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))

plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(10))

plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()

plt.savefig("pension_graph_syr5.png", dpi=300)
plt.show()
