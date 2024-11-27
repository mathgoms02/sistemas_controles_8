import control as ctl
import matplotlib.pyplot as plt
import numpy as np

# Para definir um sistema linear em python, usamos o comando "control.tf"
h = ctl.tf([2.,1.], [1.,4.,-3.])
print(h)

########
r = 0.5 #Resistência
c = 1. #Capacitância
Tsim = 10 #Tempo de simulação

numerador = [1.]
denominador = [r*c,1.]

h = ctl.tf(numerador, denominador)
print(f'FT de malha aberta = {h}')

t, yout = ctl.step_response(h, Tsim)

plt.plot(t,yout, 'b-')
# plt.show()

########

t2 = np.linspace(-1.,10.,1000)
degrau = np.ones_like(t2)
degrau[t2<0]=0
plt.plot(t2, degrau, 'r-')

####################

plt.ylabel('V(V)')
plt.xlabel('tempo (s)')
plt.legend(['Resposta ao degrau', 'degrau unitário'])
plt.grid()

plt.show()