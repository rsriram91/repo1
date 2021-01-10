# # print first and last form list
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1])

# number=[]

# for i in range (1500,2701):
#     if (i%7==0) and (i%5==0):
#         number.append(str(i))

# print (','.join(number)) # joins the string with ,

# unit=input('(F) or (C): ')
# temperature=float(input("enter the temperature: "))

# if unit.upper == "C":
#     t=(temperature - 32 * 5/9)
#     print("the temprature in celsius is : ", t)
# else:
#     t=(temperature * 9/5 +32)
#     print("the temprature in farenhit is : ", t)


# secret_number = 2
# count=0
# chance=3
# while count<chance:
#     guess=int(input("enter your guess: "))
#     count=count+1
#     if guess == secret_number:
#         print("you won the game")
#         break
#     elif guess != secret_number:
#         print("try again")
# else:
#     print("you lost")

# pattern=[1,2,3,4,5,4,3,2,1]

# for i in pattern:
#     print(i*"*")

# name=str(input("enter your name: "))

# for i in name:
#     print("reverse :" + name[::-1])
#     break


# number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# even=[]
# odd=[]
# for i in number:
#     if i%2==0:
#         even.append(str(i))
#     elif i%2==1:
#         odd.append(str(i))
# print ("the even list is ", even) 
# print("the odd list is ", odd)

# number=[1,2,3,4,5,6,7,8,9,10,11]
# count_odd=0
# count_even=0
# for x in number:
#     if x %2==0:
#         count_even=1+count_even
#     else:
#         count_odd+=1

# print("total odd count: ", count_odd)
# print("total even count: ", count_even)

# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

# for item in datalist:
#     print(type(item))

# for n in range(6):
#     if n==3 or n==6:
#         pass
#     else:
#         print(n,end=" ")
#         continue
    
# fibonacci series

# x,y=0,1
# while y<50:
#     print(y, end=" ")
#     x,y=y,x+y

# for number in range(51):
#     if number %3==0 and number %5==0:
#         print("fizzbuzz")
#         continue
#     elif number %3==0:
#         print("fizz")
#         continue
#     elif number %5==0:
#         print("buzz")
#         continue
#     print(number)