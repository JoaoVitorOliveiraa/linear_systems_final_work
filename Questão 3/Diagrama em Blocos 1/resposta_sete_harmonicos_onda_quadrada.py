import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Função de transferência: H(s) = 1 / (s^2 + s + 1)
num = [1]
den = [1, 1, 1]
system = signal.TransferFunction(num, den)

# Frequência fundamental da onda quadrada
omega = 4            # rad/s
T = 2 * np.pi / omega
t = np.linspace(0, 2 * T, 5000)   # duas épocas de observação

# Inicializa acumuladores
u_total = np.zeros_like(t)
y_total = np.zeros_like(t)

# Primeiros 7 harmônicos ímpares: n = 1, 3, 5, 7, 9, 11, 13
harmonics = [1, 3, 5, 7, 9, 11, 13]

plt.figure(figsize=(10, 6))

for n in harmonics:
    u_n = (4 / (np.pi * n)) * np.sin(n * omega * t)  # entrada harmônica
    _, y_n, _ = signal.lsim(system, U=u_n, T=t)      # saída filtrada
    u_total += u_n
    y_total += y_n
    plt.plot(t, y_n, label=f'$y_{{{n}}}(t)$  (n={n})', linewidth=1)

# Soma final dos harmônicos
plt.plot(t, y_total, 'k', linewidth=2, label='Soma $y(t)$')
plt.title('Resposta aos 7 Primeiros Harmônicos da Série de Fourier - Questão 3')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()