# def func(n):
#     return n*((n+1)/2)

# print(int(func(8)))

# a=float(input("enter the height: "))
# unit=input('(F)eet or (I)n : ')

# if unit.upper == 'F':
#     b=a*12
#     print (b)
# else:
#     unit.upper == 'I'
#     b=a/12
#     print(b)

# from math import sqrt
# a=float(input("side 1: "))
# b=float(input("side 2: "))

# c=sqrt((a**2)+(b**2))

# print(f'the hypotnuse side is {c}')


# f=open('demo.txt','r')
# print(f.readlines(2))
# f.close()

# f=open('demo.txt','r')
# for line in f:
#     print(f.readlines())

# f=open('demo.txt','w')
# f.write('this is the best\nhow are you')
# f.close()

# f=open('test1.txt','x')
# f.write('this is the new file\nhow are u doing man ?')

# import os
# os.remove('demo.txt')

# import os
# os.mkdir('waste')

# import os
# if os.path.exists('practice_1.py'):
#     print('yes')
# else:
#     print('no')

# from pathlib import Path

# path=Path()
# for file in path.glob('*'):
#     print(file)


# x=10
# if x>5:
#     raise Exception(f'the value of x should be less than 10. You entered {x}')

# import sys
# def linux_interaction():
#     assert('linux' in sys.platform),'this code runs on Linux only'
#     print('doing something')

# try:
#     linux_interaction()
# except:
#     pass

## function inside func

# def test(a):
#     def add(b):
#         nonlocal a
#         a+=1
#         return a+b
#     return add
# Func=test(4)
# print(Func(4))

# def abc():
#     x=1
#     y=5
#     g=5
#     str1='aaa'
#     print("fuck u")

# print(abc.__code__.co_nlocals)

# def absolute_path(path_fname):
#     import os
#     return os.path.abspath('path_fname')

# print(absolute_path('Sriram JMR.docx'))

# import os
# a='Sriram JMR.docx'
# print(os.path.abspath(a))

# list1=[5,8,7,4,5,6]
# for i in list1:
#     if i >=4:
#         print("yes")
#     else:
#         print("no")

my_list1 = [30, 34, 56]
print(all(i>=30 for i in my_list1))





    
