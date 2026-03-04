# # # program to print multiplication table
# # # for x in range(1,11):
# # #     print(f"{2} X {x} = {2*x}")
    
    
# # # program to print multiplication table in reverse
# # for x in range(10,1,-1):
# #     print(f"{2} X {x} = {2*x}")

# # to print numbers from specific index

# # l = [1,2,3,4,5,6,7,8,9]
# # for x in range(3,8):
# #     print(l[x])

# # task

# # for n in range(1,21):
# #     if (n%3 == 0):
# #         print(f"{n} - fizz")
# #     if (n%5==0):
# #         print(f"{n} - buzz")
# #     else:
# #         print(f"{n} - fizzbuzz")

# # for i in range(1,21):
# #     if (i%3==0):
# #         print(f"{i} - fizz")
# #     if (i%5==0) | (i%3==0):
# #         print(f"{i} - buzz")
# #     if (i%3==0) & (i%5==0):
# #         print(f"{i} - fizzbuzz")
    
# # 1. Print numbers from 1 to 10 using a loop.
# # for i in range (1,11):
# #     print(i)

# # 2. Print even numbers from 1 to 20.
# # for i in range(1,21):
# #     if(i%2==0):
# #         print(i)

# # 3. Print odd numbers from 1 to 20.
# # for i in range(1,21):
# #     if(i%2!=0):
# #         print(i)

# # 4. Calculate the sum of numbers from 1 to 100.
# # for i in range(1,101):
# #     p =(i*(i+1)/2)
# #     print(p)
# # 5. Print multiplication table of 5.
# # for i in range(1,11):
# #     print(f"{5} X {i} = {5*i}")

# n = int(input("Enter a number: "))

# fact = 1

# for i in range(1, n + 1):
#     fact *= i

# print("Factorial:", fact)

# count = 0
# for i in range(1,31):
#     if (i%2==0):
#         print(i)
#     else:
#         print(i)
# vowels only print
    
# str1 = 'something'
# x = 0
# while x<len(str1):
#    if str1 in 'aeiou':
#       print(str1[x])
#     x+=1