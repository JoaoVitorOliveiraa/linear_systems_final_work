import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# H(s) = -100/s
sys = signal.TransferFunction([-100], [1, 0])

# simular 100 ms
t = np.linspace(0, 0.1, 1000)
t_out, y_out = signal.step(sys, T=t)   # resposta ao degrau unitário

# gráfico
plt.figure(figsize=(8, 4))
plt.plot(t_out*1e3, y_out, label='y(t)   (V)')
plt.title('Resposta ao Degrau Unitário – Circuito 7')
plt.xlabel('Tempo (ms)')
plt.ylabel('Saída (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()