import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros do circuito
R1 = 1e3
R2 = 1e3
C1 = 100e-9
L1 = 0.253

# Função de transferência do sistema
num = [R1 / L1, 0]
den = [1, (R1 + R2) / L1, 1 / (L1 * C1)]
sys = signal.TransferFunction(num, den)

# Parâmetros da onda
f = 1e3                  # Frequência da dente de serra (Hz)
omega = 2 * np.pi * f
t = np.linspace(0, 0.01, 1000)
i_in = signal.sawtooth(omega * t, width=1.0)

# Resposta do sistema
t_out, i_out, _ = signal.lsim(sys, U=i_in, T=t)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, i_in, label=r'$i_{in}(t)$ (dente de serra)', linestyle='--', color='gray')
plt.plot(t_out, i_out, label=r'$i_{out}(t)$', linewidth=2)
plt.title('Resposta à Onda Dente de Serra – Circuito 2')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('$i_{out}(t)$ (A)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()