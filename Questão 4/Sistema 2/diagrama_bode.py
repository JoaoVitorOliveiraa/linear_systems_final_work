import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# --- parâmetros -------------------------------------------------------------
betas = [0.001, 0.01, 0.1, 1, 10]        # valores de β
w      = np.logspace(0, 6, 1000)         # 10^0 a 10^6 rad/s
num    = [1, 1e4]                        # numerador fixo  (s + 10⁴)

# --- figura com dois subplots empilhados -----------------------------------
fig, (ax_mag, ax_phase) = plt.subplots(2, 1, sharex=True, figsize=(10, 8))

for beta in betas:
    den = [1, 2*beta, 100]               # denominador dependente de β
    sys = signal.TransferFunction(num, den)

    w, mag, phase = signal.bode(sys, w=w)

    ax_mag.semilogx(w, mag,   label=f'β = {beta}')
    ax_phase.semilogx(w, phase, label=f'β = {beta}')

# --- ajustes de apresentação -----------------------------------------------
ax_mag.set_title('Diagrama de Bode - Sistema 2 (Todos os β)')
ax_mag.set_ylabel('Magnitude (dB)')
ax_mag.grid(True, which='both', linestyle=':')

ax_phase.set_xlabel('Frequência (rad/s)')
ax_phase.set_ylabel('Fase (graus)')
ax_phase.grid(True, which='both', linestyle=':')

ax_mag.legend()
plt.tight_layout()
plt.show()