import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros do circuito
R1 = 10e3       # 10 kΩ
C = 100e-9      # 100 nF
RC = R1 * C

# Frequência fundamental
omega = 500 * np.pi
f = omega / (2 * np.pi)
t = np.linspace(0, 4 / f, 2000)

# Construção da entrada com os 5 primeiros harmônicos
v_in = -(1 / np.pi) * sum(
    (1 / n) * np.sin(n * omega * t) for n in range(1, 6)
)

# Sistema integrador
num = [1]
den = [RC, 0]
sys = signal.TransferFunction(num, den)

# Resposta do sistema
t_out, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# Plotagem
plt.figure(figsize=(10, 4))
plt.plot(t, v_in, '--', color='gray', lw=1.3, label=r'$v_{\mathrm{in}}^{(5)}(t)$')
plt.plot(t_out, v_out, 'tab:blue', lw=2, label=r'$v_{\mathrm{out}}^{(5)}(t)$')
plt.title('Resposta aos 5 Primeiros Harmônicos da Onda Dente de Serra - Circuito 5')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('Tensão (V)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()