import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ----- parâmetros -----
alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]     # valores de α
den    = [1, 2, 2]                                 # s² + 2s + 2
omega  = 4                                         # rad/s (fundamental)

# ----- entrada: 3 primeiros harmônicos (n = 1, 3, 5) -----
T0  = 2 * np.pi / omega
t   = np.linspace(0, 3 * T0, 4000)                 # 3 períodos
u   = (4 / np.pi) * (np.sin(omega * t) +
                     np.sin(3 * omega * t) / 3 +
                     np.sin(5 * omega * t) / 5)

# ----- simulação -----
plt.figure(figsize=(9, 5))
for alpha in alphas:
    sys = signal.TransferFunction([alpha, 1], den)
    tout, y_out, _ = signal.lsim(sys, U=u, T=t)
    plt.plot(tout, y_out, label=f'α = {alpha}')

# entrada (tracejado)
plt.plot(t, u, 'k--', alpha=0.35, label='Entrada (harmônicos 1,3,5)')

# ----- gráfico -----
plt.title(r'Resposta aos 3 Primeiros Harmônicos ($\omega = 4$ rad/s) – Sistema 1')
plt.xlabel('Tempo [s]')
plt.ylabel('y(t)')
plt.grid(True, ls=':')
plt.legend(fontsize='x-small', ncol=3, loc='upper right')
plt.tight_layout()
plt.show()