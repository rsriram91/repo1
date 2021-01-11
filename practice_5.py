# def func(a,b):
#     if a==b or a+b==5 or a-b==5:
#         return True
#     return False

# print(func(7,2))
# print(func(3,2))
# print(func(2,2))

# def add_numbers(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#          raise TypeError("Inputs must be integers")
#     return a + b

# print(add_numbers(10.5, 20))

##enter input in different lines
# name=str(input("enter your name: "))
# age=int(input("enter your age: "))
# address=input("enter the adderss: ")
# print(f'Name: {name}\nAge: {age}\nAddress: {address}')

# def prog(x,y):
#     if x>0 and y>0:
#         return (x+y)*(x+y)


# print(prog(2,3))

# import math
# p1 = [4, 0]
# p2 = [6, 6]
# distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

# print(round(distance,3))

# class Reverse:
#     def rev(self,s):
#         return " ".join(reversed(s.split()))


# print(Reverse().rev('hello .py'))

# class Rectangle:
#     def __init__(self,l,w):
#         self.l=l
#         self.w=w

#     def area(self):
#         return self.l*self.w


# rectangle1=Rectangle(12,10)
# print(rectangle1.area())

# from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r=r

#     def area(self):
#         return pi*self.r**2

#     def perimeter(self):
#         return 2*pi*self.r


# area1=Circle(2)
# print(area1.area())
# perimeter1=Circle(4)
# print(perimeter1.perimeter())

# class Inst_name:
#     def __init__(self,a):
#         self.a=a

#     def gett(self):
#         return type(self.a)

    
# b=Inst_name("gem")
# print(b.gett())

# import itertools
# x = itertools.cycle('ABCD')
# print(type(x).__name__)

# # getting input form the user in a class
# class IOString():
#     def __init__(self):
#         self.str1 = ""

#     def get_String(self):
#         self.str1 = input()

#     def print_String(self):
#         print(self.str1.upper())

# str1 = IOString()
# str1.get_String()
# str1.print_String()

# a=[1,2,3,6]
# a.append(10)

# print(list(reversed(a)))