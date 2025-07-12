import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Função de transferência: H(s) = (12s + 104)/(s + 4)
num = [12, 104]
den = [1, 4]
system = signal.TransferFunction(num, den)

# Frequência fundamental do dente-de-serra
omega = 4          # rad/s
T = 2 * np.pi / omega
t = np.linspace(0, 2*T, 5000)   # duas épocas para visualização

# Inicializa sinais de entrada e saída
u_total = np.zeros_like(t)
y_total = np.zeros_like(t)

# Três primeiros harmônicos (n = 1, 2, 3)
harmonics = [1, 2, 3]

plt.figure(figsize=(10, 6))

for n in harmonics:
    coef = (2 / np.pi) * ((-1)**(n + 1)) / n     # coeficiente da série
    u_n = coef * np.sin(n * omega * t)           # entrada harmônica
    _, y_n, _ = signal.lsim(system, U=u_n, T=t)  # saída filtrada

    u_total += u_n
    y_total += y_n

    plt.plot(t, y_n, label=fr'$y_{n}(t)$  (n={n})', linewidth=1)

# Plota soma total
plt.plot(t, y_total, 'k', linewidth=2, label='Soma $y(t)$')
plt.title('Resposta aos 3 Primeiros Harmônicos da Dente-de-Serra - Questão 2')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()