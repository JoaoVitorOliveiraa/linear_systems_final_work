import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# parâmetros do circuito
R = 10e3
C = 15e-9
num = [1 / (R * C)]
den = [1, 3 / (R * C), 1 / (R**2 * C**2)]
sys = signal.TransferFunction(num, den)

# primeiro harmônico (frequência fundamental)
f1 = 1 / (2 * np.pi * R * C)
omega1 = 2 * np.pi * f1
T = 1 / f1
fs = 1e5
t = np.arange(0, 4*T, 1/fs)

# entrada: 1º harmônico da onda quadrada
x = (4 / np.pi) * np.sin(omega1 * t)

# resposta do sistema
t_out, y_out, _ = signal.lsim(sys, U=x, T=t)

# gráfico com duas escalas
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax1.plot(t, x, 'C0--')
ax1.set_ylabel('Entrada (V)')
ax1.set_title('Resposta ao 1º Harmônico de uma Onda Quadrada – Circuito 6')
ax1.grid(True, linestyle='--')

ax2.plot(t_out, y_out * 1e3, 'C1')
ax2.set_ylabel('Saída (mV)')
ax2.set_xlabel('Tempo (s)')
ax2.grid(True, linestyle='--')

plt.tight_layout()
plt.show()