# Even numbers should multiply by 2 and should be in list

j = [10,12,13,14,15]
k = []
for x in j:
    if x%2==0:
        x*=2
        k.append(x)
    else:
        k.append(x)
print(k)

# even indexes

b = []
for h in range(len(j)):
    if h%2==0:
        b.append(j[h]*2)
    else:
        b.append(j[h])
print(b)


# sorting list without using sort() method

# Ascending order

res = [10,9,5,4,3]
for x in range(len(res)):
    for y in range(x,len(res)):
        if res[x]>res[y]:
            res[x],res[y] = res[y],res[x]
print(res)

# Descending order

for x in range(len(res)):
    for y in range(x,len(res)):
        if res[x]<res[y]:
            res[x],res[y] = res[y],res[x]
print(res)


# # task-1

import random

x = int(input('Enter the any two number :'))
y = random.randint(10,100)
if x == y:
    print(f"Your number {x} and generated number{y} is same.")
else:
    print(f"your number {x} and generated number {y} are different.")

# task-2

# score = 0
# ramesh = input('enter')