# program for checking perfect number and perfect square

def perfect_num(x):
    y = 1
    sum = 0
    while y<=x//2 :
        if x%y == 0:
            sum+=y
        y+=1
    if x == sum :
        print(f"{x} is perfect number")
    else :
        print(f"{x} is not a perfect number")

perfect_num(6)
perfect_num(8)


def perfect_square(x):
    y = 1
    is_perefct_square = False
    while y<x//2 :
        if y*y==x:
            is_perefct_square = True
        y+=1
    if is_perefct_square == True :
        print('Perfect Square')    
    else:
        print('Not a Perfect Square')

perfect_square(9)
perfect_square(25)
perfect_square(8)