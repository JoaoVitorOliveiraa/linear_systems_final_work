import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Função de transferência H(s) = (12s + 104)/(s + 4)
num = [12, 104]
den = [1, 4]
system = signal.TransferFunction(num, den)

# Resposta ao degrau
t, y = signal.step(system)

# Gráfico
plt.figure(figsize=(8, 5))
plt.plot(t, y, label='y(t)')
plt.title('Resposta ao Degrau Unitário – Questão 2')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída y(t)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()