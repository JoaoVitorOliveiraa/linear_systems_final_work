import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ---- Função de transferência H(s) = 7 / (s² + 14 s + 63) ----
num = [7]
den = [1, 14, 63]
sys = signal.TransferFunction(num, den)

# ---- Cálculo do Bode ---------------------------------------
w = np.logspace(0, 3, 1000)          # 1   rad/s  → 1000 rad/s
w, mag, phase = signal.bode(sys, w)

# ---- Plot --------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

ax1.semilogx(w, mag, lw=1.8)
ax1.set_ylabel('Magnitude (dB)')
ax1.set_title(r'Diagrama de Bode – Questão 3')
ax1.grid(True, which='both', ls=':', alpha=0.7)

ax2.semilogx(w, phase, color='tab:orange', lw=1.8)
ax2.set_ylabel('Fase (graus)')
ax2.set_xlabel('Frequência (rad/s)')
ax2.grid(True, which='both', ls=':', alpha=0.7)

plt.tight_layout()
plt.show()