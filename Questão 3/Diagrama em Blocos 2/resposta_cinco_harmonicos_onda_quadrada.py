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

# Tempo e entrada com 5 primeiros harmônicos ímpares
t = np.linspace(0, 3*T, 4000)
x = (4/np.pi) * sum([(1/(2*k+1)) * np.sin((2*k+1)*omega*t) for k in range(5)])

# Resposta do sistema
t_out, y_out, _ = signal.lsim(sys, U=x, T=t)

# Plotagem
plt.figure(figsize=(10, 4))
plt.plot(t, x, 'k--', lw=1.2, label='Entrada: 5 harmônicos')
plt.plot(t_out, y_out, 'b-', lw=2, label='Saída: resposta filtrada')
plt.title('Resposta aos 5 Primeiros Harmônicos – $\omega = 8$ rad/s')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()