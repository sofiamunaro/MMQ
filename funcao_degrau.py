import numpy as np
import matplotlib.pyplot as plt

# Definindo o intervalo de x de 0 a 2pi
x = np.linspace(0, 2*np.pi, 500)

# Definindo a função f(x)
f = np.where((x >= 0) & (x <= np.pi), 1, -1)

# Plotando
plt.plot(x, f, label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axvline(np.pi, color='gray', linestyle='--', label='x = π')
plt.ylim(-1.5, 1.5)
plt.legend()
plt.grid(False)
plt.show()
