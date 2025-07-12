import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequência fundamental da dente de serra
omega = 10
t = np.linspace(0, 5, 2000)

# Construção da série com os 5 primeiros harmônicos
# Fórmula: x(t) = −2/π Σ (1/n)·sin(nωt)
harmonics = [1, 2, 3, 4, 5]
saw_sum = np.zeros_like(t)
for n in harmonics:
    A_n = -2 / (np.pi * n)
    saw_sum += A_n * np.sin(n * omega * t)

# Parâmetros β a serem testados
betas = [0.001, 0.01, 0.1, 1, 10]

plt.figure(figsize=(10, 6))

for beta in betas:
    # Função de transferência: (s + 10⁴)/(s² + 2βs + 100)
    num = [1, 1e4]
    den = [1, 2 * beta, 100]
    sys = signal.TransferFunction(num, den)

    # Resposta à entrada harmônica
    tout, y, _ = signal.lsim(sys, U=saw_sum, T=t)
    plt.plot(tout, y, label=f'β = {beta}')

# Entrada (série dos 5 harmônicos) escalada ×100 para referência visual
plt.plot(t, 100 * saw_sum, '--', color='grey', lw=1,
         label='Série (5 harmônicos - dente de serra) ×100')

plt.title('Resposta aos 5 Primeiros Harmônicos da Dente de Serra — Sistema 2')
plt.xlabel('Tempo (s)')
plt.ylabel('y(t)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()