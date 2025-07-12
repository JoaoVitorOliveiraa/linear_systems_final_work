import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Vetor de tempo de 0 a 1 segundo com 1000 pontos
t = np.linspace(0, 1, 1000)

# Resposta ao degrau unitário: v_out(t) = 1 para t ≥ 0
y = np.ones_like(t)

# Plot da resposta
plt.figure(figsize=(6, 4))
plt.plot(t, y, linewidth=2)
plt.title('Resposta ao Degrau Unitário – Circuito 4')
plt.xlabel('Tempo t (s)')
plt.ylabel('v_out(t)')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.ylim(-0.1, 1.1)
plt.xlim(0, 1)
plt.show()