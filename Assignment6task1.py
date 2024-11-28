import math

class NDimensionalVector:
    def __init__(self, coordinates):  
        self.coordinates = coordinates
        self.dimension = len(coordinates)

    def calculate_magnitude(self):
        total_sum = sum(x ** 2 for x in self.coordinates)
        return math.sqrt(total_sum)

    def calculate_dot_product(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimensions of both vectors must be the same")
        return sum(x * y for x, y in zip(self.coordinates, other.coordinates))

    def __str__(self):
        return f"NDimensionalVector({self.coordinates})"

print("**Test Cases for N-Dimensional Vectors**")

vector_2d = NDimensionalVector([1, 5])
vector_3d = NDimensionalVector([2, 6, 9])
vector_4d = NDimensionalVector([3, 7, 2, 4])
vector_5d = NDimensionalVector([4, 8, 3, 5, 6])

print("2D vector magnitude:", vector_2d.calculate_magnitude())
print("3D vector magnitude:", vector_3d.calculate_magnitude())
print("4D vector magnitude:", vector_4d.calculate_magnitude())
print("5D vector magnitude:", vector_5d.calculate_magnitude())
print("Dot product of 2D vector with itself:", vector_2d.calculate_dot_product(vector_2d))
print("Dot product of 3D vector with itself:", vector_3d.calculate_dot_product(vector_3d))
print("Dot product of 4D vector with itself:", vector_4d.calculate_dot_product(vector_4d))
print("Dot product of 5D vector with itself:", vector_5d.calculate_dot_product(vector_5d))
