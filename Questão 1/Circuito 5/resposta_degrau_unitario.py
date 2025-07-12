import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros do circuito
R1 = 10e3        # 10 kΩ
C2 = 100e-9      # 100 nF

# Função de transferência H(s) = 1 / (R1 * C2 * s)
num = [1]
den = [R1 * C2, 0]
sys = signal.TransferFunction(num, den)

# Entrada: degrau unitário
t = np.linspace(0, 0.06, 1000)   # 0 a 60 ms
v_in = np.ones_like(t)          # u(t)

# Resposta ao degrau
t_out, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# Gráfico
plt.figure(figsize=(8, 4))
plt.plot(t, v_in, '--', color='gray', label=r'$v_{\mathrm{in}}(t)=u(t)$')
plt.plot(t_out, v_out, color='tab:blue', lw=2, label=r'$v_{\mathrm{out}}(t)$')
plt.title('Resposta ao Degrau Unitário – Circuito 5')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('Tensão (V)')
plt.grid(True, ls=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()