import control as ctl
import matplotlib.pyplot as plt
import numpy as np

"""Primeira Função"""
P_s = ctl.tf([3.,1.], [1.,3.,1.])
print('FT= ', P_s)

ps_ma = ctl.poles(P_s)
zs_ma = ctl.zeros(P_s)

print(f'Polos = {ps_ma}')
print(f'Zeros = {zs_ma}')

plt.figure()
PZ = ctl.pzmap(P_s, 1,1, 'Diagrama pz de P_s')

plt.show()


# """Segunda Função"""
# P_s = ctl.tf([1.,2.], [1.,1.])
# R_s = ctl.tf([1.], [1.,0.])
# C_s = R_s * P_s
# print(f'FT = {C_s}')

# ps_ma = ctl.poles(C_s)
# zs_ma = ctl.zeros(C_s)

# print(f'Polos = {ps_ma}')
# print(f'Zeros = {zs_ma}')
# # plt.figure()
# # PZ = ctl.pzmap(C_s, 1,1, 'Diagrama pz de C_s')
# # plt.show()

# """Calculo degrau unitário"""
# Tsim = 10
# quais_T = np.linspace(-1., Tsim, 1000)
# T_mf, yout_mf = ctl.step_response(P_s, quais_T[quais_T > 0])

# degrau = np.ones_like(quais_T)
# degrau[quais_T < 0] = 0

# plt.figure()
# plt.plot(T_mf, yout_mf, 'k-')
# plt.plot(quais_T, degrau, 'r-')
# plt.xlabel('tempos(s)')
# plt.legend(['resposta ao degrau', 'degrau unitário'])
# plt.grid();
# plt.title('Sistema de 2 Ordem')

# plt.show()