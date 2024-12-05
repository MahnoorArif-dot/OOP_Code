class Matrix:
    def __init__(self, a=0, b=0, c=0, d=0):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    @staticmethod
    def add_mat(a, b):
        print('Addition of 2 matrices')
        s = Matrix()
        s._a = a._a + b._a
        s._b = a._b + b._b
        s._c = a._c + b._c
        s._d = a._d + b._d
        print(f'({s._a} {s._b} {s._c} {s._d})')

    @staticmethod
    def sub_mat(a, b):
        print('Subtraction of 2 matrices')
        s = Matrix()
        s._a = a._a - b._a
        s._b = a._b - b._b
        s._c = a._c - b._c
        s._d = a._d - b._d
        print(f'{s._a} {s._b} {s._c} {s._d}')
        print()

    @staticmethod
    def scalar(a):
        n = 5
        print('Scalar matrix')
        print(f'{a._a * n} {a._b * n} {a._c * n} {a._d * n}')

    @staticmethod
    def mult_mat(a, b):
        print('Multiplication of Two matrices')
        s = Matrix()
        s._a = (a._a * b._a) + (a._b * b._c)
        s._b = (a._a * b._b) + (a._b * b._d)
        s._c = (a._c * b._a) + (a._d * b._c)
        s._d = (a._c * b._b) + (a._d * b._d)
        print(f'{s._a} {s._b} {s._c} {s._d}')

    @staticmethod
    def det(a, b):
        d1 = (a._a * a._d) - (a._b * a._c)
        d2 = (b._a * b._d) - (b._b * b._c)
        print('Determinant of matrix a:', d1)
        print('Determinant of matrix b:', d2)

    @staticmethod
    def tran(a, b):
        print('Transpose of matrices')
        print(f'{a._a} {a._c} {a._b} {a._d}')
        print(f'{b._a} {b._c} {b._b} {b._d}')
        
    @staticmethod
    def cofactor(a, b):
        print('Cofactor of matrices')
        print(f'{a._d} {-a._c} {-a._b} {a._a}')
        print(f'{b._d} {-b._c} {-b._b} {b._a}')
        
    @staticmethod
    def singular(a, b):
        print ('Singular or Non-Singular Matrix:')
        d1 = (a._a * a._d) - (a._b * a._c)
        d2 = (b._a * b._d) - (b._b * b._c)
        if d1==0:
            print('Matrix a is Singular Matrix')
        else:
            print('Matrix a is Non-Singular Matrix')
        if d2==0:
            print('Matrix b is Singular Matrix')
        else:
            print('Matrix b is Non-Singular Matrix')
    
    @staticmethod
    def Inverse(a, b):
        d1 = (a._a * a._d) - (a._b * a._c)
        d2 = (b._a * b._d) - (b._b * b._c)
        print(f'adj1={a._d} {-a._c} {-a._b} {a._a}')
        print(f'adj2={b._d} {-b._c} {-b._b} {b._a}')
        print('Inverse of matrix a')
        s=Matrix()
        s._w=a._d/d1
        s._x=-a._b/d1
        s._y=-a._c/d1
        s._z=a._a/d1
        print(f'({s._w} {s._x} {s._y} {s._z})')
        print('Inverse of matrix b')
        s._w=a._d/d2
        s._x=-a._b/d2
        s._y=-a._c/d2
        s._z=a._a/d2
        print(f'({s._w} {s._x} {s._y} {s._z})')
        
    @staticmethod
    def division(a,b):
        print('Division of Two matrices')
        s = Matrix()
        d2 = (b._a * b._d) - (b._b * b._c)
        s._w=a._d/d2
        s._x=-a._b/d2
        s._y=-a._c/d2
        s._z=a._a/d2
        s._a = (a._a * s._w) + (a._b * s._y)
        s._b = (a._a * s._x) + (a._b * s._z)
        s._c = (a._c * s._w) + (a._d * s._y)
        s._d = (a._c * s._y) + (a._d * s._z)
        print(f'({s._a} {s._b} {s._c} {s._d})')
    
    @staticmethod
    def null(a):
        s=Matrix()
        s._a=s._a-s._a
        s._b=s._b-s._b
        s._c=s._c-s._c
        s._d=s._d-s._d
        print(f'Null Matrix')
        print(f'({s._a} {s._b} {s._c} {s._d})')
        
    @staticmethod
    def identity(a):
        m=Matrix()
        if m._a==1 and m._b==0 and m._c==0 and m._d==1:
            print('Matrix a is a Identity Matrix')
        else:
            print('Matrix a is not a Identity Matrix')
def main():
    a=Matrix(2,4,6,8)
    b=Matrix(1,3,5,7)
    Matrix.add_mat(a, b)
    Matrix.sub_mat(a, b)
    Matrix.scalar(a)
    Matrix.mult_mat(a, b)
    Matrix.det(a, b)
    Matrix.tran(a, b)
    Matrix.cofactor(a,b)
    Matrix.singular(a,b)
    Matrix.Inverse(a,b)
    Matrix.division(a,b)
    Matrix.null(a)
    Matrix.identity(a)

