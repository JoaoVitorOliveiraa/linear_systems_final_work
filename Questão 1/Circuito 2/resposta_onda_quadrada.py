import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros do circuito
R1 = 1e3         # 1 kΩ
R2 = 1e3         # 1 kΩ
C1 = 100e-9      # 100 nF
L1 = 0.253       # 253 mH

# Frequência fundamental (central do filtro)
f = 1e3          # 1 kHz
omega = 2 * np.pi * f

# Função de transferência do circuito
num = [R1 / L1, 0]
den = [1, (R1 + R2) / L1, 1 / (L1 * C1)]
sys = signal.TransferFunction(num, den)

# Sinal de entrada: onda quadrada com frequência ω
t = np.linspace(0, 0.01, 1000)
i_in = signal.square(omega * t)

# Resposta do sistema
t_out, i_out, _ = signal.lsim(sys, U=i_in, T=t)

# Plot da entrada e da saída
plt.figure(figsize=(10, 4))
plt.plot(t, i_in, label=r'$i_{in}(t)$ (onda quadrada)', linestyle='--', color='gray')
plt.plot(t_out, i_out, label=r'$i_{out}(t)$', linewidth=2)
plt.title('Resposta à Onda Quadrada – Circuito 2')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('$i_{out}(t)$ (A)')
plt.grid(True, linestyle=':')
plt.legend(loc='lower left', bbox_to_anchor=(0, 0.05), frameon=True, framealpha=0.9)
plt.tight_layout()
plt.show()