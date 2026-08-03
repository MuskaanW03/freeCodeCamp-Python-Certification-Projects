from math import sqrt

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*(self.width + self.height)
    
    def get_diagonal(self):
        return sqrt((self.width)**2 + (self.height)**2)
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_picture(self):
        if self.width > 50 or self.height>50:
            return 'Too big for picture.'
        
        return (int(self.width)*'*'+'\n')*(int(self.height))

    def get_amount_inside(self, shape):
        fit_width = self.width//shape.width
        fit_height= self.height//shape.height

        return fit_width*fit_height
    
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length,side_length) 
    
    def set_width(self,width):
        self.width = width
        self.height = width
    
    def set_height(self,height):
        self.width = height
        self.height = height
    
    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def __str__(self):
        return f"Square(side={self.width})"