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

# Tempo e sinal de entrada: 3 primeiros harmônicos
t = np.linspace(0, 3*T, 3000)
x = (4/np.pi) * (
    np.sin(omega * t) +
    (1/3) * np.sin(3 * omega * t) +
    (1/5) * np.sin(5 * omega * t)
)

# Resposta do sistema
t_out, y_out, _ = signal.lsim(sys, U=x, T=t)

# Gráfico
plt.figure(figsize=(10, 4))
plt.plot(t, x, 'k--', lw=1.2, label='Entrada: 3 harmônicos')
plt.plot(t_out, y_out, 'b-', lw=2, label='Saída: resposta filtrada')
plt.title('Resposta aos 3 Primeiros Harmônicos da Onda Quadrada – $\omega = 8$ rad/s')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()