
class Matrix:
    def __init__(self, lst, r, cl):
        self.__list = lst
        self.__row = r
        self.__col = cl

    def __str__(self):
        s = ''
        z = 0
        for i in range(len(self.__list)):
            if z == self.__col:
                s += '\n'
                z = 0
            s += str(self.__list[i]) + ' '
            z += 1
        return s

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, r):
        self.__row = r

    @property
    def list(self):
        return self.__list

    @list.setter
    def list(self, l):
        self.__list = l

    @property
    def col(self):
        return self.__col

    @col.setter
    def col(self, c):
        self.__col = c

def main():
    m2 = Matrix([1,2,3,4,5,6], 3,2)
    print(m2)

main()


        
                
        
