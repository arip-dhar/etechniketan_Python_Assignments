# 1. Which keyword is used to define an anonymous function in Python? 
# a. def 
# b. func 
# c. anonymous 
# d. lambda 

square = lambda num: num * num ## 'lambda' creates single-line functions without using 'def'.
print(f"Lambda function result for square of: {square(4)}") # display the square of 4. Output: 16

#Ans:- (D) lambda 
# ___________________________________________________________________________ 1 ____________________________________________________________________________________________


# 2. What does a module in Python represent? 
# a. A function 
# b. A directory of files 
# c. A python file with .py extension 
# d. Combination of many python files 

import math  # The 'import' keyword loads the math module (.py file built into Python)  
print("Successfully imported 'math' module.") # Shows the math modules successfully load

#Ans:- (C) A python file with .py extension 
# ___________________________________________________________________________ 2 ____________________________________________________________________________________________


# 3. Which keyword is used to use modules in Python? 
# a. load 
# b. include 
# c. module 
# d. import 

import math  # The 'import' keyword loads all modules  
print("Successfully useed 'import keyword.") #print that the import keyword successfully added.

#Ans:- (D) import
# ___________________________________________________________________________ 3 ____________________________________________________________________________________________


# 4. Which syntax imports only the sqrt() function from math module? 
# a. import sqrt from math 
# b. import sqrt 
# c. from sqrt import math 
# d. from math import sqrt 

from math import sqrt  #This is using exact sytax for imports the sqrt() function.
print(f"Square root of 16 using directly imported sqrt(): {sqrt(16)}") #Print directly sqare number. Output: 4 

#Ans:- (D) from math import sqrt
# ___________________________________________________________________________ 4 ____________________________________________________________________________________________


# 5. What error occurs if blocks of code are not properly aligned in Python? 
# a. IndentationError 
# b. SyntaxError 
# c. TypeError 
# d. ValueError


print("Misalignment causes IndentationError") #Python uses indentation (spaces/tabs) to group lines. 

#Ans:- (A)IndentationError
# ___________________________________________________________________________ 5 ____________________________________________________________________________________________


# 6. What is the parent of all exceptions? 
# a. AllError 
# b. Error 
# c. Exception 
# d. ValueError

try:
    result = 10 / 0
except Exception as error:  # Catches the error using the parent Exception class inside the except block
    print(f"Error successfully handled: {error}") # print what what error we get handled.

#Ans:- (C) Exception
# ___________________________________________________________________________ 6 ____________________________________________________________________________________________


# 7. Which block is used to handle exceptions in Python? 
# a. except 
# b. catch 
# c. try 
# d. else 

try: 
    result = 10 / 0
except Exception as error:  # Catches the error using the parent Exception class inside the except block & 'except' block we used to handle exception in python.
    print("Error successfully handled: ", error) # print what what error we get handled.

#Ans:- (A) except
# ___________________________________________________________________________ 7 ____________________________________________________________________________________________


# 8. WAP to create a function named ‘introduce’ that takes 2 arguments: 
# a. name – positional argument 
# b. age – default argument with a default value of None. 
# If age is provided while calling the function, introduce(“John”, 20), print => 
# My name is John. I am 20 years old. 
# If age is not provided while calling the function, introduce(“John”), print =>  
# My name is John. My age is secret. 

def introduce(name, age=None):  # name is positional, age has a default value of None
    if age is not None: #We using if else statement that confirm age is provided or not.
        print(f"My name is {name}. I am {age} years old.")  #If age is provided print age and name.
    else:
        print(f"My name is {name}. My age is secret.") #If age is not provided print name only.

introduce("John", 20)  # Provided age
introduce("John")      # Age not provided
# ___________________________________________________________________________ 8 ____________________________________________________________________________________________


# 9. WAP to create a function drop_minimum that takes variable length arguments (*args). 
# The function takes integers and returns a list of these integers after removing the 
# minimum value from the arguments. 
# Example: drop_minimum(5, -2, 8, 4, -5, 7, 10), output => [5, -2, 8, 4, 7, 10]


