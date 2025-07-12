import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# --- parâmetros do circuito ---
R = 10e3            # 10 kΩ
C = 15e-9           # 15 nF
num = [1/(R*C)]
den = [1, 3/(R*C), 1/(R**2*C**2)]
sys = signal.TransferFunction(num, den)

# --- frequência fundamental da dente-de-serra ---
f0 = 1/(2*np.pi*R*C)      # ≈ 1061 Hz
w0 = 2*np.pi*f0
T  = 1/f0
fs = 2e5                  # 200 kSa/s
t  = np.arange(0, 4*T, 1/fs)

# --- entrada: 3 primeiros harmônicos ---
x = -(2/np.pi)*(
       np.sin(1*w0*t)
     - 0.5*np.sin(2*w0*t)
     + (1/3)*np.sin(3*w0*t)
)

# --- resposta do sistema ---
t_out, y_out, _ = signal.lsim(sys, U=x, T=t)

# --- gráfico: entrada (V) e saída (µV) no mesmo eixo de tempo ---
fig, ax1 = plt.subplots(figsize=(10,5))

ax1.plot(t, x, 'C0', label='Entrada (V)')
ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Entrada (V)', color='C0')
ax1.tick_params(axis='y', labelcolor='C0')
ax1.grid(True, linestyle='--')

ax2 = ax1.twinx()
ax2.plot(t_out, y_out*1e6, 'C1', label='Saída (µV)')
ax2.set_ylabel('Saída (µV)', color='C1')
ax2.tick_params(axis='y', labelcolor='C1')

fig.suptitle('3 Primeiros Harmônicos da Dente-de-Serra – Circuito 6')
fig.tight_layout()
fig.legend()
plt.show()