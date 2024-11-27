import numpy as np
import matplotlib.pyplot as plt

# Definindo polos e zeros
zeros = [-0.4]
polos = [-0.395, -50.605]

plt.figure(figsize=(8, 6))

# Plotando os polos
for polo in polos:
    plt.plot(np.real(polo), np.imag(polo), 'x', markersize=10, label='polo')

# Plotando os zeros
for zero in zeros:
    plt.plot(np.real(zero), np.imag(zero), 'o', markersize=10, label='zero')

# Configurações do gráfico
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.xlim(-60, 1)
plt.ylim(-3, 3)
plt.title('Diagrama polos e zeros')
plt.ylabel('Im(s)')
plt.xlabel('Re(s)')
plt.grid()
plt.legend()

# Exibindo o gráfico
plt.show()