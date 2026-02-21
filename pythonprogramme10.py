                                                   #  OOPS (Object oriented programming )

""" 
To map with real world scenarios , we startedusing objects in code.
    This is called object oriented progarmming.

    it decreases redundancy and increases code reusability .

"""
                                                   # Class and Object 


# Class is a blueprint for creating objects .
"""
# creating class
class Student:
    name = "Aman Ojha"

# creating object( instance of class)
s1 = Student()
print(s1.name)
    
"""


"""

class cars:
    color = "red"
    color2 = "blue"
    brand = "BMW"

s1 = cars()
s2 = cars()
s3 = cars()
print(s1.color)
print(s2.color2)
print(s3.brand)    

"""

                                                 # _ _ init _ _ Function

# Construcutor --- all classes have a function called __init__(), which is always executed when the object is bring initiated.

# creating class
class Student:
    def __init__(self, fullname):
        self.name = fullname

# creating onject 
s1 = Student("Aman")
print(s1.name) # Aman

s2 = Student("Amit")
print(s2.name)