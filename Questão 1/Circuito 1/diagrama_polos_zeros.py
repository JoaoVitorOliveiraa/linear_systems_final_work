import matplotlib.pyplot as plt

# zeros e pólos
zeros = [0]
poles = [-5.01, -1994.99]

fig, ax = plt.subplots(figsize=(6, 4))

# eixos Re{s} e Im{s}
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# plotagem
ax.plot(zeros, [0]*len(zeros), 'o', markersize=10, label='Zeros')
ax.plot(poles, [0]*len(poles), 'x', markersize=10, label='Pólos')

# ajustes de gráfico
ax.set_title('Diagrama de Pólos e Zeros – Circuito 1')
ax.set_xlabel('Re{s}')
ax.set_ylabel('Im{s}')
ax.set_xlim(-2100, 100)
ax.set_ylim(-100, 100)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', linewidth=0.5)
ax.legend()

plt.tight_layout()
plt.show()