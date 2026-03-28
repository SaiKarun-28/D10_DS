lst = [1,2,1,2,3,4,5]
l1 = []
dup = []
for i in lst:
    if i in l1:
        dup.append(i)
    else:
        l1.append(i)
print(l1)
print(dup)
# print(lst)