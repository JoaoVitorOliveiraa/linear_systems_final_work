import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Função de transferência: H(s) = 1 / (s^2 + s + 1)
num = [1]
den = [1, 1, 1]
system = signal.TransferFunction(num, den)

# Frequência fundamental (escolha "sábia")
omega = 4           # rad/s
T = 2 * np.pi / omega
t = np.linspace(0, 2*T, 5000)          # duas épocas

# Gera o dente-de-serra (amplitude ±1, média zero)
u = signal.sawtooth(omega * t, width=0)   # width=0 ⇒ rampa cresce

# Calcula a saída do sistema
tout, y, _ = signal.lsim(system, U=u, T=t)

# Plota entrada e saída
plt.figure(figsize=(10, 5))
plt.plot(tout, u, 'k--', label='Entrada: dente-de-serra')
plt.plot(tout, y,  label='Saída: y(t)')
plt.title(r'Resposta ao Dente-de-Serra  ($\omega = 4\,$rad/s) - Questão 3')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()