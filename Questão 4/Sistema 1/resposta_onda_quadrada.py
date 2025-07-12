import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ----------------- parâmetros -----------------
alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]   # valores de α
den = [1, 2, 2]                                 # denominador fixo
omega = 4                                       # frequência angular (rad/s)

# grade de tempo: simular 5 períodos da onda quadrada
T0 = 2*np.pi / omega
t = np.linspace(0, 5*T0, 4000)
u = signal.square(omega * t)                    # onda quadrada ±1

# ----------------- simulação ------------------
plt.figure(figsize=(9, 5))

for alpha in alphas:
    sys = signal.TransferFunction([alpha, 1], den)      # H(s) = (αs + 1)/(s²+2s+2)
    t_out, y_out, _ = signal.lsim(sys, U=u, T=t)        # resposta temporal
    plt.plot(t_out, y_out, label=f'α = {alpha}')

# onda quadrada de referência (tracejado)
plt.plot(t, u, 'k--', alpha=0.35, label='Entrada (onda quadrada)')

# ----------------- ajustes do gráfico ---------
plt.title(r'Resposta à Onda Quadrada ($\omega = 4\,$rad/s) – Sistema 1')
plt.xlabel('Tempo [s]')
plt.ylabel('y(t)')
plt.grid(True, ls=':')
plt.legend(fontsize='x-small', ncol=3, loc='upper right')
plt.tight_layout()
plt.show()