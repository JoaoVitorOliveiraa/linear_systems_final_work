import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ── Parâmetros do circuito ────────────────────────────────
R1 = R2 = 10e3          # 10 kΩ
C1 = 100e-9             # 100 nF
C2 = 15e-9              # 15 nF
K       = C1 / (C2 * R1 * R2)
omega_0 = (1/R1 + 1/R2) / C2
system  = signal.TransferFunction([K], [1, omega_0])

# ── Entrada rampa unitária  u(t)=t·u(t) ───────────────────
t = np.linspace(0, 5/omega_0, 5000)
u = t
t_out, y, _ = signal.lsim(system, U=u, T=t)

# ── Gráfico (saída em pico-volts para enxergar) ───────────
plt.figure(figsize=(8,4))
plt.plot(t*1e3, y*1e12, label='Saída (pV)')
plt.plot(t*1e3, u, '--', alpha=.5, label='Entrada: rampa')
plt.title('Resposta à Rampa Unitária - Circuito 3')
plt.xlabel('Tempo [ms]'); plt.ylabel('Amplitude')
plt.grid(True); plt.legend(); plt.tight_layout()
plt.show()