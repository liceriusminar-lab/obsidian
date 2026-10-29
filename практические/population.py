# Логистическая модель роста числа пользователей сервиса
# Вариант 3: a = 2,3; K = 90 000; N0 = 4 000; T = 40

import numpy as np
import matplotlib.pyplot as plt

a = 2.3        
K = 90_000.0  
N0 = 4_000.0   
T = 40         

N = np.zeros(T + 1) 
N[0] = N0

for t in range(T):
    N[t + 1] = N[t] + a * N[t] * (1.0 - N[t] / K)

for t in (0, 1, 6, 12, 18, 24, 30, 40):
    print(f"t = {t:2d}  N = {N[t]:10.1f}")

plt.figure(figsize=(8, 4.5))
plt.plot(range(T + 1), N, marker="o", ms=3)
plt.axhline(K, color="gray", ls="--", lw=1, label="Ёмкость рынка K")
plt.xlabel("Месяц t")
plt.ylabel("Число пользователей N(t)")
plt.title("Логистическая модель роста пользователей (вариант 3)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("population_variant3.png", dpi=150)
plt.show()
