
class Reta:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def get_equacao(self):
        coef = (self.y2 - self.y1) / (self.x2 - self.x1)
        intercep = self.y1 - coef * self.x1
        
        if coef < 0:
            print("A reta é descrescente")
        elif coef > 0:
            print("A reta é crescente")
        else:
            print("A reta é constante")
        
        return f'y = {coef:.2f}x + {intercep:.2f}'


class Func_afim:
    
    def __init__(self, a, x, b):
        self.a = a
        self.x = x
        self.b = b
        
    def calcular(self):
        return (self.a * self.x) + self.b