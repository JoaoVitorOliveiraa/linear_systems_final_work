import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# --- parâmetros do integrador ---
R1 = 10e3        # 10 kΩ
C2 = 100e-9      # 100 nF

# função de transferência: H(s) = 1 / (R1 * C2 * s)
num = [1]
den = [R1 * C2, 0]
sys = signal.TransferFunction(num, den)

# --- sinal de entrada: rampa unitária v_in(t) = t·u(t) ---
t = np.linspace(0, 0.06, 1000)     # 0 a 60 ms
v_in = t                           # rampa de inclinação 1 V/s

# --- resposta do sistema ---
t_out, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# --- plot ---
plt.figure(figsize=(8, 4))
plt.plot(t, v_in, '--', color='gray', label=r'$v_{\mathrm{in}}(t)=t$')
plt.plot(t_out, v_out, color='tab:blue', lw=2, label=r'$v_{\mathrm{out}}(t)$')
plt.title('Resposta à Rampa Unitária – Circuito 5')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('Tensão (V)')
plt.grid(True, ls=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()