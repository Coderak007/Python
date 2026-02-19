                                                # LOOPS # 

" Loops are used to repeat instructions "
" used to save storage "
" increase readability of code "
" There are two types of loops in python "

                                               # While loops ---

# while condition : ---- here loop works until it meets the codition 
     # some work 

"""

count = 1                               # iterator & iteration
while count <= 5 :
    print(" Love you 3000 ")              
    count += 1

"""

"""

i = 1 
while i <= 9 :
    print(" Let me love you ")
    i += 1

"""

"""
i = 1
while i <= 10000 :
    print(" Men are brave " , i)
    i += 1

"""
# print numbers from 1 to 5 

"""

i = 1
while i <= 5:
    print( i)
    i += 1

print("Loop ended")

"""

# print numbers from 5 to 1 

"""

i = 5
while i >= 1 :
    print(i)
    i -= 1 

print(" Loop ended ")

"""

# print numbers from 1 to 100 

"""

i = 1 
while i <= 100 :
    print(i)
    i += 1
print(" Loop ended ")

"""

# print numbers from 100 to 1 

"""

i = 100 
while i >= 1: # stopping condition
    print(i)
    i -= 1
print( " loop ended ")

"""

# print the multilication table of a number n 

"""

print(" Table of n")
i = 1 
while i <= 10:
        print(n * i)
        i += 1 

"""

# print table of 12 ---

"""

# n = int(input( "enter number "))
i = 1
while i <= 10:
    print(12 * i)
    i += 1

"""

# print elements of the following list using a loop ---

"""

nums = [ 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100]     
# traverse                     
idx = 0
while idx < len(nums) :
    print(nums [idx])
    idx += 1

"""
# another example of above code ---

"""

heroes = [ "Ironman" , "batman" , "thor" , "superman" ]

i = 0
while i < len( heroes):
    print(heroes[i])
    i += 1 

"""
# Search for a number X in this tuple using loop : 

"""

nums = ( 1 , 4 , 9 , 16 , 25 , 36 , 49 ,64 , 81 , 100)

x = 64

i = 0         # initialisation
while i < len(nums):
    if(nums[i] == x):
        print(" FOUND ")
    else :
        print(" SEARCHING ") 
    i += 1

"""
                 # Break And Continue ---
"""
Break - used to terminate the loop when encountered . 

Continue - terminates execution in the current iteration & continue execution of the loop with the next iteration . 

"""

"""

# Examples --- 

i = 1 
while i <= 5 :
    print(i)
    if(i == 3):
        break
    i += 1

print(" End of loop ")

"""
# Example --- 

"""

nums = ( 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100 , 36)

x = 36

idx = 0         # initialisation
while idx < len(nums):
    if(nums[idx] == x):
        print(" FOUND at idx ", idx)
        break
    else :
        print(" SEARCHING ") 
    idx += 1
print(" End of Loop ")

"""

# continue : 

"""

i = 0 
while i <= 5:
    if( i == 3):
        i += 1
        continue # skip
    print(i)
    i += 1

"""

                                           # for loop
"""                                           
# 1 ---

nums = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ]    

for el in nums:
    print(el)

"""

"""
# 2

veggies = [ "potato","ladyfinger","peas","cauliflower"]

for el in veggies:
    print(el)

"""

"""
# 3


tup = (1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 )

for el in tup:
    print(el)

"""

# 4

"""

str = "men are brave"

for char in str:
    if(char == 'b'):
        print("b found")
        #continue
        break
    print(char)
else:
    print("END")

"""    


                                           # practice questions -

# print the elements of the following list using a loop .
#  [1, 4, 9 , 16, 25, 36, 49, 64, 81, 100]

"""

nums = [1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100 ]

for el in nums:
    print(el)

"""
# Search for a number x in this tuple using loop . 
#  [1, 4, 9 , 16, 25, 36, 49, 64, 81, 100]

"""

nums = (1, 4, 9 , 16, 25, 36, 49, 64, 81, 100, 49)
x = 49
idx = 0

for el in nums:
    if( el == x):
        print(" number found at idx ", idx)
        break
    idx += 1

"""
                                     # range()
"""
Range functions returns a sequence of numbers, starting from 0 by default and increments by 1(by default), and stops before a specified number.

range(start?,stop,step?)

"""
"""
for el in range(5):
    print(el)
"""
"""
for el in range(1 , 5):
    print(el)
"""
"""
for el in range(1 , 5 , 2):
    print(el)
"""

# Wap to print all numbers which are divisible by 3 and 5 upto first fifty numbers by loop - 


"""

i = 1
while i <= 50:
    if i % 3 == 0 and i % 5 == 0:
        print(i,"is divisible by both 3 and 5 ")
    i += 1

"""
     
  
# Make an AP ( first number , common difference and number of terms take all from user ) - 

"""

a = int(input("Enter first number : "))
d = int(input("Enter common difference : "))
n = int(input("Enter number of terms : "))

i = 1
while i <= n:
    b = a + (i-1) * d
    print(b)
    i += 1

"""

# Similarly make a GP - 

"""

a = int(input("Enter first number : "))
r = int(input("Enter common ratio : "))
n = int(input("Enter number of terms : "))

i = 1
while i <= n:
    b = a * (r ** i)
    print(b)
    i += 1


"""



for i in range(0 , 4):
    for j in range(0 , 4):
        print("*",end=" ")
    print()
