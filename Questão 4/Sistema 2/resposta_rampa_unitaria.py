import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Valores de β
betas = [0.001, 0.01, 0.1, 1, 10]

# Tempo de simulação (0–5 s)
t = np.linspace(0, 5, 2000)
u = t                                   # rampa unitária

plt.figure(figsize=(10, 6))
for beta in betas:
    num, den = [1, 1e4], [1, 2*beta, 100]
    sys      = signal.TransferFunction(num, den)
    tout, y, _ = signal.lsim(sys, U=u, T=t)
    plt.plot(tout, y, label=f'β = {beta}')

# Reta 100·t (ganho DC) para referência
plt.plot(t, 100*t, '--', color='grey', lw=1, label='100·t (slope esperada)')

plt.title('Resposta à Rampa Unitária — Sistema 2')
plt.xlabel('Tempo (s)')
plt.ylabel('y(t)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()