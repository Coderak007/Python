
# Strings - string is data type that stores a sequence of characters :

"""
str1 = "We are heroes."
str2 = 'Batman'

"""

# escape sequence characters - \n - next line , \t - tab
"""
str = "This is our Earth \n We all loves our Earth . "
print(str) 

"""
###

"""
str1 = "Radhe"
len1 = len(str1)
print(len1)

str2 = "Krishna"
len2 = len(str2)
print(len2)
final_str = str1 + " " + str2
print(final_str)
print(len(final_str))

"""

# Indexing - Position

"""
str = " Hari-hara "
ch = str[2]
print(ch)
print(str[5])

"""

# Slicing ---

"""
str = "Radha Krishna"
print(str[1:5])

"""

# find the first largest element in the array 

"""
array = [ 4 , 3 , 1 , 5 , 7 , 65]
find_largest = max(array)
print("first largest element" , find_largest)
 
"""
# slicing another example :

"""

str = "ApnaCollege"
print(str[1:4])
print(str[1:len(str)])

"""
# Negative index -

"""

str = "Apple"
print(str[-3 : -1])
print(str[-5 : ])

"""
# String functions -
 
"""

str = "I am a coder and a police." 
print(str.endswith("er."))
print(str.capitalize())
print(str.replace("coder","Teacher"))
print(str.find("c"))
print(str.count("am"))

"""
# Wap to input user's first name & print its length 

"""

Name = input("Enter your name :")
print("length of your name", len(Name))

"""
# Wap t ofind the occurence of '$' in a string -

"""

str = " Hi , $ I am $ symbol $ 99.99"
print(str.count("$"))

"""