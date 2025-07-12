import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ── Parâmetros do circuito ─────────────────────────────────────────
R1 = R2 = 10e3         # 10 kΩ
C1 = 100e-9            # 100 nF
C2 = 15e-9             # 15 nF

# Função de transferência H(s) = K /(s + ω0)
K       = C1 / (C2 * R1 * R2)
omega_0 = (1/R1 + 1/R2) / C2
system  = signal.TransferFunction([K], [1, omega_0])

# ── Frequência fundamental e malha de tempo ───────────────────────
f0 = omega_0 / (2*np.pi)      # Hz
T  = 1 / f0
t  = np.linspace(0, 3*T, 6000)

# ── Entrada: 7 harmônicos ímpares (k = 1,3,5,7,9,11,13) ───────────
u = np.zeros_like(t)
for k in range(1, 14, 2):     # 1, 3, 5, 7, 9, 11, 13
    u += (4 / (np.pi * k)) * np.sin(2 * np.pi * f0 * k * t)

# ── Resposta do sistema ───────────────────────────────────────────
t_out, y, _ = signal.lsim(system, U=u, T=t)

# ── Gráfico (saída escalada em pV para visibilidade) ──────────────
plt.figure(figsize=(10, 4))
plt.plot(t*1e3, y*1e12, label='Saída $v_{out}(t)$ (pV)')
plt.plot(t*1e3, u, '--', alpha=0.5, label='Entrada: 7 harmônicos')
plt.title('(o) Resposta aos 7 Primeiros Harmônicos da Onda Quadrada - Circuito 3')
plt.xlabel('Tempo [ms]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()