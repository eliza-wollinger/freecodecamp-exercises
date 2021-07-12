class Rectangle():

    def __init__(self, width, height):

        self.width = width
        self.height = height
    
    def __str__(self):

        return f"{type(self).__name__}(width={self.width}, height={self.height})"
    
    def set_width(self, new_width):

        self.width = new_width
    
    def set_height(self, new_height): 

        self.height = new_height
    
    def get_area(self):

        return self.width * self.height
    
    def get_perimeter(self):

        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self):

        return ((self.width ** 2) + (self.height ** 2)) ** 0.5
    
    def get_picture(self):

        if (self.width >= 50) or (self.height >= 50):
            return "Too big for picture."
        else:
            width_line = "".join(["*" for i in range(0, self.width)])
            shape = ""
            for height_level in range(0, self.height):
                shape += width_line + "\n"    
        return shape

    def get_amount_inside(self, shape):

        return self.get_area() // shape.get_area()

class Square(Rectangle):


    def __init__(self, side):
        
        super().__init__(width=side, height=side)

    def __str__(self):

        return f"{type(self).__name__}(side={self.width})"

    def set_side(self, new_side):

        super().set_height(new_side)
        super().set_width(new_side)
    
    def set_height(self, new_height):

        self.set_side(new_height)
    
    def set_width(self, new_width):

        self.set_side(new_width)
