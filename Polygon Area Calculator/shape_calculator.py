class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __str__(self):
        return  "Rectangle(width={w}, height={h})".format(w=self.width, h=self.height)

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        pic = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for _ in range(self.height):
                pic += "*"*self.width + "\n"
            return pic

    def get_amount_inside(self, shape):
        return self.get_area()//shape.get_area() if self.get_area() >= shape.get_area() else 0


class Square(Rectangle):
    def __init__(self, side):
        self.width = self.height = side

    def __str__(self):
        return  "Square(side={s})".format(s=self.width)

    def set_side(self, s):
        self.width = self.height = s

