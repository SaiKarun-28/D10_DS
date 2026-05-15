# Plus_one

lst1 = [9,9,9]
for i in range(len(lst1)-1,-1,-1):
    if lst1[i] < 9:
        lst1[i]+=1
        break
    else:
        lst1[i] = 0
else:
    lst1.insert(0,1)
print(lst1)

# Return Duplicates

k = [1,2,3,1,2,4]
res = []
for i in k:
    c = 0
    for j in k:
        if i == j:
            c += 1
    if c > 1:
        if i not in res:
            res.append(i)
print(res)

# Built_in_method

k1 = [1,2,3,4,1,2,3]
r = []
for i in k1:
    if k1.count(i) > 1:
        if i not in r:
            r.append(i)
print(r)

# Strong_Password

p = 'Sravan@123'
upper = False
lower = False
digit = False
special = False

if len(p) >= 8:
    for i in p:
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
        if i.isdigit():
            digit = True
        else:
            special = True
    if upper and lower and digit and special:
        print('Strong Password.')
    else:
        print('Weak Password...!')
else:
    print('Password must be 8 or greater than 8....!')
    
# Moving Zeros at the end.

a = [1,0,1,2,3,0,4]
zero = []
positive = []
for i in a:
    if i == 0:
        zero.append(i)
    else:
        positive.append(i)
print(positive + zero)

# Another method (Two pointers)

b = 0
c = 0
while c < len(a):
    if a[c] != 0:
     a[b],a[c] = a[c],a[b]
     b += 1
     c += 1
    else:
        c+=1
print(a)

# is sub string palindrome or not.

s = 'ababcad'
def is_pal(sub):
    i = 0
    j = len(sub)-1
    while i < j:
        if sub[i] != sub[j]:
            return False
        i += 1
        j -= 1
    return True

max_sub = ''
for i in range(len(s)):
     for j in range(i + 1,len(s)+1):
         sub = s[i:j]
         if is_pal(sub) == True:
            if len(sub) > len(max_sub):
               max_sub = sub
print(max_sub)

# Verify Parenthesis

# s = '([{([{}])}])'
s = '[{({{}})}]'
stack = []
is_valid = True
for ch in s:
    if ch in '([{([{':
        stack.append(ch)
    else:
        if len(stack) != 0:
            if (ch == ')' and stack[-1] == '(') or (ch == ']' and stack[-1] == '[') or (ch == '}' and stack[-1] == '{'):
                stack.pop()
            else:
                is_valid = False
                break
        else:
            is_vaild = False
            break
if len(stack) != 0:
    is_valid = False
print(is_valid)