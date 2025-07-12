import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ---------- parâmetros do circuito ----------
R1 = 10.0       # Ω
R2 = 10.0       # Ω
C1 = 100e-6     # 100 µF
L1 = 1.0        # 1 H

# ---------- função de transferência ----------
k = 1 / (C1 * R1)
b = (R1 + R2) / (C1 * R1 * R2)
c = 1 / (L1 * C1)
num = [k, 0]
den = [1, b, c]
sys = signal.TransferFunction(num, den)

# ---------- onda quadrada de frequência "sábia" ----------
omega = 100            # rad/s
f = omega / (2 * np.pi)  # Hz
T = 1 / f               # período
t = np.linspace(0, 4*T, 4000)          # 4 períodos
v_in = signal.square(omega * t)        # amplitude ±1 V

# ---------- resposta do sistema ----------
t, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# ---------- plot ----------
plt.figure(figsize=(9, 4))
plt.plot(t, v_in, label='v_in(t): onda quadrada', lw=1.8, color='k')
plt.plot(t, v_out, '--', label='v_out(t)', lw=1.8, color='tab:orange')
plt.title('Resposta à Onda Quadrada – Circuito 1  (ω = 100 rad/s)')
plt.xlabel('Tempo t (s)')
plt.ylabel('Tensão (V)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()