class Vector:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z
        
    @staticmethod
    def add(t, b):
        r = Vector()
        r._x = t._x + b._x
        r._y = t._y + b._y
        r._z = t._z + b._z
        return r
        
    @staticmethod
    def stp(t, b, m):
        s = Vector()
        s._w = t._x * (m._y * b._z - b._y * m._z) - t._y * (m._x * b._z - b._x * m._z) + t._z * (m._x * b._y - b._x * m._y)
        return s
        
def main():
    t = Vector(2, 1, 5)
    b = Vector(4, -1, -2)
    m = Vector(3, -2, 4)

    print(f't: ({t._x}, {t._y}, {t._z})')
    print(f'b: ({b._x}, {b._y}, {b._z})')
    print(f'm: ({m._x}, {m._y}, {m._z})')

    r = Vector.add(t, b)
    print(f't+b: ({r._x}, {r._y}, {r._z})')

    s = Vector.stp(t, b, m)
    print(f'stp: {s._w}')

main()