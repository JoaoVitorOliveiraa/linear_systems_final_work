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

# ----------- Frequência base e tempo -----------
omega = 100                      # rad/s
T = 2 * np.pi / omega
t = np.linspace(0, 2*T, 3000)    # dois períodos

# ----------- Entrada com 5 harmônicos ímpares -----------
A = 4 / np.pi
v_in = np.zeros_like(t)

for k in range(5):
    n = 2*k + 1
    v_in += (1/n) * np.sin(n * omega * t)

v_in *= A  # escalar comum

# ----------- Resposta do sistema -----------
t, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# ----------- Plot -----------
plt.figure(figsize=(9, 4))
plt.plot(t, v_in, 'k--', linewidth=1.5, label='5 Harmônicos da Onda Quadrada')
plt.plot(t, v_out, 'tab:purple', linewidth=2, label='Resposta do Circuito')
plt.title('Resposta aos 5 Primeiros Harmônicos da Onda Quadrada (ω = 100 rad/s) – Circuito 1')
plt.xlabel('Tempo t (s)')
plt.ylabel('Tensão (V)')
plt.legend(loc='lower left', bbox_to_anchor=(0, 0.05), frameon=True, framealpha=0.9)
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.show()