class Shape:
    value_of_pie = 3.14
    
    def __init__(self, name, bg, outline):
        self.name = name
        self.bg = bg
        self.outline = outline

class Circle(Shape):
    def __init__(self, name, bg, outline, radius):
        super().__init__(name, bg, outline)
        self.radius = radius

    def area_of_circle(self):
        self.area = int(Shape.value_of_pie * (self.radius**2))
        return self.area

class Rectangle(Shape):
    def __init__(self, name, bg, outline,length,base):
        super().__init__(name, bg, outline)
        self.length = length
        self.base = base

    def area_of_rectangle(self):
        self.area = int(self.base*self.length)
        return self.area

def main():
    circle_obj = Circle('Circle', 'Yellow', 'Yellow', 2)
    rect_obj = Rectangle('Circle', 'Yellow', 'Yellow',2,4)
    area1 = circle_obj.area_of_circle()
    area2 = rect_obj.area_of_rectangle()
    print('AREA OF CIRCLE:', area1)
    print('AREA OF RECTANGLE:', area2)

main()
