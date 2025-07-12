import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Função de transferência H(s) = (12s + 104)/(s + 4)
num = [12, 104]
den = [1, 4]
system = signal.TransferFunction(num, den)

# Frequência fundamental
omega = 4          # rad/s
T = 2 * np.pi / omega
t = np.linspace(0, 2*T, 5000)   # duas épocas para visualização
u_total = np.zeros_like(t)
y_total = np.zeros_like(t)

# Gera e acumula 1º, 3º e 5º harmônicos
for n in [1, 3, 5]:
    u_n = (4 / (np.pi * n)) * np.sin(n * omega * t)   # entrada
    tout, y_n, _ = signal.lsim(system, U=u_n, T=t)    # saída
    u_total += u_n
    y_total += y_n
    plt.plot(t, y_n, label=f'y_{n}(t)  (n={n})')

# Gráficos
plt.plot(t, y_total, 'k', linewidth=2, label='Soma y(t)')
plt.title('Resposta aos 1º, 3º e 5º Harmônicos - Questão 2')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':')
plt.legend(loc='lower left', bbox_to_anchor=(0, 0.05), frameon=True, framealpha=0.9)
plt.tight_layout()
plt.show()