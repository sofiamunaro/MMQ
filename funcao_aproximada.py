import numpy as np
import matplotlib.pyplot as plt

m = 5 #grau do polinomio de aproximacao
n = 2*m + 1  # tamanho da matriz 

# Cria um array cheio de pi
diagonal = np.full(n, np.pi)
# Muda o primeiro elemento para 2*pi
diagonal[0] = 2 * np.pi
# Cria a matriz diagonal com esses valores
matriz = np.diag(diagonal)
print(matriz)
# Cria o vetor coeficientes
coeficientes = [0] #valor calculado para (f,1)
for i in range(1,m+1):
    coeficientes.append(0) #valor calculado para (f,cos(mx))
    coeficientes.append((2*(1-(-1)**i))/i) #valor calculado para (f,sen(mx))
print(coeficientes)

vetor_gama = np.linalg.solve(matriz, coeficientes)
print(vetor_gama)
    
# Cria pontos x entre 0 e 2pi
x = np.linspace(0, 2*np.pi, 1000)

# Começa com F(x) = a0
F = np.full_like(x, vetor_gama[0])

for n in range(1, m+1):
    a_n = vetor_gama[2*n - 1]
    b_n = vetor_gama[2*n]
    F += a_n * np.cos(n * x) + b_n * np.sin(n * x)

# Plotagem
plt.plot(x, F, label=f'Aproximação com {m} graus')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True)
plt.legend()
plt.show()