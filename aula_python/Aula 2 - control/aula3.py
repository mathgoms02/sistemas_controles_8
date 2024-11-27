import control as ctl
import matplotlib.pyplot as plt
import numpy as np

R = 20.0e3
C = 10.0e-6
tau = R*C
Tsim = 1

numerador = [1]
denominador = [1.,1/tau]
P_s = ctl.tf(numerador, denominador)

print(f'FT em malha aberta = {P_s}')

################################################################################

C_s = ctl.tf([3.], [1.])
print(f'FT do controlar = {C_s}')

################################################################################

H_s = ctl.tf([1.],[1.])
G_s = ctl.series(C_s, P_s)
G1_s = ctl.feedback(G_s, H_s, sign = -1)
print(f'FT em malha fechada = {G1_s} ')

################################################################################

T_mf, yout_mf = ctl.step_response(G1_s, Tsim) # Calcula a resposta 

T2 = np.linspace(-0.2, Tsim, 1000)
degrau = np.ones_like(T2)
degrau[T2 < 0] = 0

################################################################################

plt.plot(T_mf, yout_mf, 'b-')
plt.plot(T2, degrau, 'r-')
plt.ylabel('V(V)')
plt.xlabel('Tempo(s)')
plt.legend(['Resposta ao degrau', 'Degrau unitário'])
plt.title('Circuito RC em malha fechada')
plt.grid()
plt.show()