import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# -------- parâmetros do circuito --------
R1 = 10e3          # 10 kΩ
C = 100e-9        # 100 nF
RC = R1 * C       # 1 ms

# -------- frequência fundamental --------
omega = 500 * np.pi            # rad/s  (f = 250 Hz)
f = omega / (2 * np.pi)
t = np.linspace(0, 8 / f, 4000)   # 8 períodos

# -------- entrada: 5 harmônicos ímpares -----------
harmonics = [1, 3, 5, 7, 9]
v_in = (4 / np.pi) * sum((1/n) * np.sin(n * omega * t) for n in harmonics)

# -------- sistema integrador ----------------------
num = [1]
den = [RC, 0]
sys = signal.TransferFunction(num, den)

# -------- resposta do sistema ---------------------
t_out, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# -------- plotagem -------------------------------
plt.figure(figsize=(10, 4))
plt.plot(t, v_in, '--', color='gray', lw=1.4, label=r'$v_{\mathrm{in}}^{(5)}(t)$')
plt.plot(t_out, v_out, color='tab:blue', lw=2, label=r'$v_{\mathrm{out}}^{(5)}(t)$')
plt.title('Resposta aos 5 Primeiros Harmônicos da Onda Quadrada – Circuito 5')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('Tensão (V)')
plt.grid(True, ls=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()