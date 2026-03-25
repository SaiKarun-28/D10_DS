def steps(j):
    if j>0:
        print(f"{j}th step")
        return steps(j-1)
    print('reached')

steps(5)
steps(10)

# adding using recursion

def numbers(ip,n):
    if ip >=1:
        n+=ip
        return numbers(ip-1,n)
    print(n)
    
numbers(5,0)

# method-2 using for loop

def add(n):
    sum1 = 0
    for i in range(1,n+1):
        sum1+=i
    print(sum1)
    
add(5)


# factorial using recursion

def factorial(m,n):
    if m>=1:
        n*=m
        return factorial(m-1,n)
    print(n)

factorial(5,1)

# method-2 using for loop

def fact(b):
    fact = 1
    for i in range(1,b+1):
        fact*=i
    print(fact)