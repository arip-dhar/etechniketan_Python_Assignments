# 1. Write a Python program that prints all the keywords available in Python. 

import keyword

print ("Total available Python Keyword is: ", keyword.kwlist) #Print the list of the available keywords.
# ______________________________________________________________________________ 1 _____________________________________________________________________


# 2. Create a variable x = 10 and print its type. 
x = 10 #Storing the value in X.

print ("The types of x is: ",type(x)) #Print type of value that store in X.
# ______________________________________________________________________________ 2 ______________________________________________________________________


# 3. Create a tuple with 4 numbers and print its last element and second element. 

tuple = (1, 2, 3, 4) #Creating the tuple with 4 numbers

print ("Last element is: ", tuple[-1]) #It's print the last element , here last element is 4.

print ("Second element is: ", tuple[1]) #It's Print the 2nd element, here last element is 2. But in python start counting from 0.
# ______________________________________________________________________________ 3 ________________________________________________________________________


# 4. Convert the string "123" into an integer and add 10 to it. Store the result in a variable and print it. '

num = "123" #String strig format value in num.

conv = int(num) + 10 #Converting String to Int format and add 10.

print ("Converted with addition is: ", type(conv)) #Print the result with its type.
# ________________________________________________________________________________ 4 ________________________________________________________________________


# 5. Take a float number and convert it into an integer.  

dec = 36.23 #Taking float value in dec

print ("The addition is in Int format is: ",int (dec)) #Printing dec value with converted to int.
# ________________________________________________________________________________ 5 __________________________________________________________________________


# 6. Join two strings "Hello" and "World" with a space in between. Find the length of the new string. 

val_1 = "Hello" #Taking value 1 as a string format.

val_2 = "World" #Taking value 2 as a string format.

mixed = val_1 + " " + val_2 #Giving space between the value 1 and value 2.

print ("New word is: ", mixed) #Print the full short sentence.

print ("The length is: ", len(mixed)) #Print the length of short sentence.
# _________________________________________________________________________________ 6 ______________________________________________________________________________


# 7. Take a boolean variable flag = True and print its type. 

flag = True #Take a value as a flaG = True.

print("The types of flag is: ",type(flag)) # Print it's type.
# _________________________________________________________________________________ 7 ______________________________________________________________________________


# 8. Find the length of a tuple (10, 20, 30, 40, 50) 

Tuple = (10, 20, 30, 40, 50) #Taking value into Tuple.

print ("The length of tuple is: ",len(Tuple)) #Print the Tuple length.
# _________________________________________________________________________________ 8 ________________________________________________________________________________


#9. Given 2 variables: language = “Python” version = 3.13 Create a new variable called result with “Python3.13” as the value using the variables language and version. 

language = "Python" # here is the variable 1 that the giving question.

version = "3.13"  # here is the variable 2 that the giving question.

result = language + version #Combined both variable 1 and variable 2.

print ("The result is: ", result) #Print the combined variable.
# ______________________________________________________________________________ 9 _____________________________________________________________________________________


# 10. Accept the following inputs from the user: Student Name, Age, City, Course Name, Marks in Subject 1, Marks in Subject 2, Marks in Subject 3. Store all values in appropriate variables and calculate the percent and print it. 

Name = input ("Student Name: ") #Take input from user name.

Age = int (input("Student Age: ")) #Take input from user age in Int type.

City = input ("Student City: ") #Take input from user City.

Course = input ("Student Course Name: ") #Take input from user course name.

sub1 = float(input("Student marks in Subject 1: ")) #Take the user's marks for the subject 1 as a float input.

sub2 = float(input("Student marks in Subject 2: "))#Take the user's marks for the subject 2 as a float input.

sub3 = float(input("Student marks in Subject 3: "))#Take the user's marks for the subject 3 as a float input.

total_marks = sub1 + sub2+ + sub3 # storing by adding all the subjects.

Cal = (total_marks / 300) * 100 # calculate the percentages of total marks.

print ("\n--- Student Report ---") #Print the Student report.

print("Student total marks is percentage obtained by: ", f"Stdent Name is {Name} and percentage is {Cal:.2f}%") #Print the student name and their obtained percentage marks.
# ___________________________________________________________________________ 10 ____________________________________________________________________________________________


# 11. Create a list named subjects containing: Python, SQL, Excel, Tableau Perform the following: a. Display the complete list  b. Display the first subject and the last subject  c. Add one new subject between Python and SQL. Display the updated list  d. Delete Excel from the list and display the updated list e. Copy the list into another list. f. Sort the new list in ascending order. g. Check if Excel is present in the list (use appropriate operator) 

subjects = ["Python", "SQL", "Excel", "Tableau"] # Storing all subjects in subject variable.

print ("All the Subjects are: ", subjects) # Print all the Subjects.   // Q : A //

print ("The First Subject is: ", subjects[0], ", And the last subject is: ", subjects[3]) #Display the First Subject and last subject.  // Q : B //

subjects.insert(1, "LINUX") #Add "LINUX" subject after Python and before SQL.

print ("After Insert one subject, The updated Subjects is: ", subjects) #Print the current updated subject after insertion.  // Q : C //

subjects.remove("Excel") # Remove "Excel" from the Subjects.

print("After remove one subject, The updated Subjects are: ", subjects) #Print the current updated subject after removed.  // Q : D //

My_subjects = subjects.copy() # Copy the all subjects into another list.  // Q : E //

My_subjects.sort() #Sorting the new list.

print ("After sorted new list is: ", My_subjects) #After soring new list , print the new list in ascending order.   // Q : F //

is_present = "Excel" in My_subjects #Here we checl the "Excel" subject is present in the current new list or not, OR Here 'in' is the most important Python operator that's called "Membership Operator".

print("Is 'Excel' subject present in the new list?: ", is_present) #it's diplay the bollean value, like if present display "TRUE" if not display "FALSE"    // Q : G
# ________________________________________________________________11 _____________________________________________________________________________________________________


# 12. Create the following variables: attendance = True assignment_submitted = False a. Which operator should be applied between these variables to get a True? b. Which operator should be applied between these variables to get a False? c. Which operator should be applied to ‘attendance’ to get a False? 

attendance = True # Take the given value in attendance.

assignment_submitted = False # Take the given another value in assignment_submitted.

print("--- Given Values ---") # display given values.
print("Attendance = ", attendance) # Display the value ot attendance.

print("Assignment = ", assignment_submitted) # Display the value ot assignment_submitted.

result_a = attendance or assignment_submitted # Here I use "OR" operator should be applied between these variables to get a True.

print ("Here the result using 'or' operator is: ", result_a) # Print the result using "OR" operator  // Q : A //.

result_b = attendance and assignment_submitted # Here I use "AND" operator should be applied between these variables to get a False.

print ("Here the result using 'and' operator is: ", result_b) # Print the result using "OR" operator  // Q : B //.

result_c = not attendance # Here I use "NOT" operator should be applied to ‘attendance’ to get a False.

print ("Here the result using 'NOT' operator is: ", result_c) # Print the result using "NOT" operator. Here, True becomes False and False becomes True.  // Q : C //.
# ________________________________________________________________12 _____________________________________________________________________________________________________




# ________________________________________________________________***END*** _____________________________________________________________________________________________________









