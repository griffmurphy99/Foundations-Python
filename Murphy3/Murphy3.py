#Griffin Murphy 


from random import randint #Imports the random module to be used to randomly assign ship locations on the board

grid =[[' ']*10 for x in range(10)]

letters_to_number={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9} #letter to number array to make the game more user friendly, like the real game

def drawBoard(board):
    print('  A B C D E F G H I J')
    row_num=0
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row))) #prints out the game board
        row_num +=1


def setupBoard(board):  #Creates the ships locations within the 2D array
    for ship in range(5):
        ship_r, ship_cl=randint(0,9), randint(0,9)
        
        while board[ship_r][ship_cl] =='S':
            ship_r, ship_cl = randint(0, 9), randint(0, 9) #assigns random integers for the ships columns and rows
            
        board[ship_r][ship_cl] = 'S' #sets the ships as 'S' on the game board


def shipLocation(): 
    #Enter the row number between 0 to 9
    row=input('Please enter a ship row 0-9 ').upper()
    
    while row not in '0123456789': #check if number entered is one of the characters in the array
        print("Please enter a valid row ")
        row=input('Please enter a ship row 0-9 ')
        
    #Enter the Ship column from A to J
    column=input('Please enter a ship column A-J ').upper()
    
    while column not in 'ABCDEFGHIJ': #check if number entered is one of the characters in the array
        print("Please enter a valid column ")
        column=input('Please enter a ship column A-J ')
    return int(row),letters_to_number[column] #updates the row and column variables, converts alphabet to number based on array above

def hitOrMiss(board):  #tells if a ship was hit or not
    count=0
    for row in board:
        for column in row:
            if column=='X':
                count+=1 #contributes to see if all 5 ships have been hit
    return count

setupBoard(grid) #sets up the board

turns = 10
while turns > 0:
    print('  Welcome to Battleship')
    drawBoard(grid) #Draws the board with the ships implemented
    row,column =shipLocation()
    if grid[row][column] == 'O': #checks if entered row and column has already been used
        print(' You already guessed that ')
    elif grid[row][column] =='S': #checks if entered row and column is a hit 
        print(' HIT ')
        grid[row][column] = 'X'
        turns -= 1
    else:
        print(' MISS ')
        grid[row][column] = 'O'
        turns -= 1
    if  hitOrMiss(grid) == 5: #calls the hitormiss method to see if all 5 ships were hit 
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("You sunk all the battleships ")
        break
    print(' You have ' +str(turns) + ' turns remaining ')
    if turns == 0:
        print('Game Over ')

