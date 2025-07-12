import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Função de transferência H(s) = (12s + 104)/(s + 4)
num = [12, 104]
den = [1, 4]
sys = signal.TransferFunction(num, den)

# Cálculo dos polos e zeros
zeros = sys.zeros
poles = sys.poles

# Gráfico
plt.figure(figsize=(8, 6))
plt.scatter(np.real(poles), np.imag(poles), marker='x', s=100, color='r', label='Pólos')
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', s=100, facecolors='none', edgecolors='b', label='Zeros')

# Configurações
plt.axhline(0, color='black', lw=0.5, linestyle='--')
plt.axvline(0, color='black', lw=0.5, linestyle='--')
plt.title('Diagrama de Pólos e Zeros – Questão 2', pad=20)
plt.xlabel('Eixo Real', labelpad=10)
plt.ylabel('Eixo Imaginário', labelpad=10)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()