import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Sistema: H(s) = 7 / (s² + 14s + 63)
num = [7]
den = [1, 14, 63]
sys = signal.TransferFunction(num, den)

# Frequência fundamental da onda quadrada
omega = 8  # rad/s
T = 2 * np.pi / omega

# Entrada: 1º harmônico da série de Fourier
t = np.linspace(0, 3*T, 2000)
x1 = (4/np.pi) * np.sin(omega * t)

# Resposta do sistema a x1(t)
t_out, y_out, _ = signal.lsim(sys, U=x1, T=t)

# Gráfico
plt.figure(figsize=(10, 4))
plt.plot(t, x1, 'k--', lw=1.2, label=r'1º Harmônico $x_1(t)$')
plt.plot(t_out, y_out, 'b-', lw=2, label=r'Resposta $y_1(t)$')
plt.title(r'Resposta ao 1º Harmônico da Onda Quadrada – Questão 3')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()