# Logical Operators (5 Questions)

# 1. Given x = 10 and y = 20,
#    check whether both values are greater than 5.

x = 10
y = 20
z = x>=5 and y>=5
print(z)

# 2. Write a program to check if a number n = 15 lies between 10 and 20 (inclusive).

n = 15
m = n>=10 and n<=20
print(m)

# 3. Given is_logged_in = True and is_admin = False,
#    check if the user has either login or admin access.

is_logged_in = True
is_admin = False
print(is_logged_in or is_admin)

# 4. Given age = 16,
#    check whether the person is NOT eligible to vote.

age = 16
h = age>=18
print(not(h))

# 5. For a = 0, evaluate the logical expression:
#    not(a > 0 and a < 10) and print the result.

a = 0
j = a<10 and a>0
print(not(j))