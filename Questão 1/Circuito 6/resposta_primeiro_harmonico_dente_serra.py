import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# parâmetros do circuito
R = 10e3
C = 15e-9
num = [1 / (R * C)]
den = [1, 3 / (R * C), 1 / (R**2 * C**2)]
sys = signal.TransferFunction(num, den)

# frequência fundamental da dente de serra
f0 = 1 / (2 * np.pi * R * C)
w0 = 2 * np.pi * f0
T = 1 / f0
fs = 2e5
t = np.arange(0, 4*T, 1/fs)

# entrada: 1º harmônico da dente-de-serra
x = -(2 / np.pi) * np.sin(w0 * t)

# resposta do sistema
t_out, y_out, _ = signal.lsim(sys, U=x, T=t)

# gráfico
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax1.plot(t, x, 'C0')
ax1.set_ylabel('Entrada (V)')
ax1.set_title('1º Harmônico da Dente-de-Serra – Circuito 6')
ax1.grid(True, linestyle='--')

ax2.plot(t_out, y_out * 1e6, 'C1')
ax2.set_ylabel('Saída (µV)')
ax2.set_xlabel('Tempo (s)')
ax2.grid(True, linestyle='--')

plt.tight_layout()
plt.show()