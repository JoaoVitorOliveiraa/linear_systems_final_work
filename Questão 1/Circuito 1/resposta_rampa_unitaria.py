import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# --- Parâmetros do circuito ---
R1 = 10.0        # Ω
R2 = 10.0        # Ω
C1 = 100e-6      # 100 µF
L1 = 1.0         # 1 H

# --- Função de transferência H(s) ---
k = 1 / (C1 * R1)
b = (R1 + R2) / (C1 * R1 * R2)
c = 1 / (L1 * C1)
num = [k, 0]
den = [1, b, c]
sys = signal.TransferFunction(num, den)

# --- Entrada: rampa unitária → V_in(s) = 1 / s^2
# Para simular, usamos resposta à entrada rampa (input = t)
t = np.linspace(0, 0.01, 1000)
u_rampa = t
t, y_rampa, _ = signal.lsim(sys, U=u_rampa, T=t)

# --- Plot ---
plt.figure(figsize=(7, 4))
plt.plot(t, y_rampa, linewidth=2, label='v_out(t)')
plt.plot(t, u_rampa, 'k--', alpha=0.5, label='v_in(t) = t')
plt.title('Resposta à Rampa Unitária – Circuito 1')
plt.xlabel('Tempo t (s)')
plt.ylabel('v_out(t)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.show()