import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# --- parâmetros do circuito ---
R = 10e3       # 10 kΩ
C = 15e-9      # 15 nF

# --- função de transferência H(s) ---
num = [1 / (R * C)]                       # 1/RC
den = [1, 3 / (R * C), 1 / (R**2 * C**2)] # s² + (3/RC)s + 1/(R²C²)
sys = signal.TransferFunction(num, den)

# --- resposta ao degrau unitário ---
t, y = signal.step(sys)

# --- plot ---
plt.figure(figsize=(9, 5))
plt.plot(t, y, label='y(t) – resposta ao degrau')
plt.axhline(y[-1], color='r', ls=':', label=f'Valor final ≈ {y[-1]:.4e} V')
plt.title('Resposta ao Degrau Unitário – Circuito 6')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True, ls='--')
plt.legend()
plt.tight_layout()
plt.show()