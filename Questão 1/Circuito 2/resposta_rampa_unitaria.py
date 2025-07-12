import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros do circuito
R1 = 1e3          # 1 kΩ
R2 = 1e3          # 1 kΩ
C1 = 100e-9       # 100 nF
L1 = 0.253        # 253 mH

# Função de transferência
num = [R1 / L1, 0]
den = [1, (R1 + R2) / L1, 1 / (L1 * C1)]
sys = signal.TransferFunction(num, den)

# Sinal de entrada: rampa unitária (i_in(t) = t·u(t))
t = np.linspace(0, 0.01, 1000)
i_in = t  # Rampa unitária

# Resposta ao sinal arbitrário
t_out, i_out, _ = signal.lsim(sys, U=i_in, T=t)

# Plot
plt.figure(figsize=(8, 4))
plt.plot(t_out, i_out, label=r'$i_{out}(t)$', color='green', linewidth=2)
plt.title('Resposta à Rampa Unitária – Circuito 2')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('$i_{out}(t)$ (A)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()