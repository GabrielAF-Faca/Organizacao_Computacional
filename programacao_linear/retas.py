import matplotlib.pyplot as plt

def get_retas_from_file(path):
    linhas = []
    retas = []
    with open(path, 'r') as file:
        for linha in file.readlines():
            linha = linha.replace(" ", "").replace("\n", "")
            linhas.append(linha)

    # for linha in linhas:
    #     r = []
    #     for i in linha:
    #         print(i)
    #         if i.isdigit():
    #             print("é")
    #             r.append(int(i))
    #     retas.append(r)
    return linhas

def get_intersecao(reta1, reta2):

    a1, b1, c1 = reta1
    a2, b2, c2 = reta2

    if a1 * b2 == a2 * b1:
        print("São paralelas")
        return None

    x = round(-(c2 * b1 - c1 * b2) / (a1 * b2 - a2 * b1), 3)
    y = round((a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1), 3)

    return x, y


retas = get_retas_from_file("retas")

print(retas)

i = 0
x = 0
y = 0

# pointsX = []
# pointsY = []
#
# for reta in retas:
#     for i in retas:
#         if i != reta:
#             x, y = get_intersecao(reta, i)
#             pointsX.append(x)
#             pointsY.append(y)
#             print(x, y)
