from tbcontrol.symbolic import routh
import sympy

s = sympy.Symbol('s')
K = sympy.Symbol('K')

#FTMalha aberta
C_s = K
P_s = (s+20)/(s*(s+2)*(s+3))
G_s = (C_s*P_s)
print("Malha aberta G(s)={}".format(G_s))

# FT malha fechada
H_s = 1
G1_s = sympy.cancel((G_s)/(1+G_s*H_s))
print("Malha fechada G1(s)={}".format(G1_s))
num_G1_s, den_G1_s = sympy.fraction(G1_s)
print('\n Tabela de Routh:')

num_G1_s, den_G1_s = sympy.fraction(G1_s)
tab_routh = routh(sympy.poly(den_G1_s,s))
k_estab = sympy.solve([e > 0 for e in tab_routh[:,0]],K)
sympy.pprint("\nSistema estável se: {}".format(k_estab))
print("\nTabela de Routh:")
routh(sympy.poly(den_G1_s,s)) #Não ta mostrando, rodei no Collab pra ver a matriz 