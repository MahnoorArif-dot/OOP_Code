class Vector:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z
    
    @staticmethod
    def cross_product(v1, v2):
        cp = Vector()
        cp.x = (v1._y * v2._z) - (v1._z * v2._y)
        cp.y = (v1._z * v2._x) - (v1._x * v2._z)
        cp.z = (v1._x * v2._y) - (v1._y * v2._x)
        return cp
    
    @staticmethod
    def equality_test(v1, v2):
        if v1._x==v2._x and v1._y==v2._y and v1._z==v2._z:
            print('Both Vectors are Equal')
        else:
            print('Both Vectors are Not-Equal')

def main():
    # v1 = 2i+j+5k
    # v2 = 3i-2j+4k

    v1 = Vector(2,1,5)
    v2 = Vector(3,-2,4)

    print(f'Vector1: ({v1._x}, {v1._y}, {v1._z})')
    print(f'Vector2: ({v2._x}, {v2._y}, {v2._z})')

    cp = Vector.cross_product(v1, v2)
    print(f'Cross Product of vectors: ({cp.x}, {cp.y}, {cp.z})')

    Vector.equality_test(v1,v2)

main()