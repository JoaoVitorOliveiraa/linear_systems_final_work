import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência fundamental
f = 10
omega = 2 * np.pi * f

# Entrada: 1º harmônico da onda quadrada (senoidal)
t = np.linspace(0, 3 / f, 1000)
x1 = (4 / np.pi) * np.sin(omega * t)

# Sistema: H(s) = -100 / s
sys = signal.TransferFunction([-100], [1, 0])

# Resposta à senoide
t_out, y_out, _ = signal.lsim(sys, U=x1, T=t)

# Gráfico
plt.figure(figsize=(8, 4))
plt.plot(t, x1, '--', label='1º Harmônico (entrada)')
plt.plot(t, y_out, label='Saída do sistema')
plt.title('Resposta ao 1º Harmônico da Onda Quadrada – Circuito 7')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()