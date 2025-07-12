import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Pólos e zeros da função H(s) = -100/s
poles = [0]
zeros = []

# Criar gráfico do plano s
fig, ax = plt.subplots()
ax.axhline(0, color='black', linewidth=1)  # eixo real
ax.axvline(0, color='black', linewidth=1)  # eixo imaginário

# Plotar pólos e zeros
ax.plot(np.real(poles), np.imag(poles), 'x', label='Pólos', markersize=10, color='red')
if zeros:
    ax.plot(np.real(zeros), np.imag(zeros), 'o', label='Zeros', markersize=10, color='blue')

# Ajustes visuais
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xlabel('Re')
ax.set_ylabel('Im')
ax.set_title('Diagrama de Pólos e Zeros – Circuito 7')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()