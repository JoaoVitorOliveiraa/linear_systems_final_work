import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ─── Parâmetros do Circuito ───────────────────────────────────
R1 = R2 = 10e3           # Resistores de 10kΩ
C1 = 100e-9              # Capacitor C1 = 100nF
C2 = 15e-9               # Capacitor C2 = 15nF

# Função de transferência H(s) = K / (s + ω0)
K = C1 / (C2 * R1 * R2)
omega0 = (1/R1 + 1/R2) / C2
system = signal.TransferFunction([K], [1, omega0])

# ─── Sinal de entrada: 3 primeiros harmônicos da onda quadrada ───
f0 = omega0 / (2 * np.pi)  # Frequência fundamental
T = 1 / f0
t = np.linspace(0, 3*T, 5000)

# Série de Fourier: soma dos 3 primeiros harmônicos ímpares
u = np.zeros_like(t)
for k in [1, 3, 5]:
    u += (4 / (np.pi * k)) * np.sin(2 * np.pi * f0 * k * t)

# ─── Resposta do sistema ─────────────────────────────────────────
t_out, y, _ = signal.lsim(system, U=u, T=t)

# ─── Gráfico ─────────────────────────────────────────────────────
plt.figure(figsize=(10, 4))
plt.plot(t * 1e3, y * 1e12, label='Saída $v_{out}(t)$ (pV)')
plt.plot(t * 1e3, u, '--', label='Entrada: 3 harmônicos', alpha=0.5)
plt.title('Resposta aos 3 Primeiros Harmônicos da Onda Quadrada - Circuito 3')
plt.xlabel('Tempo [ms]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()