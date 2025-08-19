                                                       # List and Tuple 
# lists in python

"""
  
A built in data type that stores set of values , it can store elements of different types ( strings , float , integers etc .)
It is like array , we can type many data in single list 

marks = [87 , 78 , 89, 99 , 99] # marks[0] , marks[1]

student = [" Aman " , 99 , 21 , "pluto"] # student[0] , student[1] 

student[0] = " Arjun " # Allowe in python 

len(student)  # returns length

"""
# example --- 

"""

marks = [99.1 , 99.2 , 99.3 , 99.4 , 99.5 , 99.6]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[3])

"""
# strings are immutable ( cannot modify or change )
# lists are mutable ( can be modify )

# example ---

"""

student = [" Aman " , 21 , 99.1 , " Delhi "]
print(student[0])
student[0] = " Krishna "
print(student)

"""
# list slicing -
"similar to string slicing " 
" list_name[ starting_idx : ending_idx ] # ending idx is not included "

# example ---

"""

marks = [ 87 , 97 , 86 , 96 , 89 , 99 ]
print(marks[ 1 : 4 ])
print(marks[ : 4 ])
print(marks[ 1 : ])
print(marks[ -3 : -1 ])

"""
# List methods ---

# list.append( ) # adds one element at the end

"""

list = [4 , 5 , 8 ]
list.append(9)
print(list)

"""
# list.sort( ) #sorts in ascending order 

"""

list = [ 9 , 4 , 6 , 0]
list.sort()
print(list)

"""
# list.sort(reverse = True)  # sorts in descending order

"""

list = [ "banana" , "litchi" , "apple"  ] 
list.sort(reverse = True)
print(list)

"""

# list.reverse() # reverses list

"""

list = [ 456 , 222 , 333 , 106]
list.reverse()
print(list)

"""
# list.insert(idx,el) # insert element at index

"""

list = [ 4 , 6 , 7 , 2 , 4 ,]
list.insert( 0 , 1)
print(list) 

"""
# list.remove( ) # removes first occurence of element
 
"""

list = [ 5 , 4 , 9 , 6 ]
list.remove( 6 )
print(list)

"""
# list.pop(idx) # remove element at idx

"""

list = [ 8 , 5 , 3 , 0]
list.pop(3)
print(list)

"""
                                       # Tuples in python

# A built-in data type that lets us create immutable sequences of values 
# immutable

"""

tup = ( 34 , 56 , 78 , 45)
print(type(tup))
print(tup[0])
print(tup[3])

"""

"""
tup = ()
print(tup)

tup = (7,) # , is must for single character 
print(tup) 

"""

# slicing of tuples

"""

tup = ( 1 , 6 , 5 , 3 )
print(tup[1:3])

"""

# Tuple methods 

"""

tup = ( 2 , 1 , 3 , 3 , 1 , 3)
print(tup.index(2))  # returns index of first occurence 
print(tup.count(3))  # counts total occurences

"""
                                 # Problems 

# Wap t oask the user to enter names of their 3 favorite animes & store them in a list .

"""
anime = []
anime1 = input(" Enter first anime : ")
anime2 =input(" Enter second anime :")
anime3 = input(" Enter third anime : ")

anime.append(anime1)
anime.append(anime2)
anime.append(anime3)

print(anime)

"""

"""
anime = []
anime.append(input(" Enter first anime : "))
anime.append(input(" Enter second anime :"))
anime.append(input(" Enter third anime : "))
print(anime)
"""

# Wap to check if a list contains a palindrome of elements . ( Hint: use copy() method)

"""

list1 = [1 , 2 , 1]
#list1 = [1 , 2 , 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
   print("Not palindrome")

"""

# Wap to count the number of students with the "A" grade in the following tuple
#["C","D","A","A","B","B","A"]

"""

grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

"""
# Store the above values in a list & sort them from "A"to"D".

"""

grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)

"""