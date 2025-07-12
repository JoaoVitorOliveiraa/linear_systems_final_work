import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Sistema: H(s) = -100/s
sys = signal.TransferFunction([-100], [1, 0])

# Tempo de simulação (até 0.1 s)
t = np.linspace(0, 0.1, 1000)
u = t  # entrada rampa unitária

# Resposta à rampa
t_out, y_out, _ = signal.lsim(sys, U=u, T=t)

# Gráfico
plt.figure(figsize=(8, 4))
plt.plot(t_out * 1e3, u, '--', label='Entrada (rampa)')
plt.plot(t_out * 1e3, y_out, label='Saída (V)')
plt.title('Resposta à Rampa Unitária – Circuito 7')
plt.xlabel('Tempo (ms)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()