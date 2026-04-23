# Day 07 - Inheritance

# Single Inheritance
class Parent1:
    def show(self):
        print("Single Inheritance: Parent class")

class Child1(Parent1):
    pass

c = Child1()
c.show()


# Multiple Inheritance
class A:
    def method_a(self):
        print("Multiple Inheritance: Class A")

class B:
    def method_b(self):
        print("Multiple Inheritance: Class B")

class C(A, B):
    pass

obj = C()
obj.method_a()
obj.method_b()


# Multilevel Inheritance
class Grandparent:
    def gp(self):
        print("Multilevel: Grandparent")

class Parent2(Grandparent):
    def p(self):
        print("Multilevel: Parent")

class Child2(Parent2):
    def c(self):
        print("Multilevel: Child")

obj = Child2()
obj.gp()
obj.p()
obj.c()


# Hierarchical Inheritance
class Parent3:
    def show(self):
        print("Hierarchical: Parent")

class Child3(Parent3):
    pass

class Child4(Parent3):
    pass

Child3().show()
Child4().show()


# Hybrid Inheritance
class X:
    def show(self):
        print("Hybrid: Class X")

class Y(X):
    pass

class Z(X):
    pass

class D(Y, Z):
    pass

d = D()
d.show()
