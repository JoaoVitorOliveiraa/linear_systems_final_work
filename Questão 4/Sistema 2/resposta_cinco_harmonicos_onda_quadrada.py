import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência fundamental
omega = 10
t = np.linspace(0, 5, 2000)

# Harmônicos ímpares: n = 1, 3, 5, 7, 9
harmonics = [1, 3, 5, 7, 9]
fourier_sum = np.zeros_like(t)
for n in harmonics:
    A_n = 4 / (np.pi * n)
    fourier_sum += A_n * np.sin(n * omega * t)

# Valores de β
betas = [0.001, 0.01, 0.1, 1, 10]

plt.figure(figsize=(10, 6))
for beta in betas:
    num = [1, 1e4]
    den = [1, 2 * beta, 100]
    sys = signal.TransferFunction(num, den)
    tout, y, _ = signal.lsim(sys, U=fourier_sum, T=t)
    plt.plot(tout, y, label=f'β = {beta}')

# Entrada (5 harmônicos) escalada
plt.plot(t, 100 * fourier_sum, '--', color='grey', lw=1, label='Série (5 harmônicos) ×100')

plt.title('Resposta aos 5 Primeiros Harmônicos da Série de Fourier de uma Onda Quadrada de Frequência ω — Sistema 2')
plt.xlabel('Tempo (s)')
plt.ylabel('y(t)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()