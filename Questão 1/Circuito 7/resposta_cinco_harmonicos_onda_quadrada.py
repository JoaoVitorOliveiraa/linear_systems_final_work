import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência fundamental
f = 10
omega = 2 * np.pi * f
t = np.linspace(0, 3 / f, 1000)

# Entrada: 5 primeiros harmônicos da onda quadrada
x5 = (4 / np.pi) * (
    np.sin(omega * t)
    + (1/3) * np.sin(3 * omega * t)
    + (1/5) * np.sin(5 * omega * t)
    + (1/7) * np.sin(7 * omega * t)
    + (1/9) * np.sin(9 * omega * t)
)

# Sistema: H(s) = -100 / s
sys = signal.TransferFunction([-100], [1, 0])

# Resposta do sistema
t_out, y_out, _ = signal.lsim(sys, U=x5, T=t)

# Gráfico
plt.figure(figsize=(8, 4))
plt.plot(t, x5, '--', label='Entrada: 5 harmônicos')
plt.plot(t, y_out, label='Saída do sistema')
plt.title('Resposta aos 5 Primeiros Harmônicos da Onda Quadrada – Circuito 7')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()