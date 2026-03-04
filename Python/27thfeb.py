# program for to find number of digits in a given number.

# x = int(input('enter the num :'))
# count = 0
# while x >0:
#     s =x%10
#     count+=1
#     x=x//10
# print(count)

# program to find whether given num is perfect number or not.

# x = int(input("enter the number :"))
# y = 1
# sum = 0
# while y<=x//2:
#     if x%y==0:
#         # print(y)
#         sum+=y
#     y+=1
# print(sum)
# if x==sum :
#     print(f"{x} is a perfect number")
# else:
#     print(f"{x} is not a perfect number")


# perefct square

# num = int(input("enter the number :"))
# x = 1
# is_perfect_square = False
# while x<=num//2:
#     if x*x==num:
#         is_perfect_square = True
#     x+=1
# if is_perfect_square == True :
#     print('perfect square')
# else:
#     print('not a perfect square')

# TASK : STRONG NUMBER

num = int(input("enter the number :"))
k = num
sum1 = 0
while num>0 and num!=0 :
    id = num%10
    s = 1
    for i in range(id,0,-1):
        s*=i
    sum1 = s+sum1
    num = num//10
print(sum1)

if sum1 == k :
    print(f'{k} is a strong number.')
else:
    print(f'{k} is not a strong number.')
    