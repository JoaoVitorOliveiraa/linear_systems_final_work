import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Função de transferência H(s) = 7 / (s^2 + 14 s + 63)
num = [7]                # numerador constante
den = [1, 14, 63]        # s² + 14 s + 63

sys = signal.TransferFunction(num, den)

# Cálculo de pólos e zeros
zeros = np.roots(num)          # vazio (array([], dtype=float64))
poles = np.roots(den)          # [-7 ± j*sqrt(14)]

# Gráfico
plt.figure(figsize=(6,4))
plt.axhline(0, color='black', lw=0.7, ls='--')
plt.axvline(0, color='black', lw=0.7, ls='--')

plt.scatter(np.real(poles), np.imag(poles),
            marker='x', s=100, color='red', label='Pólos')
if zeros.size > 0:             # não haverá zeros finitos
    plt.scatter(np.real(zeros), np.imag(zeros),
                marker='o', facecolors='none', edgecolors='blue', s=100,
                label='Zeros')

plt.title('Diagrama de Pólos e Zeros – Questão 3')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.grid(True, ls=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()