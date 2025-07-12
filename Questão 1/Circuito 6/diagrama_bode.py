import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ------ parâmetros do circuito ------
R = 10e3      # 10 kΩ
C = 15e-9     # 15 nF

# ------ função de transferência H(s) ------
num = [1 / (R * C)]                 # 1 / (RC)
den = [1, 3 / (R * C), 1 / (R**2 * C**2)]

system = signal.TransferFunction(num, den)

# ------ varredura de frequência ------
w = np.logspace(2, 6, 1000)         # 10² a 10⁶ rad/s
w, mag, phase = signal.bode(system, w)

# ------ gráfico combinado ------
plt.figure(figsize=(10, 8))

# Magnitude
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)
plt.title('Diagrama de Bode – Circuito 6')
plt.ylabel('Magnitude (dB)')
plt.grid(True, which='both', linestyle='--')

# Fase
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)
plt.xlabel('Frequência (rad/s)')
plt.ylabel('Fase (graus)')
plt.grid(True, which='both', linestyle='--')

plt.tight_layout()
plt.show()