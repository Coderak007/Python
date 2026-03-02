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

"""
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

"""

"""

# Super method - super() method is used to access methods of parent class .
class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("car started ...")

    @staticmethod
    def stop():
        print("car stoped.")

class Toyota(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name

car1 = Toyota("Prius", "electric")
print(car1.type)

"""
# Class Method ---
"""
A class method is bound to the class & receives the class as an implicit first argument .
NOTE - static method can't access or modify class state & generally for utility.

  class Student:
      @classmethod # decorator
      def college(cls):
            pass

"""

"""

class Person:
    name = "anonymous"

    def changeName(self, name):
        self.__class__.name = "Aman"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Aman Ojha")
print(p1.name)
print(Person.name)            

"""
# Property --- We use @property decorator on any method in the class to use the method as a property.
# eg ---
"""

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97 , 99)
print(stu1.percentage)

stu1.phy = 100
print(stu1.percentage)

"""
                                         # Polymorphism : Operator Overloading

# When the same operator is allowed to have different meaning according to the context.( Dunder functions )

"""

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i + ",self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal , newImg)
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal , newImg)

num1 = Complex(1, 5)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 - num2
num3.showNumber()
   
"""

# Let's Practice ---
# Define a circle class to create with radius r using the constructor. define an area() method of the class which calculates the area of the circle. define a perimeter() method of the class which allows you to calculate the perimeter of the circle.

"""
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 22/7 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 22/7 * self.radius
    
        
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

"""

# Define a Employee class with attribute role, department & salary . this class also showDetails() method. Create an Engineer class that inherits properties from employee & has additional attributes : name & age


class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role = ", self.role)
        print("dept = ", self.dept) 
        print("salary = ",self.salary)
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        super().__init__("Engineer", "IT","75,000")
       


engg1 = Engineer("Aman" , 22)
engg1.showDetails()           