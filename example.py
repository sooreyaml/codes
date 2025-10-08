class Rectangle:
    def __init__(self,height, width,color):
        self.height = height
        self.width = width
        self.color = color
    
    def add_height(self, h):
        self.height = self.height + h
        return self.height