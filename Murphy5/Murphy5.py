
#Griffin Murphy | Assignment 5 | 02/21/2023

class Student:
    def __init__(self, name, age): #creates object Student with attributes name and age
        self.name = str(name)
        self.age = str(age)

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}") #calls the attributes from object Student and prints string values for name and age attributes
        
class Engineer(Student):
    def __init__(self, name, age, courses): #creates object Engineer with attributes name, age, and course
        super().__init__(name, age) #inheritance of the Student class with attributes name and age
        self.courses = str(courses)

    def displayEngineer(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.courses}") #calls the attributes from object Engineer and prints string values for name, age, and course attributes

class Doctor(Student):
    def __init__(self, name, age, hospital):  #creates object Doctor with attributes name, age, and hospital
        super().__init__(name, age) #inheritance of the Student class with attributes name and age
        self.hospital = str(hospital)
        
    def displayDoctor(self):
        print(f"Name: {self.name}, Age: {self.age}, Hospital: {self.hospital}") #calls the attributes from object Doctor and prints string values for name, age, and hospital attributes

S = Student("Griffin", "23") #testing 
S.display() #calls the display of object Doctor name and age
E = Engineer("David", "27", "Math") #testing
E.displayEngineer() #calls the display of object Enginner name, age, and course
D = Doctor("Luke", "32", "Childrens Hospital") #testing
D.displayDoctor() #calls the display of object Doctor name, age, and hospital





