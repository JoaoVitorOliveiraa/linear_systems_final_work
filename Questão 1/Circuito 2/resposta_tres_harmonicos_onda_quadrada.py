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

# Parâmetros do sinal
f = 1e3
omega = 2 * np.pi * f
t = np.linspace(0, 0.01, 1000)

# Entrada com 3 primeiros harmônicos
i_in = (4 / np.pi) * (
    np.sin(omega * t) +
    (1/3) * np.sin(3 * omega * t) +
    (1/5) * np.sin(5 * omega * t)
)

# Resposta à entrada
t_out, i_out, _ = signal.lsim(sys, U=i_in, T=t)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, i_in, label=r'$i_{in}(t)$ (3 harmônicos)', linestyle='--', color='gray')
plt.plot(t_out, i_out, label=r'$i_{out}(t)$', linewidth=2)
plt.title('Resposta aos 3 Primeiros Harmônicos da Série de Fourier de uma Onda Quadrada – Circuito 2')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('$i_{out}(t)$ (A)')
plt.grid(True, linestyle=':')
plt.legend(loc='lower left', bbox_to_anchor=(0, 0.05), frameon=True, framealpha=0.9)
plt.tight_layout()
plt.show()