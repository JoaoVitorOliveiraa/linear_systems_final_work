import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência fundamental (rad/s) e equivalente em Hz
omega = 10
f = omega / (2 * np.pi)  # Hz

# Tempo
t = np.linspace(0, 5, 2000)
saw_input = signal.sawtooth(2 * np.pi * f * t)

# Valores de β
betas = [0.001, 0.01, 0.1, 1, 10]

plt.figure(figsize=(10, 6))
for beta in betas:
    num = [1, 1e4]
    den = [1, 2 * beta, 100]
    sys = signal.TransferFunction(num, den)
    tout, y, _ = signal.lsim(sys, U=saw_input, T=t)
    plt.plot(tout, y, label=f'β = {beta}')

# Entrada escalada
plt.plot(t, 100 * saw_input, '--', color='grey', lw=1, label='Entrada dente de serra ×100')

plt.title('Resposta à Onda Dente de Serra — Sistema 2')
plt.xlabel('Tempo (s)')
plt.ylabel('y(t)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()