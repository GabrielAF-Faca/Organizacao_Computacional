

def get_equacoes(ineq):

    sem_y = []
    com_y = []

    linhas = {0: [],
              1: []}

    for element in ineq:

        if 'y' not in element:
            linhas[1].append(element)

            sem_y.append(float(element.split('=')[1]))

        else:
            linhas[0].append(element)
            element = element.replace("<", '').replace('>', '')

            if 'x' not in element:
                element = element.split("=")[1]
                com_y.append("0*x + "+element)

            else:
                element = element.split("=")
                le = element[0]
                ld = element[1]

                index = 0

                value = ""
                values = []

                for char in le:
                    value += char
                    if index > 0:
                        if char == '-' or char == '+' or index == len(le)-1:
                            values.append(value[:-1])
                            value = char

                    index += 1

                if values[0][0] == "-":
                    ld += "+"+values[0][1:]
                else:
                    ld += "-"+values[0]

                if len(values[1]) < 2:
                    values[1] += "1"

                if '*' in values[1]:
                    values[1] = values[1][:-1]

                ld = "("+ld+")/"+values[1]

                com_y.append(ld)

    return com_y, sem_y, linhas


def get_coefs(ineq):

    coeficientes = []
    limites = []

    bounds = []

    for element in ineq:

        if not 'y' in element or not 'x' in element:
            bounds.append(element)
            continue

        if "<" in element:
            op = "<"
        elif ">" in element:
            op = ">"

        element = element.replace("<", "").replace(">", "").replace("*", "").split("=")

        if op == ">":
            element[1] = "-" + element[1]

        limites.append(float(element[1]))

        coef = ""
        coefs = []
        operators = ["-", "+"]

        for char in element[0]:
            if char.isdigit() or char in operators:
                coef += char
            else:
                coefs.append(coef)
                coef = ""

        for i in range(len(coefs)):
            c = coefs[i]
            if not c.isdigit() and len(c) < 2:
                coefs[i] += "1"

        coefs = [float(i) for i in coefs]

        if op == ">":
            coefs = [-i for i in coefs]

        coeficientes.append(coefs)

    bounds_x = []
    bounds_y = []

    for bound in bounds:
        if not 'x' in bound:
            bounds_y.append(float(bound.split("=")[1]))

        elif not 'y' in bound:
            bounds_x.append(float(bound.split("=")[1]))

    if len(bounds_x) < 2:
        bounds_x.append(None)
    else:
        bounds_x = sorted(bounds_x)

    if len(bounds_y) < 2:
        bounds_y.append(None)
    else:
        bounds_y = sorted(bounds_y)

    bb = (tuple(bounds_x), tuple(bounds_y))

    return coeficientes, limites, bb


def get_objetivo(objetivo):

    operation = "min" if "min" in objetivo else "max"

    function = objetivo.replace(operation, "")

    coef = ""
    coefs = []
    operators = ["-", "+"]

    for char in function:
        if char.isdigit() or char in operators:
            coef += char
        else:
            coefs.append(coef)
            coef = ""

    for i in range(len(coefs)):
        c = coefs[i]
        if not c.isdigit() and len(c) < 2:
            coefs[i] += "1"

    coefs = [float(i) for i in coefs]

    if operation == "max":
        return [-i for i in coefs]

    return coefs
