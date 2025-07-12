import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Função de transferência: H(s) = 1 / (s^2 + s + 1)
num = [1]
den = [1, 1, 1]
system = signal.TransferFunction(num, den)

# Frequência "sábia": ω = 4 rad/s (canto do pólo)
omega = 4
T = 2 * np.pi / omega

# Onda quadrada ±1
t = np.linspace(0, 5*T, 5000)
u = signal.square(omega * t)

# Resposta
tout, y, _ = signal.lsim(system, U=u, T=t)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(tout, u, 'k--', label='Entrada: onda quadrada')
plt.plot(tout, y, label='Saída: y(t)')
plt.title(r'Resposta à Onda Quadrada ($\omega = 4\,$rad/s) - Questão 3')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':')
plt.legend(loc='lower left', bbox_to_anchor=(0, 0.05), frameon=True, framealpha=0.9)
plt.tight_layout()
plt.show()
