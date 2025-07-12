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

# Plot# Componentes
R1 = R2 = 10e3          # 10 kΩ
C2 = 15e-9              # 15 nF

# Pólo do sistema
omega_0 = (1/R1 + 1/R2) / C2

num = [1.0]             # ganho constante (não afeta polos/zeros)
den = [1.0, omega_0]    # s + ω0

# Zeros, polos, ganho
z, p, k = signal.tf2zpk(num, den)

# Plot
plt.figure()
if z.size:
    plt.scatter(np.real(z), np.imag(z), marker='o', label='Zeros')
plt.scatter(np.real(p), np.imag(p), marker='x', label='Polos')
plt.axhline(0); plt.axvline(0)
plt.grid(True)
plt.title('Diagrama de Pólos e Zeros do Circuito 3')
plt.xlabel('Parte Real'); plt.ylabel('Parte Imaginária')
plt.legend()
plt.show()