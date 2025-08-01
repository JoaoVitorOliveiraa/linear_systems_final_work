import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros
f = 100                     # Hz
omega = 2 * np.pi * f       # rad/s
T = 1 / f
t = np.linspace(0, 4 * T, 2000)

# Harmônicos de ordem ímpar: n = 1, 3, 5, 7, 9
harmonics = [1, 3, 5, 7, 9]
v_in = np.zeros_like(t)

# Soma dos harmônicos
for n in harmonics:
    v_in += (4 / (n * np.pi)) * np.sin(n * omega * t)

# Saída do circuito (H(s)=1)
v_out = v_in

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, v_in, label='v_in(t): soma de 5 harmônicos', linewidth=2, color='black')
plt.plot(t, v_out, '--', label='v_out(t)', linewidth=1.5, color='red')
plt.title('Resposta aos 5 Primeiros Harmônicos – Circuito 4 (H(s) = 1)')
plt.xlabel('Tempo t (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()