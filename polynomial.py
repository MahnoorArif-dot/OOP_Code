class Polynomial:
    def __init__(self, c):
        self.c = c

    @staticmethod
    def add(poly1, poly2):
        n = []
        for i in range(max(len(poly1.c), len(poly2.c))):
            n.append(poly1.c[i] + poly2.c[i])
        return Polynomial(n)

    @staticmethod
    def sub(poly1, poly2):
        n = []
        for i in range(max(len(poly1.c), len(poly2.c))):
            n.append(poly1.c[i] - poly2.c[i])
        return Polynomial(n)

    @staticmethod
    def mul(poly1, poly2):
        n = []
        for i in range(len(poly1.c)):
            for j in range(len(poly2.c)):
                n.append(poly1.c[i] * poly2.c[j])
        return Polynomial(n)

    @staticmethod
    def stringify(poly):
        result = ""
        for i in range(len(poly.c)):
            if poly.c[i] != 0:
                if i == 0:
                    result += str(poly.c[i])
                elif i == 1:
                    result += "+" + str(poly.c[i]) + 'x'
                else:
                    result += "+" + str(poly.c[i]) + 'x^' + str(i)
        return result




