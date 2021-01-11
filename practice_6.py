
# # diagonal difference in a matrix
# def difference(arr): 
#     left_arr=[]
#     right_arr=[]
    
#     for i in range (len(arr)):
#         counter=0
#         counter2=len(arr)-1
#         left_arr.append(arr[counter][counter])
#         counter+=1
#     print(left_arr)
    
#     counter=0
#     for i in range (len(arr)):
#         right_arr.append(arr[counter][counter2])
#         counter+=1
#         counter-=1
#     print(right_arr)
    
#     return abs (sum(left_arr)-(right_arr))


# print(difference([1,2] ,[5,5]))

# word=str(input())
# print(f'Hello, World.\n{word}')

# i=int(input())
# d=float(input())
# s=str(input())

# a=int(round(i+d))
# b=d+d
# c="HackerRank"
# print(f'{a}\n{b}\n{c} {s}')


meal_cost=float(input())
tip_percent=int(input())
tax_percent=int(input())

def solve(meal_cost, tip_percent, tax_percent):
    
    tip=(meal_cost*tip_percent)/100
    tax=(meal_cost*tax_percent)/100
    return (round (meal_cost+tip+tax))
   



