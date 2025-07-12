import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ----------- Parâmetros do circuito -----------
R1 = 10.0
R2 = 10.0
C1 = 100e-6
L1 = 1.0

# ----------- Função de transferência -----------
k = 1 / (C1 * R1)
b = (R1 + R2) / (C1 * R1 * R2)
c = 1 / (L1 * C1)
num = [k, 0]
den = [1, b, c]
sys = signal.TransferFunction(num, den)

# ----------- Tempo e frequência base -----------
omega = 100                   # rad/s
T = 2 * np.pi / omega
t = np.linspace(0, 2*T, 3000)

# ----------- Entrada: soma dos 3 primeiros harmônicos ímpares -----------
A = 4 / np.pi
v_in = A * (
    np.sin(omega * t) +
    (1/3) * np.sin(3 * omega * t) +
    (1/5) * np.sin(5 * omega * t)
)

# ----------- Resposta do sistema -----------
t, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# ----------- Plot -----------
plt.figure(figsize=(9, 4))
plt.plot(t, v_in, 'k--', lw=1.5, label='3 Primeiros Harmônicos da Onda Quadrada')
plt.plot(t, v_out, 'tab:red', lw=2, label='Resposta do circuito')
plt.title('Resposta aos 3 Primeiros Harmônicos da Onda Quadrada (ω = 100 rad/s) – Circuito 1')
plt.xlabel('Tempo t (s)')
plt.ylabel('Tensão (V)')
plt.legend(loc='lower left', bbox_to_anchor=(0, 0.05), frameon=True, framealpha=0.9)
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.show()