import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# --- Sistema ----------------------------------------------------------
num = [12, 104]           # numerador  (12s + 104)
den = [1, 4]              # denominador (s + 4)
system = signal.TransferFunction(num, den)

# --- Parâmetros da dente-de-serra -------------------------------------
omega = 4                 # rad/s  (frequência fundamental)
T = 2 * np.pi / omega
t = np.linspace(0, 2*T, 5000)          # duas épocas para visualizar

# --- Acumulação dos 5 primeiros harmônicos ----------------------------
u_sum = np.zeros_like(t)
y_sum = np.zeros_like(t)

plt.figure(figsize=(10, 6))
for n in [1, 2, 3, 4, 5]:
    coef = (2 / np.pi) * ((-1)**(n + 1)) / n   # coeficiente da série
    u_n = coef * np.sin(n * omega * t)         # entrada harmônica
    _, y_n, _ = signal.lsim(system, U=u_n, T=t)  # saída filtrada
    u_sum += u_n
    y_sum += y_n
    plt.plot(t, y_n, lw=1, label=fr'$y_{n}(t)$')

# --- Soma total --------------------------------------------------------
plt.plot(t, y_sum, 'k', lw=2, label='Soma $y(t)$')
plt.title('Resposta aos 5 Primeiros Harmônicos da Dente-de-Serra - Questão 2')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()
