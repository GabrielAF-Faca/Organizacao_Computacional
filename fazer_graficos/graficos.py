import matplotlib.pyplot as plt
import random

from funcoes import *


# Definir os pontos da reta (aleatórios)
x1 = [random.uniform(-5, 5), random.uniform(-5, 5)]
y1 = [random.uniform(-5, 5), random.uniform(-5, 5)]


# Gerar as equações
equation1 = Reta(x1[0], y1[0], x1[1], y1[1]).get_equacao()

# Plotar a reta no gráfico
plt.plot(x1, y1, 'r', label=f'Reta 1: {equation1}')
plt.legend(loc='best')



plt.show()
