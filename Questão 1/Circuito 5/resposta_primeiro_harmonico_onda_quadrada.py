import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros do circuito
R1 = 10e3       # 10 kΩ
C2 = 100e-9     # 100 nF
RC = R1 * C2

# Frequência do 1º harmônico
omega = 500 * np.pi    # rad/s
f = omega / (2 * np.pi)

# Entrada: primeiro harmônico da onda quadrada
t = np.linspace(0, 8 / f, 1000)
v_in = (4 / np.pi) * np.sin(omega * t)

# Sistema
num = [1]
den = [RC, 0]
sys = signal.TransferFunction(num, den)

# Resposta à entrada senoidal
t_out, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# Gráfico
plt.figure(figsize=(10, 4))
plt.plot(t, v_in, '--', color='gray', label=r'$v_{\mathrm{in}}^{(1)}(t)$')
plt.plot(t_out, v_out, 'b', lw=2, label=r'$v_{\mathrm{out}}^{(1)}(t)$')
plt.title('Resposta ao 1º Harmônico da Onda Quadrada - Circuito 5')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('Tensão (V)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()