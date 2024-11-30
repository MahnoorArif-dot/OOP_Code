class Vector:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z
        
    @staticmethod
    def unit_vector(a):
        r = Vector()
        r._x = a._x **2
        r._y = a._y **2
        r._z = a._z **2
        r._w=r._x+r._y+r._z
        r._a=r._w*0.5
        return r
    
    @staticmethod
    def scalar_multiple(a):
        s = Vector()
        n=3
        s._x = a._x *n
        s._y = a._y *n
        s._z = a._z *n
        return s

        
def main():
    a = Vector(2, 1, 5)

    r = Vector.unit_vector(a)
    print(f'Unit Vector: {r._x/r._a}i + {r._y/r._a}j + {r._z/r._a}k')

    s=Vector.scalar_multiple(a)
    print(f'Scalar Multiple of Vector: {s._x}i + {s._y}j + {s._z}k')

main()