import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros do circuito
R1 = 10e3        # 10 kΩ
C2 = 100e-9      # 100 nF
RC = R1 * C2

# Frequência fundamental
omega = 500 * np.pi
t = np.linspace(0, 8 / (omega / (2 * np.pi)), 2000)

# Entrada: 3 primeiros harmônicos (1, 3, 5)
v_in = (4 / np.pi) * (
    (1 / 1) * np.sin(1 * omega * t) +
    (1 / 3) * np.sin(3 * omega * t) +
    (1 / 5) * np.sin(5 * omega * t)
)

# Sistema integrador
num = [1]
den = [RC, 0]
sys = signal.TransferFunction(num, den)

# Resposta à soma dos harmônicos
t_out, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# Plotagem
plt.figure(figsize=(10, 4))
plt.plot(t, v_in, '--', color='gray', label=r'$v_{\mathrm{in}}^{(3)}(t)$')
plt.plot(t_out, v_out, 'b', lw=2, label=r'$v_{\mathrm{out}}^{(3)}(t)$')
plt.title('Resposta aos 3 Primeiros Harmônicos da Onda Quadrada – Circuito 5')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('Tensão (V)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()