import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# -------- sistema: H(s) = 7 / (s^2 + 14 s + 63)
num = [7]
den = [1, 14, 63]
sys = signal.TransferFunction(num, den)

# -------- entrada: onda quadrada de frequência ω ≈ ω_n
omega = 8.0                 # rad/s   (≈ √63)
f = omega / (2 * np.pi)     # Hz
T = 1 / f                   # período (≈ 0,787 s)

t = np.linspace(0, 5*T, 4000)
x_sq = signal.square(omega * t)       # amplitude ±1

# -------- saída do sistema
t_out, y_out, _ = signal.lsim(sys, U=x_sq, T=t)

# -------- plot
plt.figure(figsize=(10, 4))
plt.plot(t, x_sq, '--', color='gray', lw=1.2, label=r'Entrada $x(t)$ (quadrada)')
plt.plot(t_out, y_out, color='tab:blue', lw=2, label=r'Saída $y(t)$')
plt.title(r'Resposta à Onda Quadrada – Questão 3')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('y(t)')
plt.grid(True, ls=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
