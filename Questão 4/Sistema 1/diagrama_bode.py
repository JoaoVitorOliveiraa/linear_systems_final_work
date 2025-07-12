import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Valores de α do enunciado
alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]

# Denominador fixo do Sistema 1
den = [1, 2, 2]

# Geração de grade log-espacial de frequência
w = np.logspace(-2, 3, 1000)   # 10⁻² a 10³ rad/s

# ---------- Figura com dois subplots (módulo e fase) ----------
fig, (ax_mag, ax_phase) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

for alpha in alphas:
    num = [alpha, 1]                   # numerador 1 + αs
    sys = signal.TransferFunction(num, den)   # sistema LTI
    w, mag, phase = signal.bode(sys, w)       # resposta em frequência
    ax_mag.semilogx(w, mag, label=f'α = {alpha}')
    ax_phase.semilogx(w, phase)

# ——— Configurações do gráfico ———
# Magnitude
ax_mag.set_title('Diagrama de Bode - Sistema 1 (Todos os α)')
ax_mag.set_ylabel('Magnitude [dB]')
ax_mag.grid(True, which='both', ls=':')
ax_mag.legend(fontsize='x-small', ncol=2)

# Fase
ax_phase.set_ylabel('Fase [graus]')
ax_phase.set_xlabel('Frequência [rad/s]')
ax_phase.grid(True, which='both', ls=':')

plt.tight_layout()
plt.show()
