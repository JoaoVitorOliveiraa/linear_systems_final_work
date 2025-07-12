import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros
R1 = 10e3        # 10 kΩ
C2 = 100e-9      # 100 nF
T = 4e-3         # Período da onda quadrada (4 ms)
f = 1 / T        # Frequência em Hz

# Sistema integrador
num = [1]
den = [R1 * C2, 0]
sys = signal.TransferFunction(num, den)

# Tempo de simulação
t = np.linspace(0, 8*T, 2000)  # 8 ciclos

# Entrada: onda quadrada de amplitude 1
v_in = signal.square(2 * np.pi * f * t)

# Resposta do sistema
t_out, v_out, _ = signal.lsim(sys, U=v_in, T=t)

# Plotagem
plt.figure(figsize=(10, 4))
plt.plot(t, v_in, 'gray', lw=1.5, label=r'$v_{\mathrm{in}}(t)$ (Quadrada)')
plt.plot(t_out, v_out, 'b', lw=2, label=r'$v_{\mathrm{out}}(t)$ (Triangular)')
plt.title('Resposta à Onda Quadrada – Circuito 5')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('Tensão (V)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()