# 1 reverse a string
s = 'Hello World'
l = s.split()
res = ''
for word in l:
    temp = ''
    for ch in word:
        temp = ch + temp
    res = res + temp + ' '
print(res)

# Second way
s1 = 'Hello world Example'
res1 = ''
temp1 = ''
for ch1 in s1:
    if ch1 != ' ':
        temp1 = ch1 + temp1
    else:
        res1 += temp1
        temp1 = ''
res1 = res1 + temp1 + ' '
print(res1)

# 2. Problem
# prime number (Brute Force Approach)
n = 11
c = 0
for i in range(1,n+1):
    if n%i == 0:
        c += 1
if c == 2:
    print('Prime')
else:
    print('Not a Prime')

