# 1. If a = 2 and we perform a += 3, what will be the value of a? 
# a. 2 
# b. 3 
# c. 4 
# d. 5 


a = 2
a += 3  # This is exactly equivalent to writing: a = a + 3
print("The value of 'a' is: ", a )

#Ans:- (D) 5
# ___________________________________________________________________________ 1 ____________________________________________________________________________________________

# 2. What is the result of print(False or True)? 
# a. False 
# b. True 
# c. None 

print ("The result is: ", True or False) # The 'or' operator returns True if at least one side is True.

#Ans:- (B) True
# ___________________________________________________________________________ 2 ____________________________________________________________________________________________


# 3. What is the output of print(not True)? 
# a. True 
# b. False 
# c. None 

print ("The result is: ", not True) #The 'not' operator inverts the boolean value means 'True' is 'False' and 'False' is 'True'

#Ans:- (B) False
# ___________________________________________________________________________ 3 ____________________________________________________________________________________________


# 4. If x = 1 and y = 2, what will print(x & y) return? 
# a. 0 
# b. 1 
# c. 2 
# d. 3 

x = 1
y = 2
print ("The final value is: ", x & y)  #The '&' is the Bitwise AND operator. It compares numbers bit-by-bit in binary:, 1 in binary is 01, 2 in binary is 10, 01 AND 10 results in 00 (which is 0)

#Ans:- (A) 0
# ___________________________________________________________________________ 4 ____________________________________________________________________________________________


# 5. If x = 1 and y = 2, what will print(x | y) return? 
# a. 0 
# b. 1 
# c. 2 
# d. 3 

x = 1
y = 2

print ("The final value is: ", x | y)# The '|' is the Bitwise OR operator. 01 OR 10 results in 11 (which is 3 in binary)

#Ans:- (D) 3
# ___________________________________________________________________________ 5 ____________________________________________________________________________________________


# 6. What will print('a' in 'apple') return? 
# a. False 
# b. True 
# c. ‘a’ 
# d. None 

print ("To check the result", 'a' in 'apple')#The 'in' is a membership operator that checks if a substring exists inside a string.

#Ans:- (B) True 
# ___________________________________________________________________________ 6 ____________________________________________________________________________________________


# 7. What happens if the condition in an if...else statement is False? 
# a. If  block is executed 
# b. Else block is executed 
# c. Program terminates 
# d. Error 

condition = False
if condition:
    print("If block is executed") #This is executed if the condition will True
else :
    print("Else block is executed") #This is executed because the condition was False 

#Ans:- (B) Else block is executed
# ___________________________________________________________________________ 7 ____________________________________________________________________________________________


# 8. A while loop continues executing as long as: 
# a. The condition evaluates to True 
# b. The loop variable reaches 0 
# c. The break statement is encountered 
# d. An error occurs 

count = 1
while count <= 5:
    print ("While loop running and the Count is: ", count)
    count += 1 # Increments to eventually make the loop condition False

#Ans:- (A) The condition evaluates to True 
# ___________________________________________________________________________ 8 ____________________________________________________________________________________________


# 9. What does range(5) produce? 
# a. 0 to 5 
# b. 1 to 5 
# c. 0 to 4 
# d. Nothing 

print("range(5) produces numbers:", list(range(5))) # The range(n) counts from 0 up to, but NOT including, n.

#Ans:- (C)0 to 4
# ___________________________________________________________________________9 ____________________________________________________________________________________________


# 0. Which of the following generates numbers from 10 to 1? 
# a. range(1,10,1) 
# b. range(10,1,-1) 
# c. range(10,0,1) 
# d. range(10,0,-1) 

print("Countdown 10 to 1:", list(range(10, 0, -1))) # range is start, stop, step. To go backwards, use a negative step (-1). It stops 1 number before the stop value (stops at 1, right before 0).

#Ans:- (D)range(10,0,-1)
# ___________________________________________________________________________10 ____________________________________________________________________________________________


# 11. What causes a while loop to become an infinite loop? 
# a. Using a for loop inside it 
# b. Condition always evaluates to True and no update to exit the condition 
# c. Using break inside the loop 
# d. Using continue inside the loop 

