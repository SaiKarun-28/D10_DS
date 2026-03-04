#1. Create a list of 7 integers. Add a new number to the end of the list and print the updated list.

l1 = [1,2,3,4,5,6,7]
print(type(l1))
print(l1)

# adding elements

l1.append(8)
print(l1)

l1.append(9)
l1.append(10)
l1.append(11)
l1.append(12)
l1.append(13)
print(l1)

# update

l1[12] = 15
print(l1)

l1[0] = 'mango'
print(l1)

# read
l1[0]
print(l1[0])

print([10])

# delete
del l1[2]
print(l1)

print(type(l1))

#2. Create a tuple containing 5 different data types (e.g., integer, float, string, boolean, etc.). Print the type of each element in the tuple.

t1 = (1,2,3,4,5)
print(t1)

t2 = (1,1.2,'Hi',True,None)
print(t2)

# type of each element

print(type(t2[2]))
print(type(t2[3]))
print(type(t2[0]))
print(type(t2[1]))
print(type(t2[4]))

#3.  Create a dictionary that stores information about a student (name, age, course, and marks). Print the value of the marks key.

karun_det = {
    
    'name': 'karun',
    'age': '21',
    'course': 'IoT',
    'marks': '71'
}

print(karun_det)
print(karun_det['marks'])

# adding
karun_det['sec'] = 'A'
print(karun_det)

# acessing an element
print(karun_det['sec'])
print(karun_det['marks'])
print(karun_det['course'])

# update
karun_det['marks'] = 80
print(karun_det['marks'])

# delete
del(karun_det['marks'])
print(karun_det)

#4.  Create a set with at least 6 elements, including some duplicate values. Print the set and explain what happened to the duplicates.

s1 = {1,2,3,4,5,6,'hi','nana','hi',1,4,9}
print(s1)

# duplicates are automatically removed in sets.

#5. Create a string that contains your full name. Convert it to uppercase and print the length of the string.

str = ('imiddishetti')
print(str)
print(len(str))

# converting it into upper case
# by using 'str.upper()' built in method, it converts any string into uppercase letters.
print(str.upper())

# lower case
print(str.lower())