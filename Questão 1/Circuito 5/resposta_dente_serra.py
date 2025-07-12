import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros do circuito
R1 = 10e3          # 10 kΩ
C = 100e-9        # 100 nF
RC = R1 * C

# Frequência e tempo
omega = 500 * np.pi
f = omega / (2 * np.pi)
T = 1 / f
t = np.linspace(0, 5*T, 4000)

# Geração da onda dente de serra normalizada (-1 a 1)
v_in = signal.sawtooth(omega * t, width=1.0)

# Sistema integrador
num = [1]
den = [RC, 0]
sys = signal.TransferFunction(num, den)

# Resposta à entrada
t_out, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# Plotagem
plt.figure(figsize=(10, 4))
plt.plot(t, v_in, '--', color='gray', lw=1.4, label=r'$v_{\mathrm{in}}(t)$ (Dente de Serra)')
plt.plot(t_out, v_out, 'b', lw=2, label=r'$v_{\mathrm{out}}(t)$')
plt.title('Resposta à Onda Dente de Serra – Circuito 5')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('Tensão (V)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()