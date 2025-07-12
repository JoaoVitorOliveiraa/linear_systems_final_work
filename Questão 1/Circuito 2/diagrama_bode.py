import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Valores comerciais do circuito
R1 = 1e3          # 1 kΩ
R2 = 1e3          # 1 kΩ
C1 = 100e-9       # 100 nF
L1 = 0.253        # 253 mH

# Função de transferência H(s)
num = [R1 / L1, 0]
den = [1, (R1 + R2) / L1, 1 / (L1 * C1)]
sys = signal.TransferFunction(num, den)

# Frequência angular (logspace para o gráfico de Bode)
w = np.logspace(1, 6, 1000)  # de 10 rad/s a 1 MHz
w, mag, phase = signal.bode(sys, w)

# Plot do Diagrama de Bode (magnitude e fase em subplots)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Magnitude
ax1.semilogx(w, mag)
ax1.set_title("Diagrama de Bode - Circuito 2")
ax1.set_ylabel("Magnitude (dB)")
ax1.grid(which="both", linestyle="--", linewidth=0.5)

# Fase
ax2.semilogx(w, phase)
ax2.set_ylabel("Fase (graus)")
ax2.set_xlabel("Frequência (rad/s)")
ax2.grid(which="both", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()