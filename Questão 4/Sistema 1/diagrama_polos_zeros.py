import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Valores de α
alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]

# Denominador fixo (pólos)
den = [1, 2, 2]
poles = np.roots(den)

# Cria figura com subplots (2 × 4 → 8 locais; 1 fica vazio)
fig, axes = plt.subplots(2, 4, figsize=(14, 6))
axes = axes.flatten()

for ax, alpha in zip(axes, alphas):
    zeros = np.roots([alpha, 1])            # Numerador αs + 1
    ax.scatter(np.real(poles), np.imag(poles), s=80, c='k', marker='x', label='Pólos')
    ax.scatter(np.real(zeros), np.imag(zeros), s=80, c='tab:blue', marker='o', label=f'Zero (α={alpha})')
    ax.axhline(0, color='grey', lw=0.5)
    ax.axvline(0, color='grey', lw=0.5)
    x_vals = np.concatenate((np.real(poles), np.real(zeros)))
    x_min, x_max = x_vals.min(), x_vals.max()
    margin = 0.15 * (x_max - x_min if x_max > x_min else 1)
    ax.set_xlim(x_min - margin, x_max + margin)
    ax.set_ylim(-2, 2)
    ax.set_title(f'α = {alpha}')
    ax.set_xlabel('Re')
    ax.set_ylabel('Im')
    ax.grid(True, ls=':', alpha=0.6)
    ax.legend(fontsize='x-small')

# Desativa painel excedente se houver
for ax in axes[len(alphas):]:
    ax.axis('off')

fig.suptitle('Diagrama de Pólos e Zeros — Sistema 1 (Subplots por α)', y=1.02, fontsize=14)
plt.tight_layout()
plt.show()