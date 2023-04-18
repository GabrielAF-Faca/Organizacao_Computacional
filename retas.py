

def get_reta():
    print("ax + b = c")

    return [
        int(input("Informe a: ")),
        int(input("Informe b: ")),
        int(input("Informe c: "))
    ]


def get_intersecao(reta1, reta2):

    a1, b1, c1 = reta1
    a2, b2, c2 = reta2

    if a1 * b2 == a2 * b1:
        print("São paralelas")
        return None

    x = round(-(c2 * b1 - c1 * b2) / (a1 * b2 - a2 * b1), 3)
    y = round((a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1), 3)

    return x, y


reta1 = get_reta()
reta2 = get_reta()

print(reta1, reta2)

print(get_intersecao(reta1, reta2))
