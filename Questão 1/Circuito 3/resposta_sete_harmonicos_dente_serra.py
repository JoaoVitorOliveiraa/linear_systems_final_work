import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ─── Parâmetros do circuito ──────────────────────────────────────────────
R1 = R2 = 10e3           # 10 kΩ
C1 = 100e-9              # 100 nF
C2 = 15e-9               # 15 nF

K = C1 / (C2 * R1 * R2)
omega_0 = (1/R1 + 1/R2) / C2
system  = signal.TransferFunction([K], [1, omega_0])

# ─── Frequência fundamental da onda dente de serra ───────────────────────
f0 = omega_0 / (2 * np.pi)   # Hz
T  = 1 / f0
t  = np.linspace(0, 3*T, 6000)

# ─── Entrada: 7 primeiros harmônicos da dente de serra ──────────────────
u = np.zeros_like(t)
for k in range(1, 8):  # k = 1 a 7
    coef = (2 / np.pi) * ((-1)**(k + 1) / k)
    u += coef * np.sin(2 * np.pi * f0 * k * t)

# ─── Resposta do sistema ─────────────────────────────────────────────────
t_out, y, _ = signal.lsim(system, U=u, T=t)

# ─── Gráfico (saída em pico-volts para visualização) ────────────────────
plt.figure(figsize=(10, 4))
plt.plot(t*1e3, y*1e12, label='Saída $v_{out}(t)$ (pV)')
plt.plot(t*1e3, u, '--', label='Entrada: 7 harmônicos', alpha=0.5)
plt.title('Resposta aos 7 Primeiros Harmônicos da Dente de Serra - Circuito 3')
plt.xlabel('Tempo [ms]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()