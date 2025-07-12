import matplotlib.pyplot as plt

# Cria a figura e o eixo
fig, ax = plt.subplots(figsize=(4, 4))

# Desenha os eixos real e imaginário
ax.axhline(0, linewidth=1)  # eixo Im{s}
ax.axvline(0, linewidth=1)  # eixo Re{s}

# Mensagem explicativa
ax.text(0.05, 0.9,
        "Nenhum pólo ou zero finito",
        transform=ax.transAxes)

# Configurações estéticas
ax.set_title("Diagrama de Pólos e Zeros – Circuito 4")
ax.set_xlabel("Re{ s }")
ax.set_ylabel("Im{ s }")
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='--', linewidth=0.5)

# Exibe o gráfico
plt.show()