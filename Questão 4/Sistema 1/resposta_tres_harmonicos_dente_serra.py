import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros
alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
omega = 4  # rad/s
t = np.linspace(0, 3 * 2 * np.pi / omega, 4000)

# Gerar os 3 primeiros harmônicos da dente de serra (n ímpar)
u = np.zeros_like(t)
for n in range(1, 6, 2):  # n = 1, 3, 5
    u += -(2 / (np.pi * n)) * np.sin(n * omega * t)

# Denominador comum
den = [1, 2, 2]

# Plotagem
plt.figure(figsize=(10, 6))
for alpha in alphas:
    num = [alpha, 1]
    system = signal.TransferFunction(num, den)
    tout, y, _ = signal.lsim(system, U=u, T=t)
    plt.plot(tout, y, label=f'α = {alpha}')

plt.plot(t, u, 'k--', alpha=0.3, label='Entrada (3 Harmônicos)')
plt.title('Resposta aos 3 Primeiros Harmônicos da Dente de Serra – Sistema 1')
plt.xlabel('Tempo [s]')
plt.ylabel('Saída y(t)')
plt.grid(True, linestyle=':')
plt.legend(fontsize='x-small', ncol=3, loc='upper right')
plt.tight_layout()
plt.show()