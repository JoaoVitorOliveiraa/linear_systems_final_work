import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# --- Parâmetros do circuito ---
R1 = 10e3       # 10 kΩ
C2 = 100e-9     # 100 nF

# --- Função de transferência H(s) = 1 / (R1 * C2 * s) ---
num = [1]
den = [R1 * C2, 0]  # H(s) = 1 / (0.001 * s)

# Criação do sistema de transferência
sys = signal.TransferFunction(num, den)

# Cálculo dos polos e zeros
zeros = np.roots(num)    # Nenhum zero finito
poles = np.roots(den)    # Polo em s = 0

# --- Plotagem ---
plt.figure(figsize=(6, 4))
plt.scatter(np.real(poles), np.imag(poles), marker='x', s=100, color='red', label='Pólos')
if zeros.size > 0:
    plt.scatter(np.real(zeros), np.imag(zeros), marker='o', s=100, facecolors='none', edgecolors='blue', label='Zeros')

plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.axvline(0, color='black', linestyle='--', linewidth=0.5)

plt.title('Diagrama de Pólos e Zeros – Circuito 5')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()