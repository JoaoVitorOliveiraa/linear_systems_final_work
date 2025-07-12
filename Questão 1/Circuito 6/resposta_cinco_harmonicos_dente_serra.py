import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros do circuito
R = 10e3
C = 15e-9
num = [1 / (R * C)]
den = [1, 3 / (R * C), 1 / (R**2 * C**2)]
sys = signal.TransferFunction(num, den)

# Frequência fundamental da onda dente-de-serra
f0 = 1 / (2 * np.pi * R * C)
w0 = 2 * np.pi * f0
T = 1 / f0
fs = 2e5
t = np.arange(0, 4*T, 1/fs)

# Entrada: 5 primeiros harmônicos da dente-de-serra
x = -(2 / np.pi) * (
    np.sin(w0 * t)
    - (1/2) * np.sin(2 * w0 * t)
    + (1/3) * np.sin(3 * w0 * t)
    - (1/4) * np.sin(4 * w0 * t)
    + (1/5) * np.sin(5 * w0 * t)
)

# Resposta do sistema
t_out, y_out, _ = signal.lsim(sys, U=x, T=t)

# Gráfico combinado (entrada e saída)
fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.plot(t, x, 'C0', label='Entrada (V)')
ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Entrada (V)', color='C0')
ax1.tick_params(axis='y', labelcolor='C0')
ax1.grid(True, linestyle='--')

ax2 = ax1.twinx()
ax2.plot(t_out, y_out * 1e6, 'C1', label='Saída (µV)')
ax2.set_ylabel('Saída (µV)', color='C1')
ax2.tick_params(axis='y', labelcolor='C1')

fig.suptitle('5 Primeiros Harmônicos da Dente-de-Serra – Circuito 6')
fig.tight_layout()
plt.show()