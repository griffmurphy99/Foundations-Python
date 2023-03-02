#Griffin Murphy | Project 4

class Rectangle:
    def __init__(self, length, width):  #creates an object Rectangle with attributes length and width
        self.length = int(length) #converts numbers entered from string to int
        self.width = int(width) #converts numbers entered from string to int

    def Perimeter(self):
        return 2*(self.length + self.width) #calculates and returns the Perimeter of the object Rectangle while utizing the length and width attributes

    def Area(self):
        return self.length*self.width #calculates and returns the Area of the object Rectangle while utizing the length and width attributes


    def display(self):
        print(f"The length is {self.length}, The width is {self.width}")
        print(f"The perimeter is ", self.Perimeter(), " The Area is ", self.Area())  #prints the perimeter and area called from the Perimeter()and Area() functions

class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width) #inheritance of the Rectangle class with attributes length and width
        self.height = int(height) #creates new object Parallelepiped with new attribute height

    def volume(self):
        return self.length * self.width * self.height #calculates and returns the volume of the object Parallelepiped while utizing the length and width and height attributes

    def display(self):
        print("The volume of myParallelepiped is: " , Parallelepiped.volume(self)) #calls on the attributes of the Parallelepiped object to print the volume


d = Rectangle(length=input('Please enter the length: '), width=input('Please enter the width: ')) #accepts users input and defines the length and width attributes for object Rectangle
d.display() #calls the display of object Rectangle length, width, perimeter, area
d2 = Parallelepiped(length=input('Please enter the length: '), width=input('Please enter the width: '), height=input('Please enter the height: ')) #accepts users input and defines length, width, height attributes of object parallelepiped
d2.display()#calls the display of object Parallelepiped volume

    
