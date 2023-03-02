#Griffin Murphy | Project 4 | Unit Test


from Murphy4 import *

import unittest

from unittest.mock import patch

class TestMurphy4(unittest.TestCase):

    def test_Perimeter(self):
        '''test_perimeter() Test Documentation:
        This test makes sure the perimeter() function calculates numbers correctly 

        Details:
        rect1 = Rectangle(5,5): We instantiate the object rect1 as a
        Rectangle with attributes length and width both set to the value 5
        and call the perimeter() fuction on it to compare.
        
        secondNum = 20.
        We use secondNum to verify perimeter() is calculating the right value
        which should return 20 in this instance
        '''
        rect1 = Rectangle(5,5)
        firstNum = rect1.Perimeter()
        secondNum = 20
        self.assertEqual(firstNum, secondNum)
        
    def test_Area(self):
        '''test_area() Test Documentation
        This test checks to make sure the area() function calculates properly
        
        Details:
        rect1 = Rectangle(5,5): We instantiate the object rect1 with
        attributes length and width both set to the value 5 and call the
        Area() method on it to compare.
        
        secondNum = 25.
        We use secondNum to verify Area() is calculating the right value
        which should return 25 in this instance
        '''
        rect1 = Rectangle(5,5)
        firstNum = rect1.Area()
        secondNum = 25
        self.assertEqual(firstNum, secondNum)

    def test_volume(self):
        '''test_volume() Test Documentation
        This test checks to make sure the volume() functiom calculates properly
        
        Details:
        rect1 = Parallelepiped(5,5,5): We instantiate the object rect1 as a
        Parallelepiped with attributes length and width and height all set to
        the value 5 and call the volume() method on it to compare.
        
        secondNum = 125.

        We use secondNum to verify volume() is calculating the right value which
        should return 125 in this instance
        '''
        rect1 = Parallelepiped(5,5,5)
        firstNum = rect1.volume()
        secondNum = 125
        self.assertEqual(firstNum, secondNum)



        
if __name__ == "__main__":
    unittest.main()
