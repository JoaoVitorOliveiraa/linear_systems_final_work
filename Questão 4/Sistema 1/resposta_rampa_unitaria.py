import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Valores de α
alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]

# Denominador fixo (s² + 2s + 2)
den = [1, 2, 2]

# Vetor de tempo
t = np.linspace(0, 20, 2000)          # 0–20 s
u = t                                 # rampa unitária

plt.figure(figsize=(8, 5))

for alpha in alphas:
    sys = signal.TransferFunction([alpha, 1], den)   # H(s) = (αs + 1)/(s²+2s+2)
    tout, y_out, _ = signal.lsim(sys, U=u, T=t)      # resposta à rampa
    plt.plot(tout, y_out, label=f'α = {alpha}')

plt.title('Resposta à Rampa Unitária – Sistema 1 (Todos os α)')
plt.xlabel('Tempo [s]')
plt.ylabel('y(t)')
plt.grid(True, ls=':')
plt.legend(title='Valores de α', fontsize='small', ncol=2)
plt.tight_layout()
plt.show()