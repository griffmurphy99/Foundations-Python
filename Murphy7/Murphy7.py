#Griffin Murphy | Assignment 7 | 03/06/2023
import random
import time

# Selection Sort algorithm in Python
def bubbleSort(arr):
     
    n = len(arr)
 
    for i in range(n): #makes sure to go through entire list of values depending on n value
        for j in range(0, n - i - 1):
             
            # Range of the array is from 0 to n-i-1
            # if the value is found then swap them based on one greater than the other
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                

# Selection Sort algorithm

def selectionSort(array, size):
     
    for s in range(size):
        minNums = s
         
        for i in range(s + 1, size):
             
            # For sorting in descending order
            # for minimum element in each loop
            if array[i] < array[minNums]:
                minNums = i
                
        # Arranging min at the correct position
        (array[s], array[minNums]) = (array[minNums], array[s])
        
        
        
#Generate n random numbers between x and y (0 - 100,000)
def generateNumbers(x=0, y=100000000, n = 10000 ):
    return random.sample(range(x, y), n)
    
    
if __name__ == "__main__":
    
    # generate random numbers
    nums = generateNumbers()
    print("Array is", len(nums), "values long")
    
    #before we start the start 1st function, we save the time in a variable  
    s1 =  time.time()
   # n1 = nums
    print("Time when the Bubble sort begins: ",s1) #display the start time of the function
    bubbleSort(nums) #runs the selection sort
    print("time Bubble Sort took: ", time.time() - s1, " milliseconds") # finds the total sort time by substracting the start time from the total time  

    
    # same with func 2
    s2 = time.time()
   # n2 = nums
    print("Time when the Selection Sort begins: ", s2) #display the start time of the function
    selectionSort(nums, len(nums))   #Runs the selection sort
    print("time Selection Sort took: ", time.time() - s2, "milliseconds") # finds the total sort time by substracting the start time from the total time  
