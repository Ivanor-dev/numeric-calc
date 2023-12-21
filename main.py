import matplotlib.pyplot as plt

x_value = 3  # Valor de x para o ponto (x, 0)
y_value = 5  # Valor de y para o ponto (0, y)

# Plotagem das linhas
plt.plot([x_value, x_value], [0, y_value], 'r--')  # Linha vertical pelo ponto (x, 0)
plt.plot([0, x_value], [y_value, y_value], 'b--')  # Linha horizontal pelo ponto (0, y)

# Adição de rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Mostrar o gráfico
plt.show()