import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# === Parâmetros do circuito ===
R1 = 10.0          # Ω
R2 = 10.0          # Ω
C1 = 100e-6        # 100 µF
L1 = 1.0           # 1 H

# === Função de transferência H(s) ===
k = 1 / (C1 * R1)
b = (R1 + R2) / (C1 * R1 * R2)
c = 1 / (L1 * C1)
num = [k, 0]           # k·s
den = [1, b, c]        # s² + b·s + c
sys = signal.TransferFunction(num, den)

# === Bode: frequência, magnitude (dB) e fase (graus) ===
w = np.logspace(0, 5, 1000)          # 1 rad/s → 100 krad/s
w, mag, phase = signal.bode(sys, w=w)

# === Plot conjunto (magnitude + fase) ===
fig, (ax_mag, ax_phase) = plt.subplots(
    2, 1, figsize=(8, 6), sharex=True
)

ax_mag.semilogx(w, mag, color='navy', linewidth=2)
ax_mag.set_ylabel('Magnitude (dB)')
ax_mag.set_title('Diagrama de Bode – Circuito 1')
ax_mag.grid(True, which='both', linestyle=':', alpha=0.7)

ax_phase.semilogx(w, phase, color='darkorange', linewidth=2)
ax_phase.set_xlabel('Frequência angular ω (rad/s)')
ax_phase.set_ylabel('Fase (graus)')
ax_phase.grid(True, which='both', linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()