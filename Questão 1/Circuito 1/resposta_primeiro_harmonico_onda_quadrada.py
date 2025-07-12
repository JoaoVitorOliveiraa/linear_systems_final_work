import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ----------- Parâmetros do circuito -----------
R1 = 10.0       # Ω
R2 = 10.0       # Ω
C1 = 100e-6     # 100 µF
L1 = 1.0        # 1 H

# ----------- Função de transferência H(s) -----------
k = 1 / (C1 * R1)
b = (R1 + R2) / (C1 * R1 * R2)
c = 1 / (L1 * C1)
num = [k, 0]
den = [1, b, c]
sys = signal.TransferFunction(num, den)

# ----------- Frequência do 1º harmônico -----------
omega = 100                   # rad/s
f = omega / (2 * np.pi)       # Hz
T = 1 / f
t = np.linspace(0, 2*T, 2000)

# ----------- Entrada: primeiro harmônico de onda quadrada -----------
A = 4 / np.pi
v_in = A * np.sin(omega * t)

# ----------- Resposta do sistema -----------
t, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# ----------- Plot -----------
plt.figure(figsize=(9, 4))
plt.plot(t, v_in, 'k--', linewidth=1.5, label='1º Harmônico da Onda Quadrada')
plt.plot(t, v_out, 'tab:blue', linewidth=2, label='Resposta do Circuito')
plt.title('Resposta ao 1º Harmônico da Onda Quadrada (ω = 100 rad/s) – Circuito 1')
plt.xlabel('Tempo t (s)')
plt.ylabel('Tensão (V)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()