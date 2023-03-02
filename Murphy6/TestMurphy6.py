#Griffin Murphy | Project 6 | Unit Test

from Murphy6 import *
import unittest

class TestMurphy6(unittest.TestCase):

    def test_Front(self): #test method for Front()
        d = Deque()
        items = "Front" 
        result = d.Front(items) #tests by adding "Front" to front of deque
        self.assertEqual(d.items[0],"Front")


    def test_Back(self): #test method for Back()
        d = Deque()
        items = "Back"
        result = d.Back(items) #tests by adding "Back" to back of deque

        self.assertEqual(d.items[0],"Back")


if __name__ == "__main__":
    unittest.main()




