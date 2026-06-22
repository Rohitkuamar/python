print("Namastey Python, We are learning")
# comments and variables
""" lets see this
        as a comment
"""
# variables Example
Name = "Rohit"
name = "mohit"
print(Name)
print(name)
print(Name + " " + name)

# data types Example
a=10
b=20.0  
c=12/3  # if its in p/q, it will be in float
d=34j # complex number
e="Rohit"
f=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(name))

# String and type conversion
A = "A"
print(ord(A)) # it will give the unicode of A  = char to unicode
print(chr(65)) # it will give the character of unicode 65 = unicode to char
print(str(a)) # it will convert a to string


a= "hello brothers"

# Indexing and slicing

print(a[0]) # it will give the first character of the string
print(a[1]) # it will give the second character of the string

print(a[-1]) # it will give the last character of the string
print(a[-2]) # it will give the second last character of the string

print(a[0:5]) # it will give the first 5 characters of the string
print(a[6:14]) # it will give the characters from index 6 to index 12
print(a[:5]) # it will give the first 5 characters of the string

# Slice with step
print(a[0:14:2]) # it will give the characters from index 0 to index 14 with a step of 2
print(a[0:14:3]) # it will give the characters from index 0 to index 14 with a step of 3
print(a[::]) # it will give the whole string
print(a[::2]) # it will give the characters from index 0 to index 14 with a step of 2

# type conversion

a=12
print(str(a)) # it will convert a to string
b="12"  
print(int(b)) # it will convert b to integer
c="12.5"    
print(float(c)) # it will convert c to float
d=12.5      
print(int(d)) # it will convert d to integer

# Input and Output

# name = input("Enter your name: ") # it will take input from the user and store it in the variable name
# print("Hello " + name) # it will print Hello and the name entered by the user
# age = int(input("Enter your age: ")) # it will take input from the user and convert it to integer and store it in the variable age
# print("Your age is " + str(age)) # it will print Your age is and the age entered by the user
# print(f"Hello my name is {name} and my age is {age}") 

