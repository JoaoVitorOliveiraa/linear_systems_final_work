import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Função de transferência: H(s) = 1 / (s^2 + s + 1)
num = [1]
den = [1, 1, 1]
system = signal.TransferFunction(num, den)

# Resposta ao degrau
t, y = signal.step(system)

# Gráfico
plt.figure(figsize=(8, 5))
plt.plot(t, y, label='y(t)')
plt.title('Resposta ao Degrau Unitário – Questão 3')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída y(t)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()