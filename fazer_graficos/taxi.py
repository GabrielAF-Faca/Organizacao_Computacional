from funcoes import *
import matplotlib.pyplot as plt

#calcular o valor da corrida de um táxi

preco_inicial = float(input("Informe o valor mínimo da corrida: "))
preco_por_distancia = float(input("Informe o valor por km percorrido: "))
distancia = float(input("Informe a distância percorrida (km): "))

x1 = 0
y1 = preco_inicial

x2 = distancia
y2 = Func_afim(preco_por_distancia, x2, y1).calcular()

equacao = Reta(x1, y1, x2, y2).get_equacao()

print("O valor da corrida foi: {}".format(y2))

plt.plot([x1, y1], [x2, y2], 'r', label=f'Reta 1: {equacao}')
plt.legend(loc='best')


plt.show()

