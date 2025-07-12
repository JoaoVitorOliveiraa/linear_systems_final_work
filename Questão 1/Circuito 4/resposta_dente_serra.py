import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência "sábia"
f = 100                      # Hz
omega = 2 * np.pi * f        # rad/s
T = 1 / f
t = np.linspace(0, 4 * T, 2000)

# Onda dente de serra normalizada (sobe linearmente de -1 a 1)
v_in = signal.sawtooth(omega * t, width=1)
v_out = v_in  # H(s) = 1 → saída = entrada

# Gráfico
plt.figure(figsize=(10, 4))
plt.plot(t, v_in, label='v_in(t): dente de serra', linewidth=2)
plt.plot(t, v_out, '--', label='v_out(t)', linewidth=1.5)
plt.title('Resposta à Onda Dente de Serra – Circuito 4')
plt.xlabel('Tempo t (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()