import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# ----- parâmetros do circuito -----
R1 = 10.0          # Ω
R2 = 10.0          # Ω
C1 = 100e-6        # 100 µF
L1 = 1.0           # 1 H

# ----- função de transferência H(s) -----
k = 1 / (C1 * R1)
b = (R1 + R2) / (C1 * R1 * R2)
c = 1 / (L1 * C1)
num = [k, 0]        # k·s
den = [1, b, c]     # s² + b·s + c
sys = signal.TransferFunction(num, den)

# ----- resposta ao degrau -----
t, y = signal.step(sys)     # step de amplitude 1

# ----- plot -----
plt.figure(figsize=(7, 4))
plt.plot(t, y, linewidth=2)
plt.title('Resposta ao Degrau Unitário – Circuito 1')
plt.xlabel('Tempo t (s)')
plt.ylabel('v_out(t)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.show()