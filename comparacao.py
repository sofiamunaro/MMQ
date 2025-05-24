import numpy as np
import matplotlib.pyplot as plt

#função degrau
x = np.linspace(0, 2*np.pi, 1000)
f = np.where((x >= 0) & (x <= np.pi), 1, -1)

#função aproximação
m = 30 #inserir 'grau' do polinomio
n = 2*m + 1
diagonal = np.full(n, np.pi)
diagonal[0] = 2 * np.pi
matriz = np.diag(diagonal)
print(matriz)
coeficientes = [0]
for i in range(1,m+1):
    coeficientes.append(0)
    coeficientes.append((2*(1-(-1)**i))/i)
vetor_gama = np.linalg.solve(matriz, coeficientes)
x = np.linspace(0, 2*np.pi, 1000)
F = np.full_like(x, vetor_gama[0])
for n in range(1, m+1):
    a_n = vetor_gama[2*n - 1]
    b_n = vetor_gama[2*n]
    F += a_n * np.cos(n * x) + b_n * np.sin(n * x)

#Plotando
plt.plot(x, f, label='f(x)')
plt.plot(x, F, label=f'F(x) com {m} graus')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
