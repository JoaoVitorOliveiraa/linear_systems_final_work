import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ── Parâmetros do circuito ────────────────────────────────
R1 = R2 = 10e3
C1 = 100e-9
C2 = 15e-9
K       = C1 / (C2 * R1 * R2)
omega_0 = (1/R1 + 1/R2) / C2
system  = signal.TransferFunction([K], [1, omega_0])

# ── Entrada: onda quadrada de frequência ω0 ───────────────
f0 = omega_0 / (2*np.pi)
T  = 1 / f0
t  = np.linspace(0, 5*T, 5000)
u  = signal.square(2*np.pi*f0*t)

t_out, y, _ = signal.lsim(system, U=u, T=t)

# ── Gráfico (saída em pico-volts) ─────────────────────────
plt.figure(figsize=(8,4))
plt.plot(t*1e3, y*1e12, label='Saída (pV)')
plt.plot(t*1e3, u, '--', alpha=.5, label='Entrada: onda quadrada')
plt.title('Resposta à Onda Quadrada – ω ≈ %.0f rad/s - Circuito 3' % omega_0)
plt.xlabel('Tempo [ms]'); plt.ylabel('Amplitude')
plt.grid(True); plt.legend(); plt.tight_layout()
plt.legend(loc='lower left', bbox_to_anchor=(0, 0.05), frameon=True, framealpha=0.9)
plt.show()