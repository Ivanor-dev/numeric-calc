import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Criando dados para os eixos x, y, z (usando o numpy para gerar dados)
x = np.random.rand(100)  # valores aleatórios para x
y = np.random.rand(100)  # valores aleatórios para y
z = np.random.rand(100)  # valores aleatórios para z

# Criando a figura e o eixo 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Gráfico de dispersão 3D
ax.scatter(x, y, z)

# Adicionando rótulos
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

# Mostrando o gráfico 3D
plt.show()