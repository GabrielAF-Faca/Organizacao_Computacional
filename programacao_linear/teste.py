from scipy.optimize import linprog

import matplotlib.pyplot as plt
import inequacoes as ineq
import numpy as np
import files as f

resolution = 1000

restricoes, objetivo = f.get_restricoes_from_file("./retas_backup")

coefs, limites, bound = ineq.get_coefs(restricoes)
obj = ineq.get_objetivo(objetivo)

resultado = linprog(obj,
                    A_ub=coefs,
                    b_ub=limites,
                    method='simplex',
                    bounds=bound
                    )

if resultado.success:
    x_o, y_o = resultado.x

    plt.plot(x_o, y_o, 'ro')

    plt.text(x_o, y_o + 0.5, '({}, {})'.format(round(x_o, 3), round(y_o, 3)))
    print("({}, {})".format(round(x_o, 3), round(y_o, 3)))
    print("Z =", abs((obj[0] * x_o) + (obj[1] * y_o)))

else:
    print("Solução não encontrada")

limX = 0
limY = 0

index = 0

for coef in coefs:
    raiz_x = limites[index]/coef[0]
    raiz_y = limites[index]/coef[1]

    if raiz_x > limX:
        limX = raiz_x

    if raiz_y > limY:
        limY = raiz_y

    index += 1

xx = np.linspace(0, limX, resolution)
yy = np.linspace(0, limY, resolution)

x, y = np.meshgrid(xx, yy)

c = []

for res in restricoes:
    c.append(eval(res.rstrip().lstrip()))

plt.imshow(
    np.bitwise_and.reduce(c),
    extent=(x.min(), x.max(), y.min(), y.max()),
    origin="lower",
    cmap="Reds",
    alpha=0.2
)

x = np.linspace(0, limX, resolution)

retas, assintotas, linhas = ineq.get_equacoes(restricoes)

index = 97

for reta in retas:
    plt.plot(x, eval(reta), label="(" + chr(index) + ") : " + linhas[0][index % 97].replace("*", ''))
    index += 1

plt.ylim(bottom=0, top=limY+1)
plt.xlim(left=0, right=limX+1)

plt.plot(x, x*0, color='r')
plt.axvline(0, color='r')

index_ass = 0

for reta in assintotas:
    plt.axvline(reta, color='r', label="(" + chr(index) + ") : " + linhas[1][index_ass])
    index += 1
    index_ass += 1


plt.legend(loc='upper right', bbox_to_anchor=(1, 1), fancybox=True, shadow=True)
plt.grid()

plt.show()
