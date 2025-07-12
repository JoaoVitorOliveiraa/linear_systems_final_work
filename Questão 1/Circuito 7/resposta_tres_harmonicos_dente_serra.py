import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# frequência fundamental
f0     = 10                      # Hz
omega  = 2 * np.pi * f0
T      = 1 / f0
t      = np.linspace(0, 3*T, 1500)

# entrada: 3 primeiros harmônicos da dente-de-serra
x3 = (2 / np.pi) * (
        np.sin(omega * t)
      - 0.5 * np.sin(2 * omega * t)
      + (1/3) * np.sin(3 * omega * t)
     )

# sistema integrador inversor H(s) = -100 / s
sys = signal.TransferFunction([-100], [1, 0])

# resposta do sistema
tout, yout, _ = signal.lsim(sys, U=x3, T=t)

# gráfico (mesmo eixo de tempo, dois eixos Y)
fig, ax1 = plt.subplots(figsize=(9, 4.5))

ax1.plot(tout, x3, 'C0--', label='Entrada (V)')
ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Entrada (V)', color='C0')
ax1.tick_params(axis='y', labelcolor='C0')
ax1.grid(True, ls='--')

ax2 = ax1.twinx()
ax2.plot(tout, yout, 'C1', label='Saída (V)')
ax2.set_ylabel('Saída (V)', color='C1')
ax2.tick_params(axis='y', labelcolor='C1')

fig.suptitle('3 Primeiros Harmônicos da Dente-de-Serra – Circuito 7')
fig.tight_layout()
plt.show()