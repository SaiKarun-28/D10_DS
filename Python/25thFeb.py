# nested if

# TEMPERATURE CHECK

# tem = int(input("enter the temp :"))
# if tem>0:
#     if tem<30 :
#         print("moderate")
#     elif tem>30 and tem<40:
#         print("hot")
#     else:
#         print("very hot and danger")
# else:
#     print("freezing")

# TRIANGLE FORMATION

x = int(input("enter the number:"))
y = int(input("enter the number:"))
z = int(input("enter the number:"))

if x+y+z==180:
    if x==y==z:
        print("equalateral triangle")
    elif x!=y==z or y!=x==z or z!=x==y:
        print("isosceless triangle")
    elif x!=y!=z:
        print("scalane triangle")
else:
    print("triangle can't be formed") 

