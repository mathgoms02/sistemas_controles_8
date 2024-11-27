import control as ctl
import matplotlib.pyplot as plt
import numpy as np

R=10e3
C=20e-6

#cria funçaõ de tanferencia
s = ctl.TransferFunction.s
G_s = (1)/(R*C*s +1)
print('G_s', G_s)

#Diagrama de bode
Ws=np.logspace(-3,3,1000)
plt.figure(1)
ctl.bode_plot(G_s,Ws,dB=True, wrap_phase=True)
plt.xlabel('w(rad/s)')

plt.show()