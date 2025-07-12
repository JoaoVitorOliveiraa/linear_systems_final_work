import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ---------------------------------------------
# 1) Faixa de frequência (rad/s) – escala log
# ---------------------------------------------
w = np.logspace(0, 6, 1000)          # 1 rad/s a 1 M rad/s

# ---------------------------------------------
# 2) Função de transferência H(s) = 1
#    →  |H| = 1  →  0 dB
#    →  ∠H = 0°
# ---------------------------------------------
H_mag_db    = 20 * np.log10(np.ones_like(w))  # 0 dB
H_phase_deg = np.zeros_like(w)                # 0°

# ---------------------------------------------
# 3) Criação de subplots (2 linhas, 1 coluna)
# ---------------------------------------------
fig, axs = plt.subplots(2, 1,
                        figsize=(8, 6),
                        sharex=True)

# --- Magnitude ---
axs[0].semilogx(w, H_mag_db, linewidth=2)
axs[0].set_title('Diagrama de Bode – Circuito 4')
axs[0].set_ylabel('Magnitude (dB)')
axs[0].grid(True, which='both',
            linestyle='--', linewidth=0.5)
axs[0].set_ylim(-1, 1)               # zoom em torno de 0 dB

# --- Fase ---
axs[1].semilogx(w, H_phase_deg, linewidth=2)
axs[1].set_xlabel('Frequência angular ω (rad/s)')
axs[1].set_ylabel('Fase (graus)')
axs[1].grid(True, which='both',
            linestyle='--', linewidth=0.5)
axs[1].set_ylim(-10, 10)             # zoom em torno de 0°

plt.tight_layout()
plt.show()