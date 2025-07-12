from scipy import signal
import matplotlib.pyplot as plt

# Componentes
R1 = R2 = 10e3
C1 = 100e-9
C2 = 15e-9

# Parâmetros do sistema
K = C1 / (C2 * R1 * R2)
omega_0 = (1/R1 + 1/R2) / C2

# Função de transferência: H(s) = K / (s + omega_0)
num = [K]
den = [1, omega_0]
system = signal.TransferFunction(num, den)

# Resposta ao degrau
t, y = signal.step(system)

# Gráfico
plt.figure(figsize=(8, 4))
plt.plot(t, y)
plt.title('Resposta ao Degrau Unitário – Circuito 3')
plt.xlabel('Tempo [s]')
plt.ylabel('Saída $v_{out}(t)$')
plt.grid(True)
plt.tight_layout()
plt.show()