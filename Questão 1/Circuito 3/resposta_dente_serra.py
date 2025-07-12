import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ── Parâmetros do circuito ──────────────────────────────────────────
R1 = R2 = 10e3           # 10 kΩ
C1 = 100e-9              # 100 nF
C2 = 15e-9               # 15 nF
K       = C1 / (C2 * R1 * R2)
omega_0 = (1/R1 + 1/R2) / C2
system  = signal.TransferFunction([K], [1, omega_0])

# ── Frequência fundamental da dente de serra ────────────────────────
f0 = omega_0 / (2 * np.pi)   # Hz  (escolha "sábia": f = ω₀/2π)
T  = 1 / f0
t  = np.linspace(0, 3*T, 6000)

# ── Geração da onda dente de serra ──────────────────────────────────
u = signal.sawtooth(2 * np.pi * f0 * t)        # amplitude ±1

# ── Resposta do sistema ─────────────────────────────────────────────
t_out, y, _ = signal.lsim(system, U=u, T=t)

# ── Gráfico (escala em pico-volts para visualizar) ─────────────────-
plt.figure(figsize=(10, 4))
plt.plot(t*1e3, y*1e12, label='Saída $v_{out}(t)$ (pV)')
plt.plot(t*1e3, u, '--', alpha=0.5, label='Entrada: dente de serra')
plt.title(f'Resposta a uma Dente de Serra – ω ≈ {omega_0:.0f} rad/s - Circuito 3')
plt.xlabel('Tempo [ms]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()