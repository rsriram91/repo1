# import os.path
# open('abc.txt', 'w')
# print(os.path.isfile('abc.txt'))

##to check if the shell is executing 32 or 64 bit
# import struct
# print(struct.calcsize("P") * 8)

##get os name and release
# import platform
# import os
# print(os.name)
# print(platform.system())
# print(platform.release())

# def paliandrome(n):
#         if str(n)==str(n)[::-1]:
#             return "yes"
#         return "try any other word"

# print(paliandrome(123))

# def isPalindrome(string):
# 	left_pos = 0
# 	right_pos = len(string) - 1
	
# 	while right_pos >= left_pos:
# 		if not string[left_pos] == string[right_pos]:
# 			return False
# 		left_pos += 1
# 		right_pos -= 1
# 	return True
# print(isPalindrome('aza')) 

# def perfect_num(n):
#     sum1=0
#     for i in range(1,n):
#         if n%i==0:
#             sum1+=i
#     return sum1==n

# print(perfect_num(20))

# def pascal_triangle(n):
#    trow = [1]
#    y = [0]
#    for x in range(max(n,0)):
#       print(trow)
#       trow=[l+r for l,r in zip(trow+y, y+trow)]
#    return n>=1

# pascal_triangle(8) 

# import string,sys

# def pangram(str1,alphabet=string.ascii_lowercase):
#     alphaset=set(alphabet)
#     return alphaset<=set(str1.lower())


# print(pangram("The quick brown fox jumps over the lazy dog"))

# def square():
#     list1=[]
#     for a in range(1,31):
#         list1.append(a**2)
#     return list1
# print(square())

# items=[n for n in input().split('-')]
# items.sort()
# print('-'.join(items))

# from os import listdir
# from os.path import isfile, join
# files_list=[f for f in listdir('C:\Users\Sriram\Desktop\'Python Codes'') if isfile(join('C:\Users\Sriram\Desktop\'Python Codes'',f))]
# print(files_list)

# # placing * in a function parameter we can pass multiple arguments
## placing ** we can pass multiple key value pairs or keyword arguments
# def func(*n):
#     total=0
#     for i in n:
#         total+=i
#     return total
# print(func(1,2,3,4,5))

# import getpass
# print(getpass.getuser())

## to get the ip address 
# import socket
# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
# if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
# s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
# socket.SOCK_DGRAM)]][0][1]]) if l][0][0])