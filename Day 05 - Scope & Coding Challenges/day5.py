# Day 05 - Scope & Coding Challenges

# Local Variable
def local_example():
    x = 10
    print("Local:", x)

local_example()


# Global Variable
y = 20

def global_example():
    print("Global:", y)

global_example()


# Non-Local Variable
def outer():
    z = 5
    def inner():
        nonlocal z
        z = 15
        print("Non-local:", z)
    inner()

outer()


# Coding Challenge 1 - Even or Odd
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Coding Challenge 2 - Sum of Numbers
n = 5
total = 0
for i in range(1, n+1):
    total += i
print("Sum:", total)


# Coding Challenge 3 - Reverse String
text = "Python"
print("Reverse:", text[::-1])