#Ans:- (B)Condition always evaluates to True and no update to exit the condition // (Setting a loop condition directly to 'True' creates an infinite loop.)
# ___________________________________________________________________________11 ____________________________________________________________________________________________


# 12. What is the function of the break statement? 
# a. Skips the current iteration 
# b. Restarts the loop 
# c. Exits the program 
# d. Exits the loop 

while True:
    print("Inside an infinite loop loop, but breaking out instantly...") #QNA = 11
    break  # Here 'break' statement use because we need to Exits the loop safely
print("Successfully exited loop via 'break'.") #QNA = 12

#Ans:- (D)Exits the loop
# ___________________________________________________________________________12 ____________________________________________________________________________________________


# 13. Where is pass statement commonly used? 
# a. To terminate the loop 
# b. To terminate the program 
# c. To skip the iteration 
# d. As a placeholder in empty block 

if True:
    pass  # The 'pass' does nothis . It's just placeholder, it's fill empty spaces.
print("'pass' executed seamlessly.")

#Ans:- (D)As a placeholder in empty block
# ___________________________________________________________________________13 ____________________________________________________________________________________________


# 14. Which operator is used to repeat a string in Python? 
# a. + 
# b. & 
# c. | 
# d. * 

print("String repetition :", "Arip" * 3)  # Output: AripAripArip

#Ans:- (D)*
# ___________________________________________________________________________14 ____________________________________________________________________________________________


# 15. How can you check if a substring exists within a string in Python? 
# a. substring() method 
# b. find() method 
# c. contains method 
# d. exists() method 

text = "Hello world"
print("Index of 'world':", text.find("world"))  # Output: 6 (found it's start from index 6)

#Ans:- (B)find() method 
# ___________________________________________________________________________15 ____________________________________________________________________________________________


# 16. Which of the following methods checks if a string contains only numbers 0-9? 
# a. isnum() 
# b. isalpha() 
# c. isalnum() 
# d. isdigit() 

print("'1234': ", "1234".isdigit())  # True . Because All digits under 0 - 9.
print("'123a': ", "123a".isdigit())  # False . Because All digits are not under 0 - 9.

#Ans:- (D)isdigit()
# ___________________________________________________________________________16 ____________________________________________________________________________________________


# 17. Which code creates an empty list? 
# a. empty() 
# b. {} 
# c. list.empty() 
# d. [] 

empty_list = []
print("Empty list created:", empty_list) #It's created empty list.

#Ans:- (D)[]
# ___________________________________________________________________________17 ____________________________________________________________________________________________


# 18. What does the slice marks[:3] return? 
# marks = [78, 87, 66, 98, 56, 81, 91] 
# a. [78, 87, 66, 98] 
# b. [98,56,81] 
# c. [56,81,91] 
# d. [78,87,66] 

marks = [78, 87, 66, 98, 56, 81, 91]
print("Slice marks:", marks[:3])  # Slicing [:3] grabs everything from the beginning up to index 3 (excluding 3). Indexes 0, 1, 2 -> [78, 87, 66] 

#Ans:- (D)[78,87,66]
# ___________________________________________________________________________18 ____________________________________________________________________________________________


# 19. How can you change the second element of a list x to 8? 
# a. x.update(1, 8) 
# b. x[1] = 8 
# c. x[2] = 8 
# d. x.set(1, 8) 

x_list = [10, 20, 30]
x_list[1] = 8
print("Updated list x_list:", x_list)  #  Indexing starts at 0, so the second element was 20 but after updating the second element at index 1.Output: [10, 8, 30].

#Ans:- (B) x[1] = 8 
# ___________________________________________________________________________19 ____________________________________________________________________________________________


# 20. Which statement deletes the first element of a list x? 
# a. x.remove(0) 
# b. x.delete(0) 
# c. x.pop(0) 
# d. x.discard(0) 

del_list = [100, 200, 300]
del_list.pop(0)
print("List after delete:", del_list)  # '.pop(0)' removes and returns the element at index 0. Output: [200, 300]

#Ans:- (C) x.pop(0) 
# ___________________________________________________________________________20 ____________________________________________________________________________________________


