import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência fundamental
f = 100                      # Hz
omega = 2 * np.pi * f
T = 1 / f
t = np.linspace(0, 4 * T, 2000)

# Primeiro harmônico da série de Fourier da dente de serra
v_in = - (2 / np.pi) * np.sin(omega * t)
v_out = v_in  # H(s) = 1

# Gráfico
plt.figure(figsize=(10, 4))
plt.plot(t, v_in, label='v_in(t): 1º harmônico da dente de serra', linewidth=2)
plt.plot(t, v_out, '--', label='v_out(t)', linewidth=1.5)
plt.title('Resposta ao 1º Harmônico da Dente de Serra – Circuito 4')
plt.xlabel('Tempo t (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()