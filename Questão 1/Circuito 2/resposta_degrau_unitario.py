from scipy import signal
import matplotlib.pyplot as plt

# Valores comerciais
R1 = 1e3          # 1 kΩ
R2 = 1e3          # 1 kΩ
C1 = 100e-9       # 100 nF
L1 = 0.253        # 253 mH

# Função de transferência H(s)
num = [R1 / L1, 0]
den = [1, (R1 + R2) / L1, 1 / (L1 * C1)]
sys = signal.TransferFunction(num, den)

# Resposta ao degrau unitário (Iin = 1·u(t))
t, i_out = signal.step(sys)

# Plot
plt.figure(figsize=(8, 4))
plt.plot(t, i_out, linewidth=2, color='orange')
plt.title('Resposta ao Degrau Unitário – Circuito 2')
plt.xlabel('Tempo $t$ (s)')
plt.ylabel('$i_{out}(t)$ (A)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()