import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# -------------------- parâmetros --------------------
alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]   # valores de α
den    = [1, 2, 2]                               # s² + 2s + 2
omega  = 4                                       # rad/s (fundamental)

# -------- entrada: 7 harmônicos ímpares -----------
odd_ns = [1, 3, 5, 7, 9, 11, 13]
T0  = 2 * np.pi / omega
t   = np.linspace(0, 3 * T0, 6000)               # 3 períodos
u   = (4 / np.pi) * sum(np.sin(n * omega * t) / n for n in odd_ns)

# ------------------ simulação ----------------------
plt.figure(figsize=(9, 5))
for alpha in alphas:
    sys = signal.TransferFunction([alpha, 1], den)   # H(s) = (αs+1)/(s²+2s+2)
    tout, y_out, _ = signal.lsim(sys, U=u, T=t)      # resposta temporal
    plt.plot(tout, y_out, label=f'α = {alpha}')

# entrada tracejada para referência
plt.plot(t, u, 'k--', alpha=0.3, label='Entrada (harmônicos 1–13)')

# ------------------ gráfico ------------------------
plt.title(r'Resposta aos 7 Primeiros Harmônicos ($\omega = 4$ rad/s) – Sistema 1')
plt.xlabel('Tempo [s]')
plt.ylabel('y(t)')
plt.grid(True, ls=':')
plt.legend(fontsize='x-small', ncol=3, loc='upper right')
plt.tight_layout()
plt.show()