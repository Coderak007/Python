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

"""

# creating class
class Student:

# default constructors ---
    def __init__(self):
        pass

# parameterized constructors ---
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("adding new student in database..")

# creating onject 
s1 = Student("Aman", 98)
print(s1.name, s1.marks) # Aman

s2 = Student("Amit", 98)
print(s2.name, s1.marks)

# The self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class.

"""

                                                      # class & Instance Attributes 

"""

class Student:
    college_name = "SAITM"
    name = "anonymous"

    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("adding new student in database..")

# creating onject 
s1 = Student("Aman", 98)
print(s1.name, s1.marks) # Aman

s2 = Student("Amit", 98)
print(s2.name, s1.marks)

print(s2.college_name)

"""

# METHODS - Methods are the functions that belong to objects.

"""

class Student:
    college_name = "SAITM"

    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
    
    def welcome(self):
        print("welcome student,", self.name)

    def get_marks(self):
        return self.marks    

# creating onject 
s1 = Student("Aman", 98)
print(s1.name, s1.marks) # Aman

s2 = Student("Amit", 98)
print(s2.name, s1.marks)

print(s2.college_name)

s1.welcome()
print(s1.get_marks())

"""


                                       # Practice

 # Create student class that takes name & marks of 3 subjects as arguments in constructor. then create a method to print the average.

class Student:
    def __init__(self , name , marks ):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your avg score is : ", sum/3)

s1 = Student("Aman ojha ", [99,99,98])
s1.get_avg()       



                                          