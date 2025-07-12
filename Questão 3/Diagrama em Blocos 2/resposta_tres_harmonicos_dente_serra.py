import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Sistema: H(s) = 7 / (s² + 14s + 63)
num = [7]
den = [1, 14, 63]
sys = signal.TransferFunction(num, den)

# Frequência fundamental
omega = 8  # rad/s
T = 2 * np.pi / omega
t = np.linspace(0, 3*T, 3000)

# Entrada: 3 primeiros harmônicos da dente de serra
x = sum([(((-1)**(n+1))/n) * np.sin(n * omega * t) for n in range(1, 4)])
x *= (2 / np.pi)

# Resposta do sistema
t_out, y_out, _ = signal.lsim(sys, U=x, T=t)

# Gráfico
plt.figure(figsize=(10, 4))
plt.plot(t, x, 'k--', lw=1.2, label='Entrada: 3 harmônicos da dente de serra')
plt.plot(t_out, y_out, 'b-', lw=2, label='Saída: resposta filtrada')
plt.title('Resposta aos 3 Primeiros Harmônicos da Dente de Serra – $\omega = 8$ rad/s')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()