# 21. Which function finds the largest element in list x? 
# a. maximum(x) 
# b. largest(x) 
# c. max(x) 
# d. large(x) 

num_list = [5, 45, 12, 99, 3]
print("Largest element using max():", max(num_list))  # We use 'max' function to find largest element . Output: 99

#Ans:- (C) max(x)
# ___________________________________________________________________________21 ____________________________________________________________________________________________


# 22. If b = [10,20,[80,90]], how do you access 90? 
# a. b[3][2] 
# b. b[1][2] 
# c. b[-1][-1] 
# d. b[3][1] 

b = [10, 20, [80, 90]]
print("Accessing 90 via b:", b[-1][-1]) # Negative index -1 targets the last element. b[-1] fetches the sublist [80, 90]. b[-1][-1] fetches the last element of that sublist, which is 90.

 #Ans:- (C) b[-1][-1]
 # ___________________________________________________________________________22 ____________________________________________________________________________________________


# 23. If dict1 = {'name': 'Chandra', 'id': 200}, how do you access the value 200? 
# a. dict1.get(200) 
# b. dict1.value(‘id’) 
# c. dict1[1] 
# d. dict1.get(‘id’) 

dict1 = {'name': 'Chandra', 'id': 200}
print("Accessing value of 'id':", dict1.get('id'))  # Use '.get('key')' or dict['key'] to pull data associated with a key label.Output: 200
 
 #Ans:- (D) dict1.get(‘id’)
  # ___________________________________________________________________________23 ____________________________________________________________________________________________


# 24. Which statement correctly adds a new key 'Dept' with value 'Finance' to dictionary dict1? 
# a. dict1.add(‘Dept’, ‘Finance’) 
# b. dict1.insert({‘Dept’: ‘Finance’}) 
# c. dict1.update({‘Dept’: ‘Finance’}) 
# d. dict1.extend({‘Dept’: ‘Finance’}) 

dict1.update({'Dept': 'Finance'})
print("Updated dictionary:", dict1) #Before dict1 have name and id and after adding dept by using dict1.update the update list is name , id and dept.

#Ans:- (C) dict1.update({‘Dept’: ‘Finance’}) 
 # ___________________________________________________________________________24 ____________________________________________________________________________________________


#  25. What happens if a duplicate key is added to a dictionary? 
# a. Both values are stored 
# b. Error 
# c. No change 
# d. Old value gets replaces with new value

dup_dict = {'key': '10'}#Old value
dup_dict['key'] = '20'#New Value
print("Dictionary with duplicate key added:", dup_dict)  # Output: {'key': 'new_value'}

#Ans:- (D) Old value gets replaces with new value
 # ___________________________________________________________________________25 ____________________________________________________________________________________________


# 26. If d = {'a': 1} then what does d.get('b', 0) return? 
# a. 1 
# b. None 
# c. Error 
# d. 0 

d = {'a': 1}
print("Result of d: ", d.get('b', 0))  # .get(key, default) returns the default value (0) if the key doesn't exist. Output: 0

#Ans:- (D) 0
# ___________________________________________________________________________26 ____________________________________________________________________________________________


# 27. What does the items() method return? 
# a. Keys only 
# b. Values only 
# c. Key-value pairs as tuples in dict_items 
# d. Key-value pairs as list in dict_items 

print("Items format view: ", list(d.items()))  # It outputs key-value pairs wrapped cleanly inside tuples. Output: [('a', 1)]

#Ans:- (C) Key-value pairs as tuples in dict_items 
# ___________________________________________________________________________27 ____________________________________________________________________________________________


# 28. If for k in d: is used on a dictionary d, what does k represent? 
# a. Keys 
# b. Values 
# c. Both keys and values 
# d. Indexes 

for k in d:
    print("k represents the key name: ", k)  # Looping directly over a dictionary defaults to extracting its keys. Output: a

#Ans:- (A) Keys
# ___________________________________________________________________________28 ____________________________________________________________________________________________


# 29. Which of the following statements about Python sets is TRUE? 
# a. Allows duplicate elements 
# b. Immutable 
# c. Supports indexing 
# d. Unordered with no duplicates 

