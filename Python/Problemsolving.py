# Program to find even num or odd
def Even (num):
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")

Even(2)
Even(17)

# 2. Find the largest of given 3 numbers.
lst = [1,2,3,4,3]
print(max(lst))

# Another method without built in functions.
max_num = 0
for i in lst:
    if i > max_num:
        max_num = i
print(max_num)

# 3. Program to Check string is palindrome.
s = 'markram'
d = ''
for i in range(len(s)-1,-1,-1):
    d+= s[i]
if s == d:
    print('Palindrome')
else:
    print('Not a Palindrome')

# 4. Calculate the Factorial of a number.
num = 5
fact = 1
for i in range(1,num+1):
    fact *= i
print(fact)

# Another method using Recursive.
def factorial (m,n):
    if m>=1:
        n*=m
        return factorial(m-1,n)
    print(n)
factorial(5,1)

# 5.Fibonacci sequence up to n terms.
"""Fibonacci is the sum of 2 previous numbers 
example 0,1,1,2,3,5,8,13,21,34,55...
"""
n = 5
a = 0
b = 1
for i in range(n):
    print(a)
    c = a+b
    a = b
    b = c

# 6. Count the number of vowels in a string.
vowels = ['a','e','i','o','u','A','E','I','O','U']
count = 0
s = 'sai_karun'
for ch in s:
    if ch in vowels:
        count+=1
print(count)

# 7. Sum of elements in a list.
lst = [1,2,3,4,5,6,7,8,9]
sum = 0
for num in lst:
    sum+=num
print(sum)

# 8. Program to reverse a string.
s1 = 'sai karun'
for ch in range(len(s1)-1,-1,-1):
    print(s[ch],end = '')
# Another method.
s2 = 'SAI KARUN'
d =''
for a in range(len(s2)-1,-1,-1):
   d += s2[a]
print(d)

# 9. Prime number.
'''
A number is said to be prime when it has factors of 1 and it self.
'''
n = 5
factors = 0
for i in range(1,n+1):
    if n%i == 0:
        factors += 1
if factors == 2:
    print('prime')
else:
    print('not a prime')

# 10. GCD of two numbers.

def gcd (a,b):
    a = abs(a)
    b = abs(b)
    
    # loop until b becomes zero.
    while b != 0:
        rem = a%b
        a = b
        b = rem
    print(a)
gcd(72,48)

# 11. Multiplication table of a given number.
table = 2
end = 10
for i in range(1,end+1):
    res = 2*i
    print(f'{2}X{i}={res}')

# 12. Second largest number in a list.
lst1 = [1,2,3,4,5,6,7,8,9,101,10,91,118,127,2]
"""
Sort the list and then print the -2 index of list
that is our second largest number.
"""
# Sort
for i in range(len(lst1)):
    for j in range(i+1,len(lst1)):
        if lst1[i] > lst1[j]:
            lst1[i],lst1[j] = lst1[j],lst1[i]
s = lst1[-2]
print(s)

# 13. Remove duplicates from the list.
lst2 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10]
res = []
for i in lst2:
    if i not in res:
        res.append(i)
print(res)

# 14. Sort list in ascending order.
num = [1,3,4,2,8,9,7,10,12,11]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] > num[j]:
            num[i],num[j] = num[j],num[i]
print(num)

# Descending order.
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] < num[j]:
            num[i],num[j] = num[j],num[i]
print(num)

# 15. Convert Celsius into Fahrenheit.

celsius = 32
fahrenheit = celsius*1.8+32
print(fahrenheit)

# 16. Lenght of list without using len().
lst3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
count = 0
for i in lst3:
    count += 1
print(count)

# 17. Program to merge two lists.
a = [1,2,3]
b = [4,5,6]
print(a+b)

# 18. Average of number in a list
s = [1,2,31,4]
sum1 = 0
count1 = 0
for i in s:
    count1+=1
    sum1+=i
average = sum1/count1
print(average)

# 19. Maximum and Minimum value in a list.
l = [3,4,5,6,7,8,9,10,2,1]
max1 =l[0]
min1 = l[0]
for i in l:
    if i > max1:
        max1 = i
    if i < min1:
        min1 = i
print(max1,min1)

# Another Method
"""
Sort the list and then print the indexes 0 and -1 as min and max.
"""
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
minimum = l[0]
maximum = l[-1]
print(minimum,maximum)

# 20. Leap Year.
"""
year(number) should be divisible by 4 and 400, but not with 100.
then it is an leap year.
"""
