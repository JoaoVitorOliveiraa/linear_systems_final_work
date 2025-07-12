import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

f = 100                       # Hz (fundamental)
omega = 2 * np.pi * f         # rad/s
T = 1 / f                     # período fundamental
t = np.linspace(0, 4 * T, 2000)

# Harmônicos n = 1, 3, 5
v1 = (4 / np.pi)       * np.sin( 1 * omega * t)
v3 = (4 / (3 * np.pi)) * np.sin( 3 * omega * t)
v5 = (4 / (5 * np.pi)) * np.sin( 5 * omega * t)

# Sinal composto (entrada)
v_in  = v1 + v3 + v5
v_out = v_in            # H(s) = 1 → saída igual à entrada

plt.figure(figsize=(10, 4))
plt.plot(t, v_in, label='v_in(t): soma 3 harmônicos', linewidth=2, color='black')
plt.plot(t, v_out, '--', label='v_out(t)', linewidth=1.5, color='red')
plt.plot(t, v1, alpha=0.4, label='1º harmônico (n=1)')
plt.plot(t, v3, alpha=0.4, label='3º harmônico (n=3)')
plt.plot(t, v5, alpha=0.4, label='5º harmônico (n=5)')
plt.title('Resposta aos 3 Primeiros Harmônicos de uma Onda Quadrada – Circuito 4')
plt.xlabel('Tempo t (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(loc='upper right', ncol=2)
plt.tight_layout()
plt.show()