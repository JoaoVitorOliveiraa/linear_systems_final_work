import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ----- parâmetros -----
alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
den    = [1, 2, 2]                 # s² + 2s + 2
omega  = 4                         # rad/s  (frequência do 1º harmônico)
amp    = 4 / np.pi                 # amplitude do 1º harmônico da onda quadrada

# grade de tempo (5 períodos da senóide)
T0 = 2 * np.pi / omega
t  = np.linspace(0, 5*T0, 4000)
u  = amp * np.sin(omega * t)       # entrada: 1º harmônico

# ----- simulação -----
plt.figure(figsize=(9, 5))
for alpha in alphas:
    sys = signal.TransferFunction([alpha, 1], den)
    tout, y_out, _ = signal.lsim(sys, U=u, T=t)
    plt.plot(tout, y_out, label=f'α = {alpha}')

# entrada tracejada para referência
plt.plot(t, u, 'k--', alpha=0.35, label='Entrada: 1º harmônico')

# ----- gráfico -----
plt.title(r'Resposta ao 1º Harmônico da Série de Fourier ($\omega = 4\,\mathrm{rad/s}$) – Sistema 1')
plt.xlabel('Tempo [s]')
plt.ylabel('y(t)')
plt.grid(True, ls=':')
plt.legend(fontsize='x-small', ncol=3, loc='upper right')
plt.tight_layout()
plt.show()