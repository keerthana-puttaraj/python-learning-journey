# Day 04 - Functions & Arguments

# Function Introduction
def greet():
    print("Hello")

greet()


# Arguments
def add(a, b):
    print(a + b)

add(5, 3)


# Return Values
def multiply(a, b):
    return a * b

result = multiply(2, 4)
print(result)


# Packing (*args)
def total(*numbers):
    print(sum(numbers))

total(1, 2, 3)


# Unpacking
nums = (4, 5)

def add_two(a, b):
    print(a + b)

add_two(*nums)


# Variable Arguments (**kwargs)
def details(**data):
    print(data)

details(name="Keerthana", age=21)
