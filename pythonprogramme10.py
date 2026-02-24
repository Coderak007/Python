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

"""

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

"""


                                                # Static Methods
# Methods that don't use the self parameter (work at class level)
"""

class Student:
    @staticmethod # decorator
    def college():
        print("ABC college")


"""
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function , without permanently modifying it 

# ABSTRACTION - Hiding the implementation details of a class and only showing the essential feature to the user.
# ENCAPSULATION - Wrapping data and functions into a single unit (object).
 
# Abstraction ---

"""

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

car1 = Car()
car1.start()        

"""

# Practice --- Create Account class 2 attributes - balance & account no.
# Create methods for debit , credit and printing the balance

"""

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance = ", self.get_balance())


    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance
               

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500000)
acc1.get_balance
print(acc1.balance) 
print(acc1.account_no)
      
        
"""                                         