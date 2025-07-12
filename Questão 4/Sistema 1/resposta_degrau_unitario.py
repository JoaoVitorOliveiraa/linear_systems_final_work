import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Valores de α dados no enunciado
alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]

# Denominador fixo
den = [1, 2, 2]

# Geração da grade de tempo
t = np.linspace(0, 10, 1000)

# Figura
plt.figure(figsize=(8, 5))

# Laço para plotar cada resposta
for alpha in alphas:
    num = [alpha, 1]                   # numerador: 1 + αs
    sys = signal.TransferFunction(num, den)  # sistema LTI
    t_out, y_out = signal.step(sys, T=t)     # resposta ao degrau
    plt.plot(t_out, y_out, label=f'α = {alpha}')

# Configurações do gráfico
plt.title('Resposta ao Degrau Unitário – Sistema 1 (Todos os α)')
plt.xlabel('Tempo [s]')
plt.ylabel('Saída y(t)')
plt.grid(True, which='both', ls=':')
plt.legend(title='Valores de α', fontsize='small', ncol=2)
plt.tight_layout()
plt.show()