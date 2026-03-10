# problem-2

# x = input('enter :')
# x_x1 = []
# x_x2 = []
# if len(x)%2==0:
#     x1 = x[:len(x)//2]
#     x2 = x[len(x)//2:]
#     for i in range(len(x1)):
#         if x1[i] in 'AEIOUaeiou':
#             x_x1.append(i)
#         if x2[i] in 'AEIOUaeiou':
#             x_x2.append(i)
#     if x_x1 == x_x2:
#         print('same')
#     else:
#         print('not same')
# else:
#     print('lenght must be even')

# problem-3

s = 'aaabbbccdddaa'
dict1 = {}
for i in s:
    if i in dict1:
        dict1[i] +=1
    else:
        dict1[i] = 1
print(dict1)
for s,k in dict1.items():
    print(f"{s}{k}",end = '')