X = {1, 2, 2, 3}
print("Sets remove duplicates automatically:", X) # Sets are completely unordered and reject duplicate values. Output: {1, 2, 3}

#Ans:- (D) Unordered with no duplicates
# ___________________________________________________________________________29 ____________________________________________________________________________________________


# 30. What does the difference A - B return for two sets A and B? 
# a. Common elements of A and B 
# b. Elements in A, but not in B 
# c. Elements in B, but not in A 
# d. All elements of A and B

A = {1, 2, 3}
B = {3, 4, 5}
print("Difference (A - B):", A - B)  # It returns a new set containing items that are in set A, but NOT in set B. Output: {1, 2}. and when we do '(B - A)' It's Output: {4, 5}

#Ans:- (B) Elements in A, but not in B 
# ___________________________________________________________________________30 ____________________________________________________________________________________________


# 31. Which of the following statements about frozensets is False? 
# a. Mutable 
# b. Duplicates not allowed 
# c. No indexing 
# d. Cannot use add(), remove(), discard() 

f = frozenset([1, 2, 3])
print("Frozenset representation:", f) #Output: frozenset({1, 2, 3}). So, Based on question Frozensets are IMMUTABLE. The statement saying they are "Mutable" is false.

#Ans:- (A) Mutable 
# ___________________________________________________________________________31 ____________________________________________________________________________________________


# 32. Which datatype can be an element of a set? 
# a. List 
# b. Dict 
# c. Set 
# d. String 

valid_set = {"This works fine", 10, 5.5}
print("Valid set containing a string element:", valid_set) #Set elements must be hashable/immutable (like integers, floats, or strings). Lists, sets, and dictionaries cannot be elements inside a set because they are mutable.


#Ans:- (D) String
# ___________________________________________________________________________32 ____________________________________________________________________________________________


# 33. Find all the indexes of 'p' in the given string,  
# s1 = ‘practice is important to perfectly learn python’. 
# Output should be in a list. => [0, 14, 25, 41] 

s1 = 'practice is important to perfectly learn python' #s1 holds our text string
indexs = [] # creates a completely empty list. This is our "basket" where we will collect the index numbers whenever we find a letter 'p'
for index in range(len(s1)): #len(s1) counts the total number of characters in the string. It's start counting number from 0- (n-1). The for loop runs n times. Every time it runs, the variable index updates to the next number (0, then 1, then 2, then 3, etc.).
    if s1[index] == 'p': #s1[index] means: "Go look at the character sitting at this specific tracking position."
        indexs.append(index) #When index is 0, for example: s1[0] is 'p'. The condition matches, so it runs indexes.append(0), adding 0 to our list. and after that again run When index is 1, s1[1] is 'r'. It doesn't match, so the loop ignores it and moves on.This keeps scanning character-by-character until it hits position 14, 25, and 41, dropping those numbers into our basket too.
print("All indexs position of 'p' in the given Strings are: ", indexs)  # Once the loop finishes checking all 48 positions, it prints out the list containing only the position numbers where a 'p' was found. Output: [0, 14, 25, 41]

# ___________________________________________________________________________33 ____________________________________________________________________________________________


# 34. Given a list of strings, write a Python program that counts how many strings in the list 
# have a length greater than 2 and are palindromes. Use  slicing to perform the palindrome 
# check. A palindrome is a string that reads the same forwards and backwards, for example, 
# "aba" or "1991"

my_list = ["aba", "xyz", "1991", "a", "python"] #create some list of strings
count = 0 # Start a counter at 0
for item in my_list: #Loop through each item in the list one by one
    if len(item) > 2 and item == item[::-1]: #Here is two condition given. Check two conditions at the same time. Condition A: Is the length of the string greater than 2?. Condition B: Is the original string equal to its reversed version?
        count += 1  # If both are true, add 1 to our counter
print("Count of palindromes:", count)#Print the final total

# ___________________________________________________________________________34 ____________________________________________________________________________________________


