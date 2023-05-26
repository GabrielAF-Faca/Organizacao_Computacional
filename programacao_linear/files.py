

def get_restricoes_from_file(path):

    restricoes = []
    objetivo = ""

    with open(path, 'r') as file:
        linhas = file.readlines()

    for linha in linhas:

        linha = linha.replace('\n', '').replace(' ', '').lower()

        if "max" in linha or "min" in linha:
            objetivo = linha
            continue

        x_pos = linha.find("x")

        if x_pos > 0:
            if linha[x_pos-1].isdigit():
                linha = linha[:x_pos] + "*" + linha[x_pos:]

        y_pos = linha.find("y")

        if y_pos > 0:
            if linha[y_pos-1].isdigit():
                linha = linha[:y_pos] + "*" + linha[y_pos:]

        restricoes.append(linha)

    if len(objetivo):
        return restricoes, objetivo

    return restricoes, None

