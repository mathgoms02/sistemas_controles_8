import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

num = [1]
den = [1, 1]

system = ctrl.TransferFunction(num, den)

t = np.linspace(0, 10, 1000)
t, y = ctrl.step_response(system, T=t)

plt.figure(figsize=(10, 5))
plt.plot(t, y)
plt.title('Degrau Unitário do Sistema')
plt.xlabel('T(s)')
plt.ylabel('V(V)')
plt.grid()
plt.xlim(0, 10)
plt.ylim(0, 1.2)
plt.axhline(y=1, color='red', lw=1)
plt.show()