# 35. Write a Python program that produces a list of all words with length greater than or equal 
# to 4 and starts with ‘w’ or ‘W’ from a string. NOTE: Keep only unique words. 
# Example: 
# s1 = “How much wood would a woodchuck chuck if a Woodcutter could chuck wood to 
# build a wooden house to woo his wife” 
# output => [“wood”, “would”, “woodchuck”, “Woodcutter”, “wooden”, “wife”] 

s1 = "How much wood would a woodchuck chuck if a Woodcutter could chuck wood to build a wooden house to woo his wife" 
raw_words = s1.split() #The .split() method takes the entire long string and cuts it up wherever there is a space. It creates a list of individual words that looks like this:['How', 'much', 'wood',....]
unique_words = []
for word in raw_words: #The for loop picks up each word from the list, one by one.
    cleaned_word = word.strip(",.?!") #The .strip(",.?!") function removes any punctuation marks stuck to the edges of the word (like commas or periods) so they don't mess up our matching logic.
    if len(cleaned_word) >= 4 and cleaned_word.lower().startswith('w'):  #Here is also two condition 1 is The word must have 4 or more letters.  Another is The word must start with the letter 'w' or 'W'. We use .lower() to temporarily turn the word into lowercase so that it catches both lowercase 'w' and uppercase 'W'.
        if cleaned_word not in unique_words: #This rule prevents duplicates to keep the collection unique. It checks our final list basket (unique_words) and asks: "Have we already saved this exact word pr not?"
            unique_words.append(cleaned_word) #If not saved or The first time the machine sees "wood", it saves it. otherwise The next time it sees "wood", this check returns False because it's already in the basket, so it skips it!
print( "Finally total unique word is: ", unique_words) #Every word that passes all three tests gets dropped into unique_words via .append(). Once the entire sentence is evaluated, it prints the clean collection.

# ___________________________________________________________________________35 ____________________________________________________________________________________________


# 36. WAP that reads a single string from user and outputs a dictionary showing how many 
# times each character appears in the string. 
# Example: s1 = “google.com”, Output => {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1} 
# Hints:  
#  Initialize an empty dictionary 
#  Iterate over each character in the input string.  
#  For each character, update its count in the dictionary if the character exists OR 
# add the character as key and its value as 1 

user_input = input("Enter a string: ")  #captures the text type from users.
char_counts = {} #creates a completely empty dictionary.
for char in user_input: #The for loop grabs every single character in one by one, from left to right.
    if char in char_counts:
        char_counts[char] += 1 #The if block "If we have already seen this character before, add 1 to its current count."
    else:
        char_counts[char] = 1 # The else block "If this is the very first time we are seeing this character, write it down on the sheet and give it a starting count of 1."
        print("Total number characyers are: ", char_counts) #Once the loop finishes checking the final letter, it prints the complete.

# ___________________________________________________________________________36 ____________________________________________________________________________________________


# 37. From a dictionary of products, display the product which is the costliest. 
# products = {‘soap’: 50, ‘oil’: 200, ‘laptop’: 60000, ‘phone’: 25000, ‘mouse’: 500} 
# Output => Costliest product is laptop. 

products = {'soap': 50, 'oil': 200, 'laptop': 60000, 'phone': 25000, 'mouse': 500} #This stores your inventory items as keys and their prices as values.
MaxPrice_Item = max(products, key=products.get) #Here ".get"  use for it looks up the value and returns their prices and or "max()" function use because we need in between those items fetch the costly items.
print("Costliest product is: " ,MaxPrice_Item )  # Output: Costliest product is laptop.

# ___________________________________________________________________________37 ____________________________________________________________________________________________


# 38. Given a Python dictionary d and a list of keys keys_to_remove, remove all specified keys 
# from d and print the resulting dictionary. 
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New york'} 
# keys_to_remove = ['name', 'salary'] 
# Output => {'age': 25, 'city': 'New york'}

d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New york'} #containing four key-value pairs.
keys_to_remove = ['name', 'salary'] #A list containing the specific keys we want to delete from that dictionary.
for key in keys_to_remove:  #This loops through the list of targeted keys one by one. First, key will be 'name', and in the next iteration, it will be 'salary'.
    if key in d:#It looks inside the dictionary d to see if the current key actually exists. If it does, it moves to the next line. If it doesn't, it skips it
        d.pop(key) #The ".pop" method removes the specified key and its associated value from the dictionary.
