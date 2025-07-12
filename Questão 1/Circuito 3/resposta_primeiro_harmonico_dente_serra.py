import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ── Parâmetros do circuito ─────────────────────────────────────────────
R1 = R2 = 10e3           # 10 kΩ
C1 = 100e-9              # 100 nF
C2 = 15e-9               # 15 nF

# Função de transferência: H(s) = K / (s + ω₀)
K = C1 / (C2 * R1 * R2)
omega_0 = (1/R1 + 1/R2) / C2
system  = signal.TransferFunction([K], [1, omega_0])

# ── Frequência fundamental da dente de serra ───────────────────────────
f0 = omega_0 / (2 * np.pi)  # Hz
T  = 1 / f0
t  = np.linspace(0, 3*T, 6000)

# ── Entrada: 1º harmônico da dente de serra ────────────────────────────
# Série de Fourier: x₁(t) = (2/π)·sin(ωt)
u = (2 / np.pi) * np.sin(2 * np.pi * f0 * t)

# ── Resposta do sistema ────────────────────────────────────────────────
t_out, y, _ = signal.lsim(system, U=u, T=t)

# ── Gráfico da resposta ────────────────────────────────────────────────
plt.figure(figsize=(10, 4))
plt.plot(t * 1e3, y * 1e12, label='Saída $v_{out}(t)$ (pV)')
plt.plot(t * 1e3, u, '--', label='Entrada: 1º harmônico (dente de serra)', alpha=0.5)
plt.title(f'Resposta ao 1º Harmônico da Dente de Serra – ω ≈ {omega_0:.0f} rad/s - Circuito 3')
plt.xlabel('Tempo [ms]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()