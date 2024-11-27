import control as ctl
import matplotlib.pyplot as plt
import numpy as np

a = 2
Tsim = 10

# Função de transferência MA
s = ctl.TransferFunction.s
G_s = 1 / (s + a) # ALTERAR A FUNÇÃO AQUI 
print('MA: G_s = ', G_s)

# Diagrama de Nyquist
plt.figure(1)
ny = ctl.nyquist(G_s)

# Alguns pontos interessantes para ilustrar
f_lim = 1 / (a + 1j * np.array([0, a, -a, 1000 * a, -1000 * a]))
plt.plot(f_lim.real, f_lim.imag, 'mx')

# Mapa de polos e zeros em malha aberta
plt.figure(2)
ctl.pzmap(G_s, 1, 0, 'mapa pz em malha aberta')

# Calcula a FT em malha fechada
H_s = 1
G1_s = ctl.minreal(G_s / (1 + G_s * H_s))
print('MF: G1_s = ', G1_s)

# Mapa de polos e zeros em malha fechada
plt.figure(3)
ctl.pzmap(G1_s, 1, 0, 'mapa pz em malha fechada')

# Resposta ao degrau em malha fechada
T, yout = ctl.step_response(G1_s, Tsim)
plt.figure(4)
plt.plot(T, yout, 'b-')
plt.xlabel('tempo (s)')
plt.grid()
plt.legend(['resposta ao degrau'])

plt.show()