print(d)  # Output: {'age': 25, 'city': 'New york'} 

# ___________________________________________________________________________38 ____________________________________________________________________________________________


# 39. Write a Python program that takes an integer as input and counts down from that number 
# to 0. Use a while loop and if-else statements to print a message at 0 (e.g., "Blast!"). 

countdown_start = int(input("Enter starting number for countdown: ")) #the user to type an Integer number in the console.
while countdown_start >= 0: #Here, the loop will keep executing its internal code as long as countdown_start is greater than or equal to 0.
    if countdown_start == 0:
        print("Blast!") #If the number has reached 0: The program skips printing the number and instead prints "Blast!".
        break
    else:
        print("Your current possition is: ", countdown_start) #otherwise if the number is greater than 0: The program goes to the else block and prints the current number.
        countdown_start -= 1 #If else statement work after printing number the coundown start number will be substract by 1.

# ___________________________________________________________________________39 ____________________________________________________________________________________________


# 40. Write a Python program that continuously takes a student's marks (0-100) as input and 
# prints the grade using if–elif–else according to the following rules: 
# Marks range 
# 90-100 
# Grade 
# 80-89 
# A+ 
# A 
# 70-79 
# 60-69 
# B 
# C 
# 50-59 
# Below 50 
# D 
# Fail 
# Ask the user if they want to continue. If they say “yes”, keep asking the user for marks 
# and print the respective grade. If the user says “no”, print a “Thank you” message and 
# stops the program. 
# Sample output: 
# Welcome to the grade checker program! 
# Enter your marks (0-100): 85.5 
# Your grade is A 
# Do you want to check the grade for another marks?: yes 
# Enter your marks (0-100): 79.0 
# Your grade is B 
# Do you want to check the grade for another marks?: yes 
# Enter your marks (0-100): 45 
# Your grade is Fail.

print("Welcome to the grade checker program!") #Here we print for grettings.
while True: #Starting while loops when it's true
    marks = float(input("Enter your marks (0-100): ")) #taking marks between (0-100) in decimal value from users input.
    if marks >= 90 and marks <= 100: #Start evaluating marks from grading system .
        grade = "A+" 
    elif marks >= 80: 
        grade = "A" 
    elif marks >= 70: 
        grade = "B" 
    elif marks >= 60: 
        grade = "C" 
    elif marks >= 50: 
        grade = "D" 
    else:
        grade = "Fail" 
        print("Your grade is: ", grade) #Display grading system according to give =n marks value from users.
    user_choice = input("Do you want to check the grade for another marks? (yes/no): ").lower() #Here again users have two choice they wanna check another marks or not.  And ".lower()" use for user type 'Yes or No' that types consider always lowercase.
    if user_choice != "yes": #If users select yes the loop start running for checking another grades.
        print("Thank you for checking our grading system!") #If user select no, so they exit the loop and print Thank you.
        break 

# ___________________________________________________________________________40 ____________________________________________________________________________________________


# 41. You are given a number a and you have to print your answer according to the following:  
#  If the number is divisible by 3, you print "Fizz" 
#  If the number is divisible by 5, you print "Buzz" 
#  If the number is divisible by both 3 and 5, you print "FizzBuzz" 
#  In any other case, you print the number itself 

num = int(input("Enter a number: ")) #Taking an Integer number from users
if num % 3 == 0 and num % 5 == 0: #If the number divisible by 3 & 5 both so print "FizzBuzz"
    print("FizzBuzz") 
elif num % 3 == 0: #If the number divisible by 3 so print "Fizz"
    print("Fizz") 
elif num % 5 == 0: #If the number divisible by 5 both so print "Buzz"
    print("Buzz") 
else:
    print("This is not divisible by 3 or 5", num) #If the number not divisible by 3 and 5 so print as same number .

# ___________________________________________________________________________41 ____________________________________________________________________________________________


