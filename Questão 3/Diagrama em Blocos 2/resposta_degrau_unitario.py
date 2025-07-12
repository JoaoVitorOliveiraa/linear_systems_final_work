import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Definição da função de transferência: H(s) = 7 / (s^2 + 14s + 63)
num = [7]
den = [1, 14, 63]
system = signal.TransferFunction(num, den)

# Cálculo da resposta ao degrau unitário
t, y = signal.step(system)

# Plot do gráfico
plt.figure(figsize=(7, 4))
plt.plot(t, y, color='blue', lw=2)
plt.title('Resposta ao Degrau Unitário – Questão 3')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída $y(t)$')
plt.grid(True, ls=':', alpha=0.7)
plt.tight_layout()
plt.show()