class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if(self.width > 50 or self.height > 50):
            return "Too big for picture."
        string = (("*" * self.width) + "\n") * self.height
        return string

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side

    
# Thanks to Landon Schlangen who walked me through this FreeCodeCamp Project.
# The video I watched that (which he was kind enough to take the time to provide)
# is at his youTube channel Landon Schlangen.. https://www.youtube.com/channel/UC4oRFTHw71_CBSHAcCRmV6w
# The link is https://www.youtube.com/watch?v=sMVCsctweh4

# This is my forth time with python and I will come back to this project as I
# further skills through the other projects.
# Python is getting easier, at least with this project, as i found myself moved through this project faster.
# Thank you again to everyone that shares their knowledge to help others learn.
#
# 9/19/2021
# Done on VS Code
