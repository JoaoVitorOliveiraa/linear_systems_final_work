import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Função de transferência: H(s) = 1 / (s^2 + s + 1)
num = [1]
den = [1, 1, 1]
system = signal.TransferFunction(num, den)

# Frequência fundamental
omega = 4  # rad/s
T = 2 * np.pi / omega
t = np.linspace(0, 2*T, 5000)  # duas épocas

# Primeiro harmônico da série de Fourier do dente-de-serra
u = (2 / np.pi) * np.sin(omega * t)

# Resposta do sistema
tout, y, _ = signal.lsim(system, U=u, T=t)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t, u, 'k--', label=r'Entrada: $\frac{2}{\pi} \sin(\omega t)$')
plt.plot(t, y, color='orange', label='Saída: y(t)')
plt.title(r'Resposta ao 1º Harmônico da Dente-de-Serra ($\omega = 4$ rad/s) - Questão 3')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()