# Operators
a=20
b=10
print(a+b) # it will give the sum of a and b
print(a-b) # it will give the difference of a and b
print(a*b) # it will give the product of a and b
print(a/b) # it will give the quotient of a and b
print(a//b) # it will give the floor division of a and b
print(a%b) # it will give the remainder of a and b
print(a**b) # it will give the power of a to b

# Assignment Operators
a=10
a+=5 # it will add 5 to a and assign the result to a
print(a) # it will print the value of a
a-=5 # it will subtract 5 from a and assign the result to a
print(a) # it will print the value of a
a*=5 # it will multiply a by 5 and assign the result to a
print(a) # it will print the value of a
a/=5 # it will divide a by 5 and assign the result to a
print(a) # it will print the value of a
a//=5 # it will floor divide a by 5 and assign the result to a
print(a) # it will print the value of a
a%=5 # it will take the modulus of a by 5 and assign the result to a
print(a) # it will print the value of a
a**=5 # it will take the power of a to 5 and assign the result
print(a) # it will print the value of a

# comparison operators
a=10
b=20
print(a==b) # it will check if a is equal to b and return True or False
print(a!=b) # it will check if a is not equal to b and return True
print(a> b) # it will check if a is greater than b and return True or False
print(a< b) # it will check if a is less than b and return True or
print(a>=b) # it will check if a is greater than or equal to b and return True or False
print(a<=b) # it will check if a is less than or equal to b and
print(a is b) # it will check if a and b are the same object in memory and return True or False
print(a is not b) # it will check if a and b are not the same object in memory and return True or False

# Logical Operators
a=10
b=20
print(a>5 and b>15) # it will check if a is greater than 5 and b is greater than 15 and return True or False
print(a>5 or b>15) # it will check if a is greater than 5 or b is greater than 15 and return True or False
print(not(a>5 and b>15)) # it will check if a is not greater than 5 and b is not greater than 15 and return True or False

# Membership Operators
a="Hello World"
print("Hello" in a) # it will check if "Hello" is present in a and return True or False
print("hello" in a) # it will check if "hello" is present in a and return True or False
print("World" not in a) # it will check if "World" is not present in a and return True or False

# Conditional Statements
a=10
if a>0:
    print("a is positive")      
elif a<0:
    print("a is negative")  
else:
    print("a is zero")

                
 # nested if statements
a=10
if a>0:
    print("a is positive")
    if a%2==0:
        print("a is even")
    else:
        print("a is odd")
elif a<0:
    print("a is negative")
else:
    print("a is zero")
        
# For Loop
for i in range(5): # it will iterate from 0 to 4
    print(i) # it will print the value of i
for i in range(1, 11): # it will iterate from 1 to 10
    print(i) # it will print the value of i
for i in range(1, 11, 2): # it will iterate from 1 to 10 with a step of 2
    print(i) # it will print the value of i
    
a= "Nature"
for i in a: # it will iterate through each character in the string a
    print(i) # it will print the value of i

#factorial of a number using for loop
num = 5
factorial = 1
for i in range(1, num+1): # it will iterate from 1 to num
    factorial *= i # it will multiply factorial by i and assign the result to factorial
print(f"The factorial of {num} is {factorial}") # it will print the factorial of num

    
# While Loop
i=0
while i<5: # it will iterate until i is less than 5
    print(i) # it will print the value of i
    i+=1 # it will increment the value of i by 1    
    

# Functions  
def greet(name): # it will define a function named greet that takes a parameter name
    print(f"Hello {name}") # it will print Hello and the value of name
    
greet("Rohit") # it will call the function greet and pass "Rohit" as an argument

def add(a, b): # it will define a function named add that takes two parameters a and b
    return a + b # it will return the sum of a and b
result = add(10, 20) # it will call the function add and pass 10 and 20 as arguments and store the result in the variable result
print(f"The sum of 10 and 20 is {result}") # it will print the sum of 10 and 20

def factorial(n): # it will define a function named factorial that takes a parameter n
    if n == 0: # it will check if n is equal to 0
        return 1 # it will return 1 if n is equal to 0
    else:
        return n * factorial(n-1) # it will return n multiplied by the factorial of n-1 if n is not equal to 0
num = 5
result = factorial(num) # it will call the function factorial and pass num as an argument and store the result in the variable result
print(f"The factorial of {num} is {result}") # it will print the factorial of num


# Data Structures
# List
my_list = [1, 2, 3, 4, 5] # it will create a list named my_list with the values 1, 2, 3, 4, and 5
print(my_list) # it will print the value of my_list
my_list.append(6) # it will add the value 6 to the end of my_list
print(my_list) # it will print the value of my_list
my_list.insert(0, 0) # it will insert the value 0 at index 0 in my_list
print(my_list) # it will print the value of my_list
my_list.remove(3) # it will remove the value 3 from my_list
print(my_list) # it will print the value of my_list
my_list.pop() # it will remove the last value from my_list
print(my_list) # it will print the value of my_list
my_list.pop(0) # it will remove the value at index 0 from my_list
print(my_list) # it will print the value of my_list
my_list.extend([7, 8, 9]) # it will add the values 7, 8, and 9 to the end of my_list
print(my_list) # it will print the value of my_list
my_list.sort() # it will sort the values in my_list in ascending order
print(my_list) # it will print the value of my_list
my_list.reverse() # it will reverse the order of the values in my_list
print(my_list) # it will print the value of my_list
my_list.clear() # it will remove all the values from my_list
print(my_list) # it will print the value of my_list

# Print positive and negative elements of an List
my_list = [1, -2, 3, -4, 5] # it will create a list named my_list with the values 1, -2, 3, -4, and 5
positive_list = [] # it will create an empty list named positive_list
negative_list = [] # it will create an empty list named negative_list
for i in my_list: # it will iterate through each value in my_list
    if i > 0: # it will check if the value is greater than 0
        positive_list.append(i) # it will add the value to positive_list if it is greater than 0
    elif i < 0: # it will check if the value is less than 0
        negative_list.append(i) # it will add the value to negative_list if it is less than 0
print(f"Positive elements in the list: {positive_list}") # it will print the positive elements in the list
print(f"Negative elements in the list: {negative_list}") # it will print the negative elements in the list

# Find the greatest element and print its index too
my_list = [1, 2, 3, 4, 5] # it will create a list named my_list with the values 1, 2, 3, 4, and 5
max_value = max(my_list) # it will find the greatest value in my_list and store it in the variable max_value
max_index = my_list.index(max_value) # it will find the index of the greatest value in my_list and store it in the variable max_index
print(f"The greatest element in the list is {max_value} and its index is {max_index}") # it will print the greatest element in the list and its index

# Find the second greatest element without removeing the greatest element
my_list = [1, 2, 3, 4, 5] # it will create a list named my_list with the values 1, 2, 3, 4, and 5
max_value = max(my_list) # it will find the greatest value in my_list and store it in the variable max_value
second_max_value = float('-inf') # it will initialize second_max_value to negative infinity
for i in my_list: # it will iterate through each value in my_list
    if i > second_max_value and i < max_value: # it will check if the value is greater than second_max_value and less than max_value
        second_max_value = i # it will update second_max_value with the value if it meets the conditions
print(f"The second greatest element in the list is {second_max_value}") # it will print the second greatest element in the list     

# Tuple
my_tuple = (1, 2, 3, 4, 5) # it will create a tuple named my_tuple with the values 1, 2, 3, 4, and 5
print(my_tuple) # it will print the value of my_tuple
print(my_tuple[0]) # it will print the first value of my_tuple
print(my_tuple[1]) # it will print the second value of my_tuple
print(my_tuple[-1]) # it will print the last value of my_tuple
print(my_tuple[-2]) # it will print the second last value of my_tuple
print(my_tuple[0:3]) # it will print the first three values of my_tuple
print(my_tuple[::2]) # it will print the values of my_tuple with a step


# Set
my_set = {1, 2, 3, 4, 5} # it will create a set named my_set with the values 1, 2, 3, 4, and 5
print(my_set) # it will print the value of my_set
my_set.add(6) # it will add the value 6 to my_set
print(my_set) # it will print the value of my_set
my_set.remove(3) # it will remove the value 3 from my_set
print(my_set) # it will print the value of my_set
my_set.discard(4) # it will remove the value 4 from my_set if it is present, otherwise it will do nothing
print(my_set) # it will print the value of my_set
my_set.pop() # it will remove and return an arbitrary value from my_set
print(my_set) # it will print the value of my_set
my_set.clear() # it will remove all the values from my_set
print(my_set) # it will print the value of my_set


# Dictionary
my_dict = {"name": "Rohit", "age": 25, "city": "Delhi"} # it will create a dictionary named my_dict with the keys "name", "age", and "city" and their corresponding values
print(my_dict) # it will print the value of my_dict
print(my_dict["name"]) # it will print the value of the key "name" in my_dict
print(my_dict["age"]) # it will print the value of the key "age" in my_dict
print(my_dict["city"]) # it will print the value of the key "city" in my_dict
my_dict["name"] = "Mohit" # it will update the value of the key "name" in my_dict to "Mohit"
print(my_dict) # it will print the value of my_dict


  
# Exception Handling

a= int(input("Enter a number: ")) # it will take input from the user and convert it to an integer and store it in the variable a
try: # it will try to execute the code inside the block
    x = 10 / a # it will raise a ZeroDivisionError
except ZeroDivisionError: # it will catch the ZeroDivisionError and execute the code inside the block
    print("You cannot divide by zero") # it will print a message indicating that division by zero is not allowed
    x = 0 # it will set x to 0
print(x) # it will print the value of x

# else finally raise
try: # it will try to execute the code inside the block
    x = 10 / a # it will raise a ZeroDivisionError
except ZeroDivisionError: # it will catch the ZeroDivisionError and execute the code inside the block
    print("You cannot divide by zero") # it will print a message indicating that division by zero is not allowed
    x = 0 # it will set x to 0
except Exception as e: # it will catch any other exception and execute the code inside the block
    print(f"An error occurred: {e}") # it will print a message indicating that an error occurred and the error message  
else: # it will execute the code inside the block if no exception is raised
    print("Division successful") # it will print a message indicating that division was successful
finally: # it will execute the code inside the block regardless of whether an exception was raised or not
    print("This will always be executed") # it will print a message indicating that this block will always be executed

    
    
# File Handling
open("file.txt", "w") # it will open a file named file.txt in write mode and create it if it does not exist
with open("file.txt", "w") as f: # it will open a file named file.txt in write mode and create it if it does not exist and assign it to the variable f
    f.write("Hello, World!") # it will write "Hello, World!" to the file
with open("file.txt", "r") as f: # it will open a file named file.txt in read mode and assign it to the variable f
    content = f.read() # it will read the content of the file and store it in the variable content
print(content) # it will print the content of the file
    
        
                       
    


