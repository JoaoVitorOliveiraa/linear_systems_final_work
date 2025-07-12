import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência fundamental
omega = 10
t = np.linspace(0, 5, 2000)

# 1º harmônico da dente de serra: -2/π · sin(ωt)
saw_first_harmonic = (-2 / np.pi) * np.sin(omega * t)

# Valores de β
betas = [0.001, 0.01, 0.1, 1, 10]

plt.figure(figsize=(10, 6))
for beta in betas:
    num = [1, 1e4]
    den = [1, 2 * beta, 100]
    sys = signal.TransferFunction(num, den)
    tout, y, _ = signal.lsim(sys, U=saw_first_harmonic, T=t)
    plt.plot(tout, y, label=f'β = {beta}')

# Entrada escalada por 100 para referência
plt.plot(t, 100 * saw_first_harmonic, '--', color='grey', lw=1, label='1º Harmônico dente de serra ×100')

plt.title('Resposta ao 1º Harmônico da Dente de Serra — Sistema 2')
plt.xlabel('Tempo (s)')
plt.ylabel('y(t)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()