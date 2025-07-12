import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Função de transferência H(s) = (12s + 104)/(s + 4)
num = [12, 104]
den = [1, 4]
system = signal.TransferFunction(num, den)

# Frequências e resposta de Bode
w, mag, phase = signal.bode(system)

# Plot
plt.figure(figsize=(10, 8))

# Magnitude
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)
plt.title('Diagrama de Bode – Questão 2')
plt.ylabel('Magnitude (dB)')
plt.grid(True, which='both', linestyle=':')

# Fase
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)
plt.xlabel('Frequência (rad/s)')
plt.ylabel('Fase (graus)')
plt.grid(True, which='both', linestyle=':')

plt.tight_layout()
plt.show()
