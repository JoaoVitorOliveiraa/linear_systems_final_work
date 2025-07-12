import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros
alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
den = [1, 2, 2]  # Denominador fixo do sistema: s² + 2s + 2
omega = 4        # Frequência angular da onda (rad/s)
T0 = 2 * np.pi / omega
t = np.linspace(0, 3 * T0, 6000)

# Série de Fourier da onda dente de serra (N harmônicos)
N = 25
x = sum(((-1)**(n+1)) * np.sin(n * omega * t) / n for n in range(1, N+1))
x *= (2 / np.pi)  # Normalização da amplitude

# Simulação
plt.figure(figsize=(9, 5))
for alpha in alphas:
    num = [alpha, 1]
    sys = signal.TransferFunction(num, den)
    _, y_out, _ = signal.lsim(sys, U=x, T=t)
    plt.plot(t, y_out, label=f'α = {alpha}')

# Entrada tracejada
plt.plot(t, x, 'k--', alpha=0.3, label='Entrada: Dente de Serra')

# Gráfico
plt.title(r'Resposta à Onda Dente de Serra ($\omega=4$ rad/s) – Sistema 1')
plt.xlabel('Tempo [s]')
plt.ylabel('y(t)')
plt.grid(True, ls=':')
plt.legend(fontsize='x-small', ncol=3, loc='upper right')
plt.tight_layout()
plt.show()