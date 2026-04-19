# Day 03 - Control Statements

# If-Else
a = 10
if a > 5:
    print("Greater than 5")
else:
    print("Less or equal to 5")


# Nested If
num = 8
if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")


# Ternary Condition
x = 20
result = "Even" if x % 2 == 0 else "Odd"
print(result)


# Match Case (Python 3.10+)
day = 1
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Other day")


# While Loop
i = 1
while i <= 3:
    print(i)
    i += 1


# For Loop
for i in range(1, 4):
    print(i)


# Break
for i in range(5):
    if i == 3:
        break
    print(i)


# Continue
for i in range(5):
    if i == 2:
        continue
    print(i)


# Pass
for i in range(3):
    pass
