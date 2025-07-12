import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ----------------- parâmetros -----------------
alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]   # valores corretos de α
den    = [1, 2, 2]                               # s² + 2s + 2  (pólos fixos)
omega  = 4                                       # rad/s (frequência fundamental)

# -------- entrada: 5 primeiros harmônicos ímpares da dente de serra --------
odd_ns = [1, 3, 5, 7, 9]                         # 5 termos ímpares
T0   = 2 * np.pi / omega                         # período fundamental
t    = np.linspace(0, 3 * T0, 6000)              # três períodos

# série de Fourier (sinal dente de serra)
u = np.zeros_like(t)
for n in odd_ns:
    u += -(2 / (np.pi * n)) * np.sin(n * omega * t)

# ----------------- simulação ------------------
plt.figure(figsize=(9, 5))
for alpha in alphas:
    sys = signal.TransferFunction([alpha, 1], den)   # H(s) = (αs + 1)/(s² + 2s + 2)
    tout, y_out, _ = signal.lsim(sys, U=u, T=t)      # resposta temporal
    plt.plot(tout, y_out, label=f'α = {alpha}')

# entrada tracejada
plt.plot(t, u, 'k--', alpha=0.3, label='Entrada: 5 harmônicos')

# ----------------- gráfico --------------------
plt.title(r'Resposta aos 5 Primeiros Harmônicos da Dente de Serra ($\omega=4$ rad/s) – Sistema 1')
plt.xlabel('Tempo [s]')
plt.ylabel('y(t)')
plt.grid(True, ls=':')
plt.legend(fontsize='x-small', ncol=3, loc='upper right')
plt.tight_layout()
plt.show()