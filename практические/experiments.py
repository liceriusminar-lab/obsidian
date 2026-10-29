# Скрипт серий компьютерного эксперимента
# Вариант 3: базовые значения a = 2,3; K = 90 000; N0 = 4 000

import numpy as np
import matplotlib.pyplot as plt

A_BASE, K_BASE, N0_BASE = 2.3, 90_000.0, 4_000.0
T_PLOT = 40      
T_CLASSIFY = 160  


def simulate(a, K, N0, T):
    """Рассчитывает траекторию N(t) по рекуррентной логистической формуле."""
    N = np.zeros(T + 1)
    N[0] = N0
    for t in range(T):
        N[t + 1] = N[t] + a * N[t] * (1.0 - N[t] / K)
    return N


def time_to_95(N, K):
    """Номер месяца первого достижения уровня 0,95*K (или None, если не достигнут)."""
    target = 0.95 * K
    for t, val in enumerate(N):
        if val >= target:
            return t
    return None


def describe(N, K):
    """Краткое текстовое описание установившегося режима по хвосту траектории."""
    tail = N[-32:]
    tol = 0.002 * K  
    for period in range(1, 17):
        if np.allclose(tail[:-period], tail[period:], atol=tol):
            if period == 1:
                return "монотонный выход / равновесие"
            return f"устойчивый цикл, период {period}"
    return "нерегулярное поведение (периодичность не обнаружена)"


def run_series(name, param_name, values, base_params, filename):
    print(f"\n=== {name} ===")
    plt.figure(figsize=(9, 5))
    rows = []
    for v in values:
        params = dict(base_params)
        params[param_name] = v
        N_long = simulate(params["a"], params["K"], params["N0"], T_CLASSIFY)
        t95 = time_to_95(N_long, params["K"])
        regime = describe(N_long, params["K"])
        rows.append((params["a"], params["K"], params["N0"], t95, regime))
        print(f"{param_name}={v}: t*={t95}, режим: {regime}")
        N_plot = N_long[: T_PLOT + 1]
        plt.plot(range(T_PLOT + 1), N_plot, marker="o", ms=3, label=f"{param_name}={v}")
    plt.xlabel("Месяц t")
    plt.ylabel("Число пользователей N(t)")
    plt.title(name)
    plt.legend(fontsize=8)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
    return rows


if __name__ == "__main__":
    base = {"a": A_BASE, "K": K_BASE, "N0": N0_BASE}

    series1 = run_series(
        "Серия 1. Влияние коэффициента прироста a",
        "a", [1.2, 1.9, 2.1, 2.3, 2.55, 2.8], base, "series1.png",
    )
    series2 = run_series(
        "Серия 2. Влияние начального состояния N0",
        "N0", [1000, 4000, 50000, 95000], base, "series2.png",
    )
    series3 = run_series(
        "Серия 3. Влияние ёмкости рынка K",
        "K", [60000, 120000], base, "series3.png",
    )

    print("\nГрафики сохранены: series1.png, series2.png, series3.png")
