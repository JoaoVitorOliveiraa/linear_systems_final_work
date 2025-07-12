import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros da onda quadrada
f = 10  # frequência em Hz
omega = 2 * np.pi * f
T = 1 / f

# Tempo de simulação
t = np.linspace(0, 3 * T, 1000)
x = signal.square(omega * t)  # entrada: onda quadrada de frequência ω

# Sistema H(s) = -100 / s
sys = signal.TransferFunction([-100], [1, 0])

# Simulação
t_out, y_out, _ = signal.lsim(sys, U=x, T=t)

# Gráfico
plt.figure(figsize=(8, 4))
plt.plot(t_out, x, '--', label='Entrada: onda quadrada')
plt.plot(t_out, y_out, label='Saída: onda triangular')
plt.title('Resposta à Onda Quadrada – Circuito 7')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()