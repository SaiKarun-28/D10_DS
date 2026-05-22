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

