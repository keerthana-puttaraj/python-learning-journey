# Day 06 - OOP Basics

# Class and Object
class Person:
    def _init_(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)

p1 = Person("Keerthana")
p1.greet()


# Methods in Class
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print("Addition:", calc.add(5, 3))


# Decorator (Basic)
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
