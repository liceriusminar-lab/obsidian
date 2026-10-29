# Демонстрационный вариант: серии эксперимента (задание 4, раздел 5.4)
# Базовые значения: a = 0,6; K = 100 000; N0 = 5 000; T = 24

import numpy as np
import matplotlib.pyplot as plt


def simulate(a, K, N0, T):
    N = np.zeros(T + 1)
    N[0] = N0
    for t in range(T):
        N[t + 1] = N[t] + a * N[t] * (1.0 - N[t] / K)
    return N


def ru_num(x):
    """Формат с пробелом-разделителем тысяч, для подписей легенды."""
    return f"{x:,.0f}".replace(",", " ")


def ru_dec(x):
    """Формат с запятой вместо точки, для коэффициента a."""
    return f"{x:.2f}".rstrip("0").rstrip(".").replace(".", ",")


T = 24
K_BASE, N0_BASE, A_BASE = 100_000, 5_000, 0.6

plt.figure(figsize=(10, 5.5))
for a in [0.3, 0.6, 1.2, 1.9, 2.2, 2.55, 2.9]:
    N = simulate(a, K_BASE, N0_BASE, T)
    plt.plot(range(T + 1), N, marker="o", label=f"a = {ru_dec(a)}")
plt.axhline(K_BASE, color="gray", ls="--", lw=1, label="ёмкость K")
plt.title("Серия 1. Влияние коэффициента прироста a")
plt.xlabel("Месяц t")
plt.ylabel("Число пользователей N(t)")
plt.legend(loc="upper left", fontsize=9)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("demo_series1.png", dpi=150)
plt.close()

plt.figure(figsize=(10, 5.5))
for N0 in [500, 20000, 90000, 105000]:
    N = simulate(A_BASE, K_BASE, N0, T)
    plt.plot(range(T + 1), N, marker="o", label=f"N0 = {ru_num(N0)}")
plt.axhline(K_BASE, color="gray", ls="--", lw=1, label="ёмкость K")
plt.title("Серия 2. Влияние начального числа пользователей N0")
plt.xlabel("Месяц t")
plt.ylabel("Число пользователей N(t)")
plt.legend(loc="lower right", fontsize=9)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("demo_series2.png", dpi=150)
plt.close()

plt.figure(figsize=(10, 5.5))
for K in [60000, 150000]:
    N = simulate(A_BASE, K, N0_BASE, T)
    plt.plot(range(T + 1), N, marker="o", label=f"K = {ru_num(K)}")
plt.axhline(K_BASE, color="gray", ls="--", lw=1, label="ёмкость K")
plt.title("Серия 3. Влияние ёмкости рынка K")
plt.xlabel("Месяц t")
plt.ylabel("Число пользователей N(t)")
plt.legend(loc="lower right", fontsize=9)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("demo_series3.png", dpi=150)
plt.close()

print("saved demo_series1.png, demo_series2.png, demo_series3.png")
