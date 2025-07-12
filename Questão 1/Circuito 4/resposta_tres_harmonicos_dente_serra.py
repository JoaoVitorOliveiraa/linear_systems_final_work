import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parâmetros
f = 100      # Hz
omega = 2 * np.pi * f
T = 1 / f
t = np.linspace(0, 4 * T, 2000)

# Harmônicos n = 1, 2, 3
harmonics = [1, 2, 3]
v_in = np.zeros_like(t)

for n in harmonics:
    v_in += -(2 / (np.pi * n)) * np.sin(n * omega * t)

# Saída do seguidor de tensão
v_out = v_in

# Gráfico
plt.figure(figsize=(10, 4))
plt.plot(t, v_in, label='v_in(t): soma 3 harmônicos', linewidth=2, color='black')
plt.plot(t, v_out, '--', label='v_out(t)', linewidth=1.5, color='red')

# Componentes individuais (opcional)
for n in harmonics:
    plt.plot(t, -(2 / (np.pi * n)) * np.sin(n * omega * t),
             alpha=0.35, label=f'{n}º harmônico (n={n})')

plt.title('Resposta aos 3 Primeiros Harmônicos da Dente de Serra – Circuito 4')
plt.xlabel('Tempo t (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(loc='upper right', ncol=2)
plt.tight_layout()
plt.show()