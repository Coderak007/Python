                                 # OOPs - part 2 

# del keyword - Used to delete object properties or object itself.
"""

eg - del s1.name
     del s1

"""

# New Example ---

"""

class Student:
    def __init__(self , name):
        self.name = name

s1 = Student("Aman")
print(s1.name)
del s1.name
print(s1.name)        

"""

# Private (like) attributes & methods --- Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.
"""

class Account:
    def __init__(self , acc_no , acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345" , "abcde")

print(acc1.acc_no) 
print(acc1.reset_pass())

"""


                                          # Inheritance #

        # When one class (child / derived) derives the properties & methods of another class(parent / base)
# Single inheritance ---
"""

class Car:
    color = "Thunder black"
    @staticmethod
    def start():
        print("car started ...")

    @staticmethod
    def stop():
        print("car stoped.")

class Toyota(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyota("BMW")
car2 = Toyota("Audi")

print(car1.name)
print(car1.color)

"""
# Multi Level Inheritance ---
"""

class Car:
    @staticmethod
    def start():
        print("car started ...")

    @staticmethod
    def stop():
        print("car stoped.")

class Toyota(Car):
    def __init__(self, brand):
        self.brand = brand

class Ferrari(Toyota):
    def __init__(self, type):
        self.type = type

car1 = Ferrari("Petrol")
car1.start()

"""
# Multiple Inheritance ---

class A:
    varA = "hi , i am class A"

class B:
    varB = "hi , i am class B"

class C(A, B):
    varC = "hi , i am class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)  