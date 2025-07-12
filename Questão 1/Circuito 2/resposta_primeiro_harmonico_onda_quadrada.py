import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros do circuito
R1 = 1e3
R2 = 1e3
C1 = 100e-9
L1 = 0.253

# Função de transferência
num = [R1 / L1, 0]
den = [1, (R1 + R2) / L1, 1 / (L1 * C1)]
sys = signal.TransferFunction(num, den)

# 1º harmônico
f = 1e3
omega = 2 * np.pi * f
t = np.linspace(0, 0.01, 1000)
i_in_1 = (4 / np.pi) * np.sin(omega * t)

# Resposta à senoide
t_out, i_out_1, _ = signal.lsim(sys, U=i_in_1, T=t)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, i_in_1, label=r'$i_{in}^{(1)}(t)$', linestyle='--', color='gray')
plt.plot(t_out, i_out_1, label=r'$i_{out}^{(1)}(t)$', linewidth=2)
plt.title('Resposta ao 1º Harmônico da Série de Fourier de uma Onda Quadrada– Circuito 2')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('$i_{out}(t)$ (A)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()