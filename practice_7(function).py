# n=int(input())
# if n%2==1:
#     print("Weird")
# elif n%2==0 and n in range(2,5):
#     print("Not Weird")
# elif n%2==0 and n in range(6,21):
#     print("Weird")
# else:
#     n%2==0 and n>20
#     print("Not Weird")

# class Person:
#     def __init__(self,initialAge):
#         self.age=initialAge
#         if self.age<0:
#             print("Age is not valid, setting age to 0.")
#             self.age=0
#     def amIOld(self):
#         if self.age<13:
#             print("You are young.")
#         elif self.age>=13 and self.age <18:
#             print("You are a teenager")
#         else:
#             print("You are old")
#     def yearPasses(self):
#         self.age+=1   

        
# pers=Person(10)
# print(pers.amIOld())

# def sum1(numbers):
#     total=0
#     for i in numbers:
#         total+=i
#     return total

# print(sum1([8,2,3,0,7]))

# def multi(numbers):
#     total=1
#     for i in numbers:
#         total*=i
#     return total

# print(multi([8,2,3,-1,7]))

# def max1(a,b,c):
#     return max(a,b,c)

# print(max1(2,3,4))

# def max1(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c
    
# print(max1(5,8,10))

# def rev(s):
#     return "".join(reversed(s))

# print(rev("123abc"))

# # factorial
# from math import factorial
# def fact(n):
#     if n==0:
#         return 1
#     return n*factorial(n-1)

# print(fact(4))

# def check(a):
#     if a in range(3,9):
#         print("yes")
#     else:
#         print("no")
    
# print(check(90))

# def case(s):
#     count_upper=0
#     count_lower=0
#     for i in s:
#         if i.isupper():
#             count_upper+=1
#         else:
#             count_lower+=1
#     print(f'upper is {count_upper}')
#     print(f'lower is {count_lower}')   

# print(case("ThequickBrownFox"))

# def up_low(str):
#     upper_count=0
#     lower_count=0
#     for x in str:
#         if x.isupper():
#             upper_count+=1
#         else:
#             lower_count+=1
#     print(f'number of upper case letter {upper_count}')
#     print(f'number of lower case letter {lower_count}')

# print(up_low("The Thevfiyas Are Fucking"))

# def sample(list1):
#     new=[]
#     for i in list1:
#         if i not in new:
#             new.append(i)
#     return new

# print(sample([1,2,3,3,3,3,4,5]))

# def prime(n):
#     if n==1:
#         return False
#     elif n==2:
#         return True
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         return True

# print(prime(7))

# def sample(list1):
#     new=[]
#     for i in list1:
#         if i%2==0:
#             new.append(i)
#     return new

# print(sample([1, 2, 3, 4, 5, 6, 7, 8, 9]))

