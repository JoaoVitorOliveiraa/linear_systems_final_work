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

# ----------- Frequência da dente de serra -----------
omega = 100                     # rad/s
f = omega / (2 * np.pi)         # Hz
T = 1 / f
t = np.linspace(0, 2*T, 3000)   # dois períodos

# ----------- Onda dente de serra com Fourier (20 harmônicos) -----------
A = 2 / np.pi
v_in = np.zeros_like(t)

for k in range(1, 21):  # harmônicos k = 1 a 20
    v_in += ((-1)**(k+1)) * (1/k) * np.sin(k * omega * t)

v_in *= A

# ----------- Resposta do sistema -----------
t, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# ----------- Plot -----------
plt.figure(figsize=(9, 4))
plt.plot(t, v_in, 'k--', linewidth=1.5, label='Dente de Serra (20 harmônicos)')
plt.plot(t, v_out, 'tab:blue', linewidth=2, label='Resposta do circuito')
plt.title('Resposta à Onda Dente de Serra – Circuito 1 (ω = 100 rad/s)')
plt.xlabel('Tempo t (s)')
plt.ylabel('Tensão (V)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.show()