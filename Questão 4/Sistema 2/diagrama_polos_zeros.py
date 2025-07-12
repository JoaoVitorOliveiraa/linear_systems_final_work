import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Valores de β
betas = [0.001, 0.01, 0.1, 1, 10]

# Numerador fixo  (zero em s = -10⁴)
num = [1, 1e4]

# Cria figura com subplots (2 × 3 → 6 locais; 1 ficará vazio)
fig, axes = plt.subplots(2, 3, figsize=(14, 6))
axes = axes.flatten()

for ax, beta in zip(axes, betas):
    # Denominador dependente de β → s² + 2βs + 100
    den = [1, 2*beta, 100]

    # Cálculo de pólos e zeros
    poles = np.roots(den)          # pólos variam com β
    zeros = np.roots(num)          # zero fixo em -10⁴

    # Plotagem
    ax.scatter(np.real(poles), np.imag(poles),
               s=80, marker='x', label='Pólos')
    ax.scatter(np.real(zeros), np.imag(zeros),
               s=80, marker='o', facecolors='none', label='Zero')

    # Eixos de referência
    ax.axhline(0, color='grey', lw=0.5)
    ax.axvline(0, color='grey', lw=0.5)

    # Ajuste automático dos limites (com margem)
    x_vals = np.concatenate((np.real(poles), np.real(zeros)))
    x_min, x_max = x_vals.min(), x_vals.max()
    margin = 0.15 * (x_max - x_min if x_max > x_min else 1)
    ax.set_xlim(x_min - margin, x_max + margin)

    # Altura suficiente para caber a parte imaginária
    y_max = max(abs(np.imag(poles)).max(), 1)
    ax.set_ylim(-1.1*y_max, 1.1*y_max)

    # Rótulos, grade, legenda
    ax.set_title(f'β = {beta}')
    ax.set_xlabel('Re')
    ax.set_ylabel('Im')
    ax.grid(True, ls=':', alpha=0.6)
    ax.legend(fontsize='x-small')

# Desativa painel excedente (o 6.º)
for ax in axes[len(betas):]:
    ax.axis('off')

fig.suptitle('Diagrama de Pólos e Zeros — Sistema 2 (Subplots por β)',
             y=1.02, fontsize=14)
plt.tight_layout()
plt.show()