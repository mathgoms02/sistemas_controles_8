from tbcontrol.symbolic import routh
import sympy

s = sympy.Symbol('s')

#FTMalha aberta
C_s = 1
P_s = 1000/((s+2)*(s+3)*(s+5))
G_s = sympy.expand(C_s*P_s)
print("Malha aberta G(s)={}".format(G_s))

# FT malha fechada
H_s = 1
G1_s = sympy.cancel((G_s)/(1+G_s*H_s))
print("Malha fechada G1(s)={}".format(G1_s))
num_G1_s, den_G1_s = sympy.fraction(G1_s)
print('\n Tabela de Routh:')
routh(sympy.poly(den_G1_s, s)) #Não ta mostrando, rodei no Collab pra ver a matriz 