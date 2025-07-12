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

# Frequência fundamental
f = 1e3
omega = 2 * np.pi * f
t = np.linspace(0, 0.01, 1000)

# Entrada: 5 primeiros harmônicos da dente de serra
i_in = (2 / np.pi) * (
    np.sin(1 * omega * t) -
    (1/2) * np.sin(2 * omega * t) +
    (1/3) * np.sin(3 * omega * t) -
    (1/4) * np.sin(4 * omega * t) +
    (1/5) * np.sin(5 * omega * t)
)

# Resposta do sistema
t_out, i_out, _ = signal.lsim(sys, U=i_in, T=t)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, i_in, label=r'$i_{in}^{(5)}(t)$ (5 harmônicos)', linestyle='--', color='gray')
plt.plot(t_out, i_out, label=r'$i_{out}(t)$', linewidth=2)
plt.title('Resposta aos 5 Primeiros Harmônicos da Dente de Serra – Circuito 2')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('$i_{out}(t)$ (A)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()