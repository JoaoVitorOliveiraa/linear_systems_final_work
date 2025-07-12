import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência fundamental
omega = 10
t = np.linspace(0, 5, 2000)

# Série com 3 primeiros harmônicos da dente de serra
harmonics = [1, 2, 3]
saw_sum = np.zeros_like(t)
for n in harmonics:
    A_n = -2 / (np.pi * n)
    saw_sum += A_n * np.sin(n * omega * t)

# Valores de β
betas = [0.001, 0.01, 0.1, 1, 10]

plt.figure(figsize=(10, 6))
for beta in betas:
    num = [1, 1e4]
    den = [1, 2 * beta, 100]
    sys = signal.TransferFunction(num, den)
    tout, y, _ = signal.lsim(sys, U=saw_sum, T=t)
    plt.plot(tout, y, label=f'β = {beta}')

# Entrada escalada por 100
plt.plot(t, 100 * saw_sum, '--', color='grey', lw=1, label='Série (3 harmônicos - dente de serra) ×100')

plt.title('Resposta aos 3 Primeiros Harmônicos da Dente de Serra — Sistema 2')
plt.xlabel('Tempo (s)')
plt.ylabel('y(t)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()