class Matrix:
    def __init__(self, a=0, b=0, c=0, d=0):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    @staticmethod
    def add_mat(a, b):
        print('Addition of 2 matrices')
        s = Matrix()
        s._a = a._a + b._a
        s._b = a._b + b._b
        s._c = a._c + b._c
        s._d = a._d + b._d
        print(f'({s._a} {s._b} {s._c} {s._d})')

    @staticmethod
    def sub_mat(a, b):
        print('Subtraction of 2 matrices')
        s = Matrix()
        s._a = a._a - b._a
        s._b = a._b - b._b
        s._c = a._c - b._c
        s._d = a._d - b._d
        print(f'{s._a} {s._b} {s._c} {s._d}')
        print()

    @staticmethod
    def scalar(a):
        n = 5
        print('Scalar matrix')
        print(f'{a._a * n} {a._b * n} {a._c * n} {a._d * n}')

    @staticmethod
    def mult_mat(a, b):
        print('Multiplication of Two matrices')
        s = Matrix()
        s._a = (a._a * b._a) + (a._b * b._c)
        s._b = (a._a * b._b) + (a._b * b._d)
        s._c = (a._c * b._a) + (a._d * b._c)
        s._d = (a._c * b._b) + (a._d * b._d)
        print(f'{s._a} {s._b} {s._c} {s._d}')

    @staticmethod
    def det(a, b):
        d1 = (a._a * a._d) - (a._b * a._c)
        d2 = (b._a * b._d) - (b._b * b._c)
        print('Determinant of matrix a:', d1)
        print('Determinant of matrix b:', d2)

    @staticmethod
    def tran(a, b):
        print('Transpose of matrices')
        print(f'{a._a} {a._c} {a._b} {a._d}')
        print(f'{b._a} {b._c} {b._b} {b._d}')
        
    @staticmethod
    def cofactor(a, b):
        print('Cofactor of matrices')
        print(f'{a._d} {-a._c} {-a._b} {a._a}')
        print(f'{b._d} {-b._c} {-b._b} {b._a}')
        
    @staticmethod
    def singular(a, b):
        print ('Singular or Non-Singular Matrix:')
        d1 = (a._a * a._d) - (a._b * a._c)
        d2 = (b._a * b._d) - (b._b * b._c)
        if d1==0:
            print('Matrix a is Singular Matrix')
        else:
            print('Matrix a is Non-Singular Matrix')
        if d2==0:
            print('Matrix b is Singular Matrix')
        else:
            print('Matrix b is Non-Singular Matrix')
    
    @staticmethod
    def Inverse(a, b):
        d1 = (a._a * a._d) - (a._b * a._c)
        d2 = (b._a * b._d) - (b._b * b._c)
        print(f'adj1={a._d} {-a._c} {-a._b} {a._a}')
        print(f'adj2={b._d} {-b._c} {-b._b} {b._a}')
        print('Inverse of matrix a')
        s=Matrix()
        s._w=a._d/d1
        s._x=-a._b/d1
        s._y=-a._c/d1
        s._z=a._a/d1
        print(f'({s._w} {s._x} {s._y} {s._z})')
        print('Inverse of matrix b')
        s._w=a._d/d2
        s._x=-a._b/d2
        s._y=-a._c/d2
        s._z=a._a/d2
        print(f'({s._w} {s._x} {s._y} {s._z})')
        
    @staticmethod
    def division(a,b):
        print('Division of Two matrices')
        s = Matrix()
        d2 = (b._a * b._d) - (b._b * b._c)
        s._w=a._d/d2
        s._x=-a._b/d2
        s._y=-a._c/d2
        s._z=a._a/d2
        s._a = (a._a * s._w) + (a._b * s._y)
        s._b = (a._a * s._x) + (a._b * s._z)
        s._c = (a._c * s._w) + (a._d * s._y)
        s._d = (a._c * s._y) + (a._d * s._z)
        print(f'({s._a} {s._b} {s._c} {s._d})')
    
    @staticmethod
    def null(a):
        s=Matrix()
        s._a=s._a-s._a
        s._b=s._b-s._b
        s._c=s._c-s._c
        s._d=s._d-s._d
        print(f'Null Matrix')
        print(f'({s._a} {s._b} {s._c} {s._d})')
        
    @staticmethod
    def identity(a):
        m=Matrix()
        if m._a==1 and m._b==0 and m._c==0 and m._d==1:
            print('Matrix a is a Identity Matrix')
        else:
            print('Matrix a is not a Identity Matrix')
def main():
    a=Matrix(2,4,6,8)
    b=Matrix(1,3,5,7)
    Matrix.add_mat(a, b)
    Matrix.sub_mat(a, b)
    Matrix.scalar(a)
    Matrix.mult_mat(a, b)
    Matrix.det(a, b)
    Matrix.tran(a, b)
    Matrix.cofactor(a,b)
    Matrix.singular(a,b)
    Matrix.Inverse(a,b)
    Matrix.division(a,b)
    Matrix.null(a)
    Matrix.identity(a)

main()