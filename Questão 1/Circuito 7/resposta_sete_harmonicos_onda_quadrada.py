import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência fundamental
f = 10
omega = 2 * np.pi * f
t = np.linspace(0, 3 / f, 1000)

# Entrada: 7 primeiros harmônicos ímpares da onda quadrada
harmonicos = [1, 3, 5, 7, 9, 11, 13]
x7 = np.zeros_like(t)
for k in harmonicos:
    x7 += (1 / k) * np.sin(k * omega * t)
x7 *= (4 / np.pi)

# Sistema: H(s) = -100 / s
sys = signal.TransferFunction([-100], [1, 0])

# Resposta do sistema
t_out, y_out, _ = signal.lsim(sys, U=x7, T=t)

# Gráfico
plt.figure(figsize=(8, 4))
plt.plot(t, x7, '--', label='Entrada: 7 harmônicos')
plt.plot(t, y_out, label='Saída do sistema')
plt.title('Resposta aos 7 Primeiros Harmônicos da Onda Quadrada – Circuito 7')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()