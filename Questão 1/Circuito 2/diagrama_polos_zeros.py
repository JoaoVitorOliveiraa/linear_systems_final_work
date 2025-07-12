import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Valores comerciais
R1 = 1e3          # 1 kΩ
R2 = 1e3          # 1 kΩ
C1 = 100e-9       # 100 nF
L1 = 0.253        # 253 mH

# H(s) = (R1/L1)*s / (s² + (R1+R2)/L1*s + 1/(L1*C1))
num = [R1 / L1, 0]
den = [1, (R1 + R2) / L1, 1 / (L1 * C1)]
sys = signal.TransferFunction(num, den)

# Polos e zeros
zeros = np.roots(num)
poles = np.roots(den)

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(np.real(poles), np.imag(poles), marker='x', s=100, color='r', label='Polos')
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', s=100, facecolors='none',
            edgecolors='b', label='Zeros')
plt.axhline(0, color='black', lw=0.5, linestyle='--')
plt.axvline(0, color='black', lw=0.5, linestyle='--')
plt.xlabel('Eixo Real')
plt.ylabel('Eixo Imaginário')
plt.title('Diagrama de Pólos e Zeros – Circuito 2')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()