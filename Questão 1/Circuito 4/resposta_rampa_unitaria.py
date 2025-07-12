import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Vetor de tempo (0 a 1 s, 1000 pontos)
t = np.linspace(0, 1, 1000)

# Rampa unitária: v_out(t) = t para t ≥ 0
y = t  # porque H(s)=1 → saída = entrada

# Plot
plt.figure(figsize=(6, 4))
plt.plot(t, y, linewidth=2)
plt.title('Resposta à Rampa Unitária – Circuito 4')
plt.xlabel('Tempo t (s)')
plt.ylabel('v_out(t)')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.ylim(-0.05, 1.05)
plt.xlim(0, 1)
plt.show()