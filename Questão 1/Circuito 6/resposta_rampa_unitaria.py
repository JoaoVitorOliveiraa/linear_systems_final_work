import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# --- parâmetros do circuito ---
R = 10e3       # 10 kΩ
C = 15e-9      # 15 nF

# --- função de transferência H(s) = (1/RC)/(s² + (3/RC)s + 1/(R²C²)) ---
num = [1 / (R * C)]
den = [1, 3 / (R * C), 1 / (R**2 * C**2)]
sys = signal.TransferFunction(num, den)

# --- entrada: rampa unitária x(t) = t·u(t) ---
t = np.linspace(0, 0.01, 1000)   # 0–10 ms
u = t                             # rampa

# --- resposta usando lsim ---
t_out, y_out, _ = signal.lsim(sys, U=u, T=t)

# --- gráfico ---
plt.figure(figsize=(9, 5))
plt.plot(t_out, y_out, label='y(t) – resposta à rampa')
plt.title('Resposta à Rampa Unitária – Circuito 6')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()