"""
name = input("Enter your name: ")
print("Welcome " , name)

val = input("enter some value:")
print(type(val1), val) # "25" , "99.99" , input always results in string ( str )


# Take input from user

name = input("enter name: ")
age = input("enter age: ")
marks = input("enter marks: ")

print("welcome", name)
print("age =", age)
print("marks =", marks)


# write a program to input 2 numbers & print their sum.
first = int(input("enter first:"))
second = int(input("enter second:"))

print("sum:" , first + second)


# WAP to input side of a square & print its area
side = float(input("enter sqaure side:"))

print("area=" , side * side)

# WAP to input 2 floating point numbers & print their average
a = float(input("enter first:"))
b = float(input("enter second:"))
print("avg =", (a + b) /2)


# WAP to input 2 int numbers,a and b.
# print True if a is greater than or equal to b . if not print False

a = int(input("enter first:"))       
b = int(input("enter second:"))

print(a >= b)

"""
# WAP to input 2 floating point numbers & print their average 
 
a = float(input("Enter first :"))
b = float(input("Enter second :"))

print("avg = ",(a+b)/2)