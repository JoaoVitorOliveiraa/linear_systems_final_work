import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# parâmetros do circuito
R = 10e3           # 10 kΩ
C = 15e-9          # 15 nF

# função de transferência H(s)
num = [1 / (R * C)]
den = [1, 3 / (R * C), 1 / (R**2 * C**2)]
sys = signal.TransferFunction(num, den)

# onda quadrada na frequência central f0
f0 = 1 / (2 * np.pi * R * C)   # ≈ 1061 Hz
T, fs = 1 / f0, 5e5            # período e amostragem 500 kHz
t = np.arange(0, 4 * T, 1 / fs)
x = signal.square(2 * np.pi * f0 * t)  # ±1 V

# resposta do circuito
t_out, y_out, _ = signal.lsim(sys, U=x, T=t)

# gráfico em dois subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax1.plot(t, x, 'C0--')
ax1.set_ylabel('Entrada (V)')
ax1.set_title('Resposta à Onda Quadrada – Circuito 6')
ax1.grid(True, linestyle='--')

ax2.plot(t_out, y_out * 1e3, 'C1')
ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel('Saída (mV)')
ax2.grid(True, linestyle='--')

plt.tight_layout()
plt.show()