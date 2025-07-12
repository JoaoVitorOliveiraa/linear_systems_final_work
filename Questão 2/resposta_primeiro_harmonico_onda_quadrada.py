import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Sistema
num = [12, 104]
den = [1, 4]
system = signal.TransferFunction(num, den)

# Frequência do 1º harmônico (fundamental da onda quadrada)
omega = 4
T = 2 * np.pi / omega

# Entrada: primeiro harmônico da série de Fourier
t = np.linspace(0, 5*T, 5000)
u = (4 / np.pi) * np.sin(omega * t)

# Resposta
tout, y, _ = signal.lsim(system, U=u, T=t)

# Gráfico
plt.figure(figsize=(10, 5))
plt.plot(tout, u, 'k--', label=r'Entrada: $\frac{4}{\pi}\sin(\omega t)$')
plt.plot(tout, y, label='Saída: y(t)')
plt.title(r'Resposta ao 1º Harmônico da Série de Fourier ($\omega = 4\,$rad/s) - Questão 2')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()