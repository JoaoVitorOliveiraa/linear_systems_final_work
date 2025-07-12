import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência fundamental ω (rad/s)
omega = 10

# Primeiro harmônico da onda quadrada
A1 = 4 / np.pi
t = np.linspace(0, 5, 2000)
first_harmonic = A1 * np.sin(omega * t)

# Valores de β
betas = [0.001, 0.01, 0.1, 1, 10]

plt.figure(figsize=(10, 6))
for beta in betas:
    num = [1, 1e4]
    den = [1, 2 * beta, 100]
    sys = signal.TransferFunction(num, den)
    tout, y, _ = signal.lsim(sys, U=first_harmonic, T=t)
    plt.plot(tout, y, label=f'β = {beta}')

# Entrada de referência escalada
plt.plot(t, 100 * first_harmonic, '--', color='grey', lw=1, label='100·(4/π)·sin(ωt)')

plt.title('Resposta ao 1º Harmônico da Série de Fourier de uma Onda Quadrada de Frequência ω — Sistema 2')
plt.xlabel('Tempo (s)')
plt.ylabel('y(t)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()