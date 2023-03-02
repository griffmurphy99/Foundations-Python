#Griffin Murphy | Assignment 6 | 02/28/2023

class Deque:
    def __init__(self):
        self.items = []
    def Back(self, data:str): #Method for appending right of deque
        self.items.append(data)
    def Front(self, data:str): #Method for appending left of deque
        self.items.insert(0, data)
    def display(self):
        print(self.items)
 
d = Deque()
print('''
                        Welcome to the waitlist.

To add a person to the front of the line enter "front" followed by their name
(ex front Paul)
To add a person to the back of the line enter "back" followed by their name
(ex back John)
To see all users in line enter "display"
To end the program enter "stop" 
''')

while True:
    x = input('Enter what you would like to do: ').split()
 
    option = x[0].strip().lower()
    if option == 'back':
        d.Back(str(x[1]))
    elif option == 'front':
        d.Front(str(x[1]))
    elif option == 'display':
        d.display()
    elif option == 'stop':
        print('Goodbye!')
        break