# 42. WAP to create a password authentication system. Store a password in a variable. Ask for 
# a password from the user. Allow the user 3 attempts to enter the password. If user enters 
# wrong password 3 times, print “Access denied”. If the user enters correct password 
# within 3 attempts, print “Access granted” and break early. 

Secret_Password = "Hacker101" #The correct password stored in the system.
attempts = 3 #The user have 3 attempts only
while attempts > 0: #If attempts greater than 0
    user_pass = input("Enter password: ") #User enter the password .
    if user_pass == Secret_Password: #If the password is correct
        print("Congraculation You guess the secret password Access granted") # User successfully break the password
        break 
    else: #If user input wrong password
        attempts -= 1 #The attempt will be substract by 1 or user lost 1 chance.
        if attempts > 0: # Now users have 2 attempts if they lost one more attempts.
            print(f"Wrong password. You have {attempts} attempts left.") #users display alert shows that they have last one chance left.
        else:
            print("Sorry You can't break this secret password, Access denied") #If they lost user shows "access denied".

 # ___________________________________________________________________________42 ____________________________________________________________________________________________


# 43. Write a Python program to create a Simple Coin Toss Game.  
# Requirements:  
#  Display a welcome message to the user.  
#  Ask the user to guess either "heads" or "tails".  
#  Validate the input: If the user enters anything other than "heads" or "tails", show 
# an error message and ask again.  
#  Use the random module to simulate a coin toss: Randomly choose between 
# "heads" and "tails".  
#  Display the result of the coin toss.  
#  Check whether the user’s guess matches the coin toss result:  
# o If yes → print a success message (e.g., “You guessed it right!”)  
# o If no → print a failure message (e.g., “Wrong guess!”)  
#  Ask the user if they want to play again:  
# o If the user types "yes", repeat the game.  
# o If the user types "no", display a goodbye message and stop the game.  
#  The program must use a while loop.  
# Sample Output: 
# Welcome to the Simple Coin Toss Game! 
# Guess 'heads' or 'tails': heads 
# Coin shows: tails 
# Wrong guess!  
# Do you want to play again? (yes/no): yes 
# Guess 'heads' or 'tails': tails 
# Coin shows: tails 
# You guessed it right!  
# Do you want to play again? (yes/no): no  
# Thanks for playing!

import random #Imports Python’s built-in module for generating random selections.
print("Welcome to the Simple Coin Toss Game!") 
options = ["heads", "tails"] #A list containing the two possible outcomes of a coin flip.
while True: #This creates an infinite loop (while True). The game will keep running over and over until it hits a break statement.
    user_guess = input("Guess 'heads' or 'tails': ").lower().strip() #Users have to choose two options head or tail . And .lower().strip() use to converts the input to lowercase and removes any accidental spaces
    while user_guess not in options: #This is an inner loop. If the user types something invalid type without head or tail, the condition is True. The program will print an error message and demand input again, trapping the user until they type exactly "heads" or "tails".
        print("Invalid input! Try again.") 
        user_guess = input("Guess 'heads' or 'tails': ").lower().strip() 
    coin_result = random.choice(options) #randomly picks either "heads" or "tails" from your list with a 50/50 chance.
    print("Coin shows: ", coin_result) 
    if user_guess == coin_result: #If the user guess correct so user guess right.
        print("You guessed it right!") 
    else: 
        print("Wrong guess!")    #If the user guess wrong so user guess wrong.
    replay = input("Do you want to play again? (yes/no): ").lower().strip() #Here again users have two choice they wanna check another marks or not. And .lower().strip() use to converts the input to lowercase and removes any accidental spaces
    if replay != "yes": #If users select yes the loop start running for checking another play game.
        print("Thanks for playing!") #If user select no, so they exit the loop and print Thank you.
        break 

print("\n==============================================================================")
print("Assignment 2 main file demonstration completed!")
print("==============================================================================")

 # ___________________________________________________________________________43 ____________________________________________________________________________________________

<<<<<<< HEAD
# ________________________________________________________________***END*** _____________________________________________________________________________________________________

=======

# ________________________________________________________________***END*** _____________________________________________________________________________________________________
>>>>>>> 8662a90 (Updated README repository structure catalog)
