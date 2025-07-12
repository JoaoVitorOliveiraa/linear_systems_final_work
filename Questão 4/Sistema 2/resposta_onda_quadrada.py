import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência da onda quadrada (rad/s)
omega = 10  # próximo da frequência natural do sistema

# Tempo
t = np.linspace(0, 5, 2000)
square_wave = signal.square(omega * t)

# Lista de βs
betas = [0.001, 0.01, 0.1, 1, 10]

plt.figure(figsize=(10, 6))
for beta in betas:
    num = [1, 1e4]
    den = [1, 2*beta, 100]
    sys = signal.TransferFunction(num, den)
    tout, y, _ = signal.lsim(sys, U=square_wave, T=t)
    plt.plot(tout, y, label=f'β = {beta}')

# Entrada escalada para comparação
plt.plot(t, 100 * square_wave, '--', color='grey', lw=1, label='Entrada (×100)')

plt.title('Resposta à Onda Quadrada — Sistema 2')
plt.xlabel('Tempo (s)')
plt.ylabel('y(t)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()