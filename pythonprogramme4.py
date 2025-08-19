# Conditional statements - 

# Traffic light example - 

"""

light = "Green"

if( light == "Red"):
    print("stop")
elif(light == "Green"):
    print("Go")
elif(light == "Yellow"):
    print("Look")
else:
    print("light is broken")

"""
# About elif --- 

"""
num = 5

if(num>2):
    print("greater than 2")
elif(num>3):
    print("greater than 3")

"""

# Here elif is executed due to true presence of if 

# Examples --- 

"""

age = 14

if(age >= 18):
    print("Drive")
else:
    print("Cannot Drive")

"""
# Indentation - it means spacing and it is must in python language :

# wap to give grade to the students ---

"""
marks >= 90 , grade = "A"
90 > marks >= 80 , grade = "B"
80 > marks >= 70 , grade = "C"
70 > marks , grade = "D"

"""
# sol - 

"""

marks = 79

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C" 
else:
    grade = "D"
print(" grade of the student -> ", grade )

"""
                                                     # PRACTICE #    

# Doing a nesting code for example ---

"""
age = 34 

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

"""

# Wap to check if a number entered by the user is odd or even .

"""

num = int(input("Enter number "))
rem = num % 2
if(rem == 0):
    print("Even")
else:
    print("Odd")

"""
# Wap to find the largest of three numbers entered by the user ---

"""

a = int(input(" Enter first number : "))
b = int(input(" Enter second number : "))
c = int(input(" Enter third number : "))

if( a >= b and a >= c):
    print(" first number is largest " , a)
elif(b >= c):
    print(" second number is largest " , b)
else:
    print(" third is largest " , c)
    
"""

# Wap to check if a number is a multiple of 7 or not .

"""

num = int(input(" Enter number "))
if( num % 7 == 0):
    print(" mutliple of 7 ")
else:
    print(" Not a multiple ")

"""