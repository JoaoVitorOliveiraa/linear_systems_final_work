import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros do circuito
R = 10e3
C = 15e-9
num = [1 / (R * C)]
den = [1, 3 / (R * C), 1 / (R**2 * C**2)]
sys = signal.TransferFunction(num, den)

# Frequência fundamental
f0 = 1 / (2 * np.pi * R * C)
w0 = 2 * np.pi * f0
T = 1 / f0
fs = 2e5
t = np.arange(0, 4*T, 1/fs)

# Entrada: 7 primeiros harmônicos ímpares
harmonicos = [1, 3, 5, 7, 9, 11, 13]
x = np.zeros_like(t)
for k in harmonicos:
    x += (1 / k) * np.sin(k * w0 * t)
x *= (4 / np.pi)

# Resposta do sistema
t_out, y_out, _ = signal.lsim(sys, U=x, T=t)

# Gráficos
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax1.plot(t, x, 'C0')
ax1.set_ylabel('Entrada (V)')
ax1.set_title('7 Primeiros Harmônicos da Onda Quadrada – Circuito 6')
ax1.grid(True, linestyle='--')

ax2.plot(t_out, y_out * 1e3, 'C1')
ax2.set_ylabel('Saída (mV)')
ax2.set_xlabel('Tempo (s)')
ax2.grid(True, linestyle='--')

plt.tight_layout()
plt.show()