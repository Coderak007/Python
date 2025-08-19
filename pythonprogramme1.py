         # sum
a = 5000 
b = 1000
sum = a + b
print(sum)

# Arithmetic operators
a = 10
b = 5

print(a + b )
print(a - b )
print(a * b )
print(a / b )
print(a % b ) # remainder
print(a ** b) #a^b

# Relational operators
a = 50
b = 30
print(a == b) # False
print(a != b) # True
print(a >= b) # True
print(a > b) # True
print(a <= b) # False
print(a < b) # False

# Assignment operators
num = 10
num = num + 10 # we can also use num += 10 , we can use -= , *= , /= , %= , **=
print("num :", num)

# Logical operators ( not , and , or )
# it returns opposite
a = 50
b = 30
print(not False)
print(not(a > b))

val1 = True
val2 = False
print("and operator:" , val1 and val2)

print("OR operator:", val1 or val2)


# Type conversion and Type conversion
a = int("2")
b = 4.25

print(type(a))
print(a + b)

# input in python 

name = input("Enter your name: ")
print("Welcome AM" , name)
