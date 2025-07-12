import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência da dente-de-serra
f0 = 10  # Hz
omega0 = 2 * np.pi * f0
T = 1 / f0
t = np.linspace(0, 3 * T, 1500)

# Entrada: onda dente-de-serra simétrica entre -1V e +1V
x = signal.sawtooth(omega0 * t, width=0.5)

# Sistema: H(s) = -100 / s
sys = signal.TransferFunction([-100], [1, 0])

# Resposta do sistema
t_out, y_out, _ = signal.lsim(sys, U=x, T=t)

# Gráfico da entrada e da saída
fig, ax1 = plt.subplots(figsize=(9, 4.5))

ax1.plot(t_out, x, 'C0--', label='Entrada (V)')
ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Entrada', color='C0')
ax1.tick_params(axis='y', labelcolor='C0')
ax1.grid(True, ls='--')

ax2 = ax1.twinx()
ax2.plot(t_out, y_out, 'C1', label='Saída (V)')
ax2.set_ylabel('Saída', color='C1')
ax2.tick_params(axis='y', labelcolor='C1')

fig.suptitle('Resposta à Onda Dente-de-Serra – Circuito 7')
fig.tight_layout()
plt.show()