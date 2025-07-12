import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Função de transferência H(s) = (12s + 104)/(s + 4)
num = [12, 104]
den = [1, 4]
system = signal.TransferFunction(num, den)

# Geração da rampa unitária
t = np.linspace(0, 2, 1000)           # 0-2 s
u = t                                 # rampa: u(t)=t

# Simulação da resposta com lsim
tout, y, _ = signal.lsim(system, U=u, T=t)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(tout, u, 'k--', label='Entrada r(t)=t')
plt.plot(tout, y,  label='Saída y(t)')
plt.title('Resposta à Rampa Unitária – Questão 2')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()