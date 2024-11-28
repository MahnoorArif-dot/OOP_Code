import tkinter as tk

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, canvas):
        raise NotImplementedError("Subclasses must implement the draw method")

    def area(self):
        raise NotImplementedError("Subclasses must implement the area method")

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height)

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, x, y, side):
        super().__init__(x, y, side, side)

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius)

    def area(self):
        return 3.14159 * self.radius * self.radius

class Oval(Circle):
    def __init__(self, x, y, radius, radius2):
        super().__init__(x, y, radius)
        self.radius2 = radius2

    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius2,
                           self.x + self.radius, self.y + self.radius2)

    def area(self):
        return 3.14159 * self.radius * self.radius2
shapes = [Rectangle(10, 10, 50, 30), Circle(80, 60, 30), Square(150, 100, 40), Oval(220, 150, 50, 20)]
window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()

for shape in shapes:
    shape.draw(canvas)

window.mainloop()

