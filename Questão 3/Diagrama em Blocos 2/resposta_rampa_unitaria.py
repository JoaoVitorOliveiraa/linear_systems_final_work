import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Função de transferência: H(s) = 7 / (s² + 14s + 63)
num = [7]
den = [1, 14, 63]
system = signal.TransferFunction(num, den)

# Entrada rampa: x(t) = t -> X(s) = 1/s²
t = np.linspace(0, 5, 1000)
u_rampa = t  # entrada rampa

# Simulação da resposta
t_out, y_out, _ = signal.lsim(system, U=u_rampa, T=t)

# Plot da resposta
plt.figure(figsize=(7, 4))
plt.plot(t_out, y_out, lw=2, label='Saída $y(t)$')
plt.plot(t, u_rampa, 'k--', lw=1, label='Entrada rampa')
plt.title('Resposta à Rampa Unitária – Questão 3')
plt.xlabel('Tempo (s)')
plt.ylabel('y(t)')
plt.grid(True, ls=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()