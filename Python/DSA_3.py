write a program to print numbers from m to n
m = int(input('enter the number :'))
n = int(input('enter the number :'))
while m<=n:
    print(m)
    m+=1
    
# reverse
m1 = int(input('enter the number :'))
n1 = int(input('enter the number :'))
while m1<=n1:
    print(n1)
    n1 = n1-1
    
# sum of n natural numbers
n = 10
s = 0
for i in range(1,n+1):
    s +=i
print(s)

# sum of even numbers
n1 = 100
s1 = 0
for i in range(1,n1+1):
     if i%2==0:
         s1+=i
print(s1)

# prime numbers
# print the numbers from a list where 1st digit and last digit should be same
s = [122,9889,565,8768,939,900,1221,430]
r = []
for i in s:
    k = i
    last = k%10
    while k>=10:
        k = k//10
        if k == last:
            r.append(i)
print(r)
        