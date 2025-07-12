import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros da onda
f = 100                       # Hz
omega = 2 * np.pi * f         # rad/s
T = 1 / f                     # período (s)

# Vetor de tempo: quatro períodos
t = np.linspace(0, 4 * T, 2000)

# Geração da onda quadrada unitária (0–1)
v_in = 0.5 * (np.sign(np.sin(omega * t)) + 1)

# Seguidor de tensão: saída = entrada
v_out = v_in

# Plot
plt.figure(figsize=(8, 3))
plt.plot(t, v_in, label='v_in(t)', linewidth=2)
plt.plot(t, v_out, '--', label='v_out(t)', linewidth=1.5)
plt.title('Resposta a Onda Quadrada – Circuito 4')
plt.xlabel('Tempo t (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()