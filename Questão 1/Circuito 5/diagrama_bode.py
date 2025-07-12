import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# --------- parâmetros do circuito ----------
R1 = 10e3       # 10 kΩ
C2 = 100e-9     # 100 nF

# --------- H(s) = 1 / (R1·C2·s) -------------
num = [1]
den = [R1 * C2, 0]           # (R1·C2)·s

sys = signal.TransferFunction(num, den)

# --------- cálculo do Bode ------------------
w = np.logspace(0, 6, 1000)  # 1 rad/s → 1 M rad/s
w, mag, phase = signal.bode(sys, w)

# --------- gráfico --------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6), sharex=True)

ax1.semilogx(w, mag, lw=1.8)
ax1.set_ylabel('Magnitude (dB)')
ax1.set_title('Diagrama de Bode – Circuito 5')
ax1.grid(which='both', ls=':', alpha=0.7)

ax2.semilogx(w, phase, color='tab:orange', lw=1.8)
ax2.set_ylabel('Fase (graus)')
ax2.set_xlabel('Frequência (rad/s)')
ax2.grid(which='both', ls=':', alpha=0.7)

plt.tight_layout()
plt.show()