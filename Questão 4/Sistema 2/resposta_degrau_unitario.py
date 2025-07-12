import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# --- parâmetros -------------------------------------------------------------
betas = [0.001, 0.01, 0.1, 1, 10]
t     = np.linspace(0, 5, 2000)           # 0–5 s

plt.figure(figsize=(10, 6))
for beta in betas:
    num, den = [1, 1e4], [1, 2*beta, 100]
    sys      = signal.TransferFunction(num, den)
    tout, y  = signal.step(sys, T=t)
    plt.plot(tout, y, label=f'β = {beta}')

plt.title('Resposta ao Degrau Unitário — Sistema 2')
plt.xlabel('Tempo (s)')
plt.ylabel('y(t)')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()