# add all the elements in list without using any predefined functions
d = [10,20,30,50]
d1 = 0
for x in d:
    d1 = d1 + x
print(d1)

# lenght of list without using functions

k = [10,20,30,40,50]
count = 0
for x in k:
    count+=1
print(count)

# add's only numbers

s = [10,20,30,40,50,'python','java']
s2 = 0
for c in s:
    if type(c) == int:
        s2+=c
print(s2)

# maximum without using any pre defined functions

j = [10,20,30,40,50]
for x in j:
    hig = 0
    if x > hig:
        hig+=x
print(hig)


# average

list1 = [10,20,30,40,50,60]
sum1 = 0
count1 = 0
for s in list1:
    sum1+=s
    count1+=1
    avg = sum1/count1
print(avg)

