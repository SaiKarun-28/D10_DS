'''
Date: 30-03-2026
Day: Monday
'''
# Area of square
i = int(input('enter a side : '))
area = i*i
print(area)

# Area of rectangle
h = int(input('enter a lenght :'))
b = int(input('enter the breadth :'))
area1 = b*h
print(area1)

# Area of triangle
b1 = int(input('enter the base :'))
h2 = int(input('enter the height :'))
area2 = b1*h2/2
print(area2)

# Perimeter of the square
s = int(input('enter a side'))
perimeter = 4*s
print(perimeter)

# Perimeter of the rectangle
l1 = int(input('enter the lenght :'))
b1 = int(input('enter the breadth :'))
rect_perimeter = 2*(l1+b1)
print(rect_perimeter)

# Perimeter of triangle
s1 = int(input('enter the side :'))
s2 = int(input('enter the side :'))
s3 = int(input('enter the side :'))
triangle_perimeter = s1+s2+s3
print(triangle_perimeter)

# Break amount
amt = int(input('enter the amount :'))
t = amt//1000
thousands = t*1000
r = amt - thousands
a = r//500
five_hundereds = a*500
balance = r - five_hundereds
print(f'1000s : {t} 500s : {a} remaining : {balance}')

# Sum of marks
maths = int(input('enter the marks :'))
physics = int(input('enter the marks :'))
chemistry = int(input('enter the marks :'))
total = maths + physics + chemistry
print(total)

# Average marks
average_marks = total/3

# conversion
t_sec = int(input('enter the total seconds :'))
min = t_sec//60
hrs = min//60
Minutes = 0
Hours = 0
if min>=60:
    Minutes+=1
    if hrs>=60:
        Hours+=1
