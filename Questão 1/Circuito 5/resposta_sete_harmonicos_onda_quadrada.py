import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros do circuito
R1 = 10e3         # 10 kΩ
C = 100e-9       # 100 nF
RC = R1 * C

# Frequência fundamental
omega = 500 * np.pi          # rad/s
f = omega / (2 * np.pi)
t = np.linspace(0, 8 / f, 4000)

# Entrada com 7 harmônicos ímpares: n = 1, 3, 5, 7, 9, 11, 13
harmonics = [1, 3, 5, 7, 9, 11, 13]
v_in = (4 / np.pi) * sum((1/n) * np.sin(n * omega * t) for n in harmonics)

# Sistema integrador
num = [1]
den = [RC, 0]
sys = signal.TransferFunction(num, den)

# Resposta à entrada harmônica
t_out, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# Plotagem
plt.figure(figsize=(10, 4))
plt.plot(t, v_in, '--', color='gray', lw=1.4, label=r'$v_{\mathrm{in}}^{(7)}(t)$')
plt.plot(t_out, v_out, 'tab:blue', lw=2, label=r'$v_{\mathrm{out}}^{(7)}(t)$')
plt.title('Resposta aos 7 Primeiros Harmônicos da Onda Quadrada – Circuito 5')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('Tensão (V)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()