import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência fundamental
f = 100                    # Hz
omega = 2 * np.pi * f      # rad/s
T = 1 / f                  # período (s)

# Vetor de tempo: 4 períodos
t = np.linspace(0, 4 * T, 2000)

# Primeiro harmônico da série de Fourier da onda quadrada
v_in = (4 / np.pi) * np.sin(omega * t)

# Saída (ganho unitário): v_out = v_in
v_out = v_in

# Gráfico
plt.figure(figsize=(8, 3))
plt.plot(t, v_in, label='v_in(t): 1º harmônico', linewidth=2)
plt.plot(t, v_out, '--', label='v_out(t)', linewidth=1.5)
plt.title('Resposta ao 1º Harmônico – Circuito 4 (H(s) = 1)')
plt.xlabel('Tempo t (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()