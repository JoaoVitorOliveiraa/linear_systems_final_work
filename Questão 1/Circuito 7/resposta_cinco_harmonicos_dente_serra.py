import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros
f0 = 10
omega = 2 * np.pi * f0
T = 1 / f0
t = np.linspace(0, 3*T, 1500)

# Entrada: 5 primeiros harmônicos da dente-de-serra
x5 = (2 / np.pi) * (
    np.sin(omega * t)
    - (1/2) * np.sin(2 * omega * t)
    + (1/3) * np.sin(3 * omega * t)
    - (1/4) * np.sin(4 * omega * t)
    + (1/5) * np.sin(5 * omega * t)
)

# Sistema: integrador inversor
sys = signal.TransferFunction([-100], [1, 0])

# Resposta
t_out, y_out, _ = signal.lsim(sys, U=x5, T=t)

# Gráfico
fig, ax1 = plt.subplots(figsize=(9, 4.5))

ax1.plot(t_out, x5, 'C0--', label='Entrada: 5 harmônicos')
ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Entrada (V)', color='C0')
ax1.tick_params(axis='y', labelcolor='C0')
ax1.grid(True, ls='--')

ax2 = ax1.twinx()
ax2.plot(t_out, y_out, 'C1', label='Saída (V)')
ax2.set_ylabel('Saída (V)', color='C1')
ax2.tick_params(axis='y', labelcolor='C1')

fig.suptitle('Resposta aos 5 Primeiros Harmônicos da Dente-de-Serra – Circuito 7')
fig.tight_layout()
plt.show()