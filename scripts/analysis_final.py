import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.stats.diagnostic import acorr_ljungbox

df_full = pd.read_csv(
    'mertens_full.csv',
    dtype={'n': 'int32', 'mu': 'int8', 'M': 'int32'}
   )
n = df_full['n'].values
mu = df_full['mu'].values
M = df_full['M'].values

df_plot = pd.read_csv('mertens_plot.csv', dtype={'n': 'int32', 'M': 'int32'})
n_plot = df_plot['n'].values
M_plot = df_plot['M'].values

mu_dist = pd.read_csv('distribution.txt')
p_minus1 = mu_dist[mu_dist['mu_value'] == -1]['probability'].values[0]
p_0 = mu_dist[mu_dist['mu_value'] == 0]['probability'].values[0]
p_1 = mu_dist[mu_dist['mu_value'] == 1]['probability'].values[0]

N = len(M)
print(f"Завантажено N = {N} точок.")
print(f"Розподіл μ: P(-1)={p_minus1:.4f}, P(0)={p_0:.4f}, P(1)={p_1:.4f}")

plt.figure(figsize=(14, 6))
plt.plot(n, M, linewidth=0.5, color='blue')
plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
plt.xlabel('n')
plt.ylabel('M(n)')
plt.title('Функція Мертенса (проріджені дані)')
plt.grid(alpha=0.3)
plt.savefig('mertens.png', dpi=300)
plt.show()

ratio = M / np.sqrt(n)
plt.figure(figsize=(14, 6))
plt.plot(n, ratio, linewidth=0.3, color='green')
plt.axhline(y=0, color='black', linestyle='--')
plt.xlabel('n')
plt.ylabel('M(n) / √n')
plt.title('Нормалізована функція Мертенса')
plt.grid(alpha=0.3)
plt.savefig('mertens_normalized.png', dpi=300)
plt.show()

ratio_abs = np.abs(M) / np.sqrt(n)
plt.figure(figsize=(14, 6))
plt.plot(n, ratio_abs, linewidth=0.3, color='darkred')
plt.xlabel('n')
plt.ylabel('|M(n)| / √n')
plt.title('Нормоване абсолютне відхилення функції Мертенса')
plt.grid(alpha=0.3)
plt.savefig('mertens_ratio_abs.png', dpi=300)
plt.show()

print(f"Максимальне |M(n)|/√n = {np.max(ratio_abs):.4f}")
print(f"Максимальне M(n)/√n = {np.mean(ratio):.4f}")
print(f"Мінімальне M(n)/√n = {np.min(ratio):.4f}")

rng = np.random.default_rng(42)
steps_rw = rng.choice([-1, 0, 1], size=N, p=[p_minus1, p_0, p_1])
random_walk = np.cumsum(steps_rw)

idx = np.arange(999, N, 1000, dtype=int)

if idx[-1] != N - 1:
    idx = np.append(idx, N - 1)
rw_plot = random_walk[idx]

plt.figure(figsize=(14, 6))
plt.plot(n_plot, M_plot, label='M(n)', linewidth=0.5, alpha=0.7)
plt.plot(n_plot, rw_plot, label='Випадкове блукання (реальний розподіл μ)', linewidth=0.5, alpha=0.7)
plt.xlabel('n')
plt.ylabel('Значення')
plt.title('M(n) та випадкове блукання')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('mertens_vs_random.png', dpi=300)
plt.show()

plt.figure(figsize=(12, 5))
plot_acf(M_plot, lags=100, ax=plt.gca())
plt.title("Автокореляція M(n) (проріджений ряд)")
plt.savefig('autocorr_M.png', dpi=300)
plt.show()

plt.figure(figsize=(12, 5))
plot_acf(mu[:100000], lags=100, ax=plt.gca())
plt.title("Автокореляція M(n) (перші 100 000)")
plt.savefig('autocorr_mu.png', dpi=300)
plt.show()

lb_test = acorr_ljungbox(mu[:100000], lags=[10, 20, 30], return_df=True)
print("\nТест Льюнга-Бокса на μ (перші 100 000 значень):")
print(lb_test)

max_abs = np.max(np.abs(M))
n_max_abs = n[np.argmax(np.abs(M))]
max_pos = np.max(M)
n_max_pos = n[np.argmax(M)]
min_neg = np.min(M)
n_min_neg = n[np.argmin(M)]
max_ratio = np.max(ratio)
min_ratio = np.min(ratio)
max_abs_ratio = np.max(ratio_abs)

with open('results.txt', 'w', encoding='utf-8') as f:
    f.write("Дослідження: Статичний аналіз функції Мертенса\n\n")
    f.write(f"Максимальне |M(n)|: {max_abs} при = {n_max_abs}\n")
    f.write(f"Максимальне M(n): {max_pos} при = {n_max_pos}\n")
    f.write(f"Мінімальне M(n): {min_neg} при = {n_min_neg}\n")
    f.write(f"Максимальне M(n)/√n: {max_ratio:.6f}\n")
    f.write(f"Мінімальне M(n)/√n: {min_ratio:.6f}\n")
    f.write(f"Максимальне |M(n)|/√n: {max_abs_ratio:.6f}\n")

print("\nРезультати збережено у файл results.txt")