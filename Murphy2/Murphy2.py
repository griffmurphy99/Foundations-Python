
def main():
    while True:
        x = float(input("Enter the first positive Integer: "))
        y = float(input("Enter the second positive Integer: "))
        
        if(x < 0) or (y < 0):
            print("Not positive integers. Program end")
            return #Breaks the while loop and stops program from execuding code

        if x % y == 0: #calculates if the first number is evenly divisable by the second
          print("True")
   
        else:
            print("False") #prints false if they dont devide evenly
    
main()
