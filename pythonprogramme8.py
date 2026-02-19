                                                      # Lets practice #

# print numbers from 1 to 10 using for loop ---

"""

for i in range(1,11):
    print(i , end = ' ')

"""
# print all even numbers from 1 to 20 using while loop ---

"""

i = 1 
while i <= 20:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1

"""

"""

i = 2
while i <= 20:
    print(i)
    i += 2

"""

# Sum of numbers from 1 to 1000 using a for loop ---

"""

total = 0
for i in range(1, 1001):
    total += i
print("sum:", total)    

"""


# print the multiplication table of a number n , upto 10 ---

"""

n = int(input("Enter a number : "))
i = 1 
while i <= 10:
    print( n * i)
    i += 1

"""

"""

n = int(input("Enter a number : "))

for i in range(1,11):
    print(n * i)

"""
# print the factorial of a number n ---

"""

n = int(input("Enter a number : "))
factorial = 1
for i in range(1, n+1):
    factorial *= i  
print("Factorial:", factorial)


"""
# code used from math module to find factorial ---

"""
import math

n = int(input("Enter a number: "))
print("Factorial:", math.factorial(n))

"""
# print the fibonacci series upto n terms ---
"""
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

"""
# print numbers from 1 to 100 ---

"""

for i in range(1 , 101):
    print(i)
    
"""   
                   # Pass statement #
# pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
# Example ---
"""

for i in range(5):
    pass # TODO: implement this loop later  

print("Men are Brave")  

"""