def drop_minimum(*args): #create a function that takes variable length argument(*args)
    numbers_list = list(args)  # Convert the inputs tuple into a mutable list
    if numbers_list:
        min_value = min(numbers_list)  # Find the lowest value
        numbers_list.remove(min_value)  # Remove the lowest value from the list
    return numbers_list

print("Result after dropping minimum:", drop_minimum(5, -2, 8, 4, 5, 7, 10)) #In these numbere list remove or delete minimum number that is (-2) and print remaining number.
# ___________________________________________________________________________ 9 ____________________________________________________________________________________________


# 10. A function find_max(a, b, c) that returns the largest of its three arguments by calling the 
# built-in max() function. Create another function called main() that reads three user inputs 
# x, y & z from the user (integers) and calls find_max() function. The main() function 
# should print only the resulting maximum value.

def find_max(a, b, c): #create a function that returns the largfest of its(a b c) three arguments
    return max(a, b, c)  # Calls the built-in max() function

def main():
    # Simulating the user input for demonstration (Change these numbers to test different inputs)
    x, y, z = 15, 42, 23
    print(f"Simulating user inputs: x={x}, y={y}, z={z}") #Shows what nu,ber given for (x y z) by users 
    maximum = find_max(x, y, z) #Find maximun number of those three numbers
    print(f"Resulting maximum value: ",maximum) #print maximum number only.

main()  # Run the main block layout
# ___________________________________________________________________________ 10 ____________________________________________________________________________________________


# 11. Write a lambda function to add two numbers. 

addition = lambda num1, num2: num1 + num2 #create 'lamda' function name is 'addition'
print(f"Result of lambda addition : {addition(10, 20)}") #print the addition of two numbers (10 & 20).
# ___________________________________________________________________________ 11 ____________________________________________________________________________________________


# 12.  Write a lambda function that accepts a temperature in Celsius (a float number), converts 
# it to the Fahrenheit scale using the formula: Fahrenheit = Celsius * 9 / 5 + 32 

celsius_to_fahrenheit = lambda celsius: celsius * 9 / 5 + 32  #Create lamda function for a temperature in Celsius (a float number), converts it to the Fahrenheit scale using the formula: Fahrenheit = Celsius * 9 / 5 + 32
print(f"Conversion of 37.5°C to Fahrenheit: {celsius_to_fahrenheit(37.5)}") #print the converted fahrenheit number of the given number
# ___________________________________________________________________________ 12 ____________________________________________________________________________________________


# 13. Write a Python program to create a file called student.txt. Write the following three lines 
# into it:  
# Python is easy to learn. 
# File handling is important.  
# Practice makes perfect. 
# Use exception/error handing to catch FileExists error and all errors (Exception). 

try: #The try block houses the code that might throw an error.
    with open("student.txt", "w") as file: # 'w' opens the file for writing.
        file.write("Python is easy to learn.\n")  #'.write() function is a method into a file to write somenthing in file.
        file.write("File handling is important.\n") 
        file.write("Practice makes perfect.\n") 
    print("student.txt created and populated successfully.") #when file created without any error so print that the file populated successfully.
except FileExistsError:
    print("Error: The file already exists.")  # If file already created then this error handled bacause we don't need duplicate files then print file already exits.
except Exception as e:
    print(f"An unexpected error occurred: {e}") # If file not created so showing the error why file not created.
# ___________________________________________________________________________ 13 ____________________________________________________________________________________________


# 14. Write a program to read the contents of student.txt and 
# a. Print all content 
# Output: 
# Python is easy to learn. 
# File handling is important. 
# Practice makes perfect. 
# b. Print line-by-line.  
# Output:  
# Line 1: Python is easy to learn. 
# Line 2: File handling is important.  
# Line 3: Practice makes perfect. 

