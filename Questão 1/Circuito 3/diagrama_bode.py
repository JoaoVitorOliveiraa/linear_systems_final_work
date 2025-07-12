import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ─── Parâmetros do circuito ────────────────────────────────────────────────────
R1 = R2 = 10e3      # 10 kΩ
C1 = 100e-9         # 100 nF
C2 = 15e-9          # 15 nF

# ─── Função de transferência H(s) = K / (s + ω0) ───────────────────────────────
K       = C1 / (C2 * R1 * R2)        # ganho (afeta apenas a magnitude)
omega_0 = (1/R1 + 1/R2) / C2         # posição do pólo

num = [K]            # numerador
den = [1, omega_0]   # denominador s + ω0
system = signal.TransferFunction(num, den)

# ─── Cálculo do Bode ───────────────────────────────────────────────────────────
w = np.logspace(2, 6, 1000)          # 10² a 10⁶ rad/s
w, mag, phase = signal.bode(system, w=w)

# ─── Plot: magnitude e fase na mesma figura ────────────────────────────────────
fig, axs = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Magnitude
axs[0].semilogx(w, mag)
axs[0].set_title('Diagrama de Bode – Circuito 3')
axs[0].set_ylabel('Magnitude [dB]')
axs[0].grid(which='both', linestyle='--')

# Fase
axs[1].semilogx(w, phase)
axs[1].set_xlabel('Frequência [rad/s]')
axs[1].set_ylabel('Fase [graus]')
axs[1].grid(which='both', linestyle='--')

plt.tight_layout()
plt.show()