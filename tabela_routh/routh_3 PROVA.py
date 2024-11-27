import control as ctl
import matplotlib.pyplot as plt
import numpy as np

# Função de tranferencia Malha aberta
s = ctl.TransferFunction.s
G_s = ((s-1)*(s-2))/(s**2+4*s+8) # a função vai aqui
print('G_s = ', G_s) 

#LGR
plt.figure(1)
ctl.root_locus(G_s)
plt.ylim([-3,3])
plt.xlim([-3,3])

#EXTRA: máxima k para estabilidade
out_st_magn = ctl.stability_margins(G_s)
gain_margin = out_st_magn[0]
print('K máximo de estabilidade=',gain_margin) 

plt.show()