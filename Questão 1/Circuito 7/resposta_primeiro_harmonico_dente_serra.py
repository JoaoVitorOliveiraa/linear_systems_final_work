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

# entrada: 1º har# frequência fundamental
f0 = 10        # Hz
omega = 2 * np.pi * f0
t = np.linspace(0, 3 / f0, 1000)

# entrada: 1º harmônico da dente-de-serra (±1 V)
x1 = (2 / np.pi) * np.sin(omega * t)

# sistema integrador: H(s) = -100 / s
sys = signal.TransferFunction([-100], [1, 0])

# resposta ao seno
t_out, y_out, _ = signal.lsim(sys, U=x1, T=t)

# gráfico
plt.figure(figsize=(8, 4))
plt.plot(t, x1, '--', label='Entrada: 1º harmônico (V)')
plt.plot(t_out, y_out, label='Saída: resposta do circuito (V)')
plt.title('Resposta ao 1º Harmônico da Dente-de-Serra – Circuito 7')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()