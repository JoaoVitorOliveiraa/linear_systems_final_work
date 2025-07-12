import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# H(s) = -100 / s
num = [-100]
den = [1, 0]
sys = signal.TransferFunction(num, den)

# Frequência logarítmica de varredura
w = np.logspace(-1, 5, 800)  # de 0.1 a 100000 rad/s

# Obter magnitude e fase
w, mag, phase = signal.bode(sys, w)

# Gráfico Bode combinado
plt.figure(figsize=(10, 8))

# Magnitude
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)
plt.title('Diagrama de Bode – Circuito 7 (H(s) = -100/s)')
plt.ylabel('Magnitude (dB)')
plt.grid(True, which='both', ls='--')

# Fase
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)
plt.xlabel('Frequência (rad/s)')
plt.ylabel('Fase (graus)')
plt.grid(True, which='both', ls='--')

plt.tight_layout()
plt.show()