try:
    with open("student.txt", "r") as file: # 'r' opens the file for reading into file.
        lines = file.readlines() #read the file line by line
    
    print("Print all content:") #Printing All Content (Preserving Structure)
    for line in lines:
        print(line, end="")  # end="" avoids double spacing #Q : A
        
    print("\nPrint line-by-line:") #Numbered count Line-by-Line Print 
    for index, line in enumerate(lines, start=1):
        print(f"Line {index}: {line.strip()}")  # .strip() cleans up the trailing newline , #Q : B
except FileNotFoundError:
    print("The file student.txt was not found.") #iF file not found so print it that file not found.
# ___________________________________________________________________________ 14 ____________________________________________________________________________________________


# 15. Write a Python program to count how many words are present in student.txt.  
# Output: 
# Total words: 12 

try:
    with open("student.txt", "r") as file: # 'r' opens the file for reading into file.
        content = file.read() #read the file line by line
    words = content.split()  # Splitting by space isolates each word
    print(f"Total words: {len(words)}")  # Output: Total words: 12
except FileNotFoundError:
    print("File missing.") #if file not found so print it that file missing.
# ___________________________________________________________________________ 15 ____________________________________________________________________________________________


# 16. Write a Python program to add the below line to the file: 
# Python file handling becomes simple with practice. 

try:
    with open("student.txt", "a") as file: # 'a' stands for append mode, which adds text safely to the bottom without overwriting
        file.write("Python file handling becomes simple with practice.\n")  #'.write() function is a method into a file to write somenthing in file.
    print("Line successfully appended to student.txt.") #After addming line it's print that line successfully added.
except Exception as e:
    print(f"Error appending line: {e}") # If something fails for ading lines what's the  error shows us.
# ___________________________________________________________________________ 16 ____________________________________________________________________________________________


# 17. Create a list, numbers = [7, 4, 0, -2, 3]. Print this list. Then ask the user to provide an 
# index for which they want to value. Use exception handling to handle IndexError.

numbers = [7, 4, 0, -2, 3]  
print("List: ",numbers)  

simulated_user_index = 8 # Simulating index request safely (Change this variable to try out errors!)
print(f"User requested value at index position: {simulated_user_index}") #print what index number user requested value?

try:
    value = numbers[simulated_user_index] #if the number in that index
    print(f"Value found: {value}") #print the value of the index
except IndexError:
    print("Exception Handled: IndexError! That index position does not exist in the list.") #if the user requested index not in numbers index so print or handles the error that it's does not exist.
# ___________________________________________________________________________ 17 ____________________________________________________________________________________________


# 18. Create a python module named calculator.py. Define the following functions inside it:  
# add(a, b) 
# subtract(a, b) 
# multiply(a, b) 
# divide(a, b) 
# Create another file main.py where you import the module and call all functions by 
# passing the values to the arguments.
 
#/////////////////////////////////////////////////////////////((PLEASE CHECK calculator.py FILE BEFORE THIS))/////////////////////////////////////////////////////////////////////////
 # main.py - Primary Module Controller Loop
import calculator  # Imports your custom calculator module[cite: 2]

def run_calculator_tests():
    x, y = 20, 5     # Pass arbitrary numbers to test the calculator function arguments
    
    print("--- calculator.py Module Verification ---")
    print(f"Inputs: a = {x}, b = {y}\n") #Shows what inputs given of a & b value by users
    print("Addition Result:      ", calculator.add(x, y)) # Addition (a + b)        
    print("Subtraction Result:   ", calculator.subtract(x, y))   # Substraction (a - b)
    print("Multiplication Result:", calculator.multiply(x, y))   # Multiplication (a * b)
    print("Division Result:       ", calculator.divide(x, y))     # Division (a / b)

if __name__ == "__main__":
    run_calculator_tests()

print("\n==============================================================================")
print("Assignment 3 main file demonstration completed!")
print("==============================================================================")
# ___________________________________________________________________________ 18 ____________________________________________________________________________________________


# ________________________________________________________________***END*** _____________________________________________________________________________________________________
