import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Coeficientes do denominador de H(s) = 6666.67 / (s² + 2e4 s + 4.44e7)
a = 1
b = 20_000
c = 4.44e7

# Cálculo das raízes do denominador  (pólos)
delta = b**2 - 4*a*c
s1 = (-b + np.sqrt(delta)) / (2*a)
s2 = (-b - np.sqrt(delta)) / (2*a)

# Plot do plano-s
plt.figure(figsize=(8, 6))
plt.axhline(0, color='black', linewidth=0.6)  # eixo imaginário
plt.axvline(0, color='black', linewidth=0.6)  # eixo real
plt.scatter([s1, s2], [0, 0], marker='x', s=120, label='Pólos')
plt.title('Diagrama de Pólos – Circuito 6')
plt.xlabel('Re{s}')
plt.ylabel('Im{s}')
plt.grid(True, which='both', linestyle='--', linewidth=0.7)
plt.legend()
plt.xlim(-21000, 1000)
plt.ylim(-5000, 5000)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()