# str = 'something is fishy'
# x = 1
# for char in str:
#     print(char,str[x])
#     x+=1

"""" to print D-HELLO
T-HELLO
A-HELLO

"""""
# str = 'DATA'
# for i in str:
#     print(f"{i}-HELLO")

# list_1 =[4,6,8,2,3,1,8,9]
# for i in list_1:
#     print(f"{i} square is {i**2}")
    
# l=[1,2,3,4,5,6,7,8,9]
# for i in l:
#     x = i**2
#     print(f"{i} square is {x}")

# Problem-2
# list_1= ['shiva','karun','karthik','tejaswini','yamini','deepak','sathwik']
# for i in list_1:
#     print(f"{i} lenght is {len(i)}")
    
# nums = [3,5,7,8,2,4,6,10]
# x = 0
# for i in nums:
#     print(i*x)
#     x+=1

## count of occurance of particular character in a given string.

# str1='BANANA'

# dict1 = {}

# for x in str1:
#     if x in dict1:
#         dict1[x]+=1
#     else:
#         dict1[x]=1
# print(dict1)

# # string conversions
# l1 = []
# ios = ['apple','banana','SOME','hello','WELCOME','oops']
# for i in ios:
#     if i==i.lower():
#         # print(i.upper())
#         l1+=[i.upper()]
#     else:
#         #  print(i.lower())
#         l1+=[i.lower()]
# print(l1)

# # problem-2
# str1 = 'soMetHINg'
# for j in str1:
#     if j==j.lower():
#         print(j.upper())
#     else:
#         print(j.upper())

# to print in as a same string or as a single word.
# o = ''
# for j in str1:
#     if j==j.lower():
#         o+=j.upper()
#     else:
#         o+=j.lower()
# print(o)

# #factorial = 5*4*3*2*1=120
# f = int(input("enter the number:"))
# fact = 1
# for i in range (1,f+1,1):
#     fact*=i
# print(fact)

# TASK
ecommerce_data = [
    {
        "order_id": "O1001",
        "customer_name": "Ravi Kumar",
        "city": "Hyderabad",
        "product": "Wireless Mouse",
        "category": "Electronics",
        "price": 799,
        "quantity": 2,
        "total_amount": 1598,
        "payment_method": "UPI",
        "order_status": "Delivered"
    },
    {
        "order_id": "O1002",
        "customer_name": "Sneha Reddy",
        "city": "Bangalore",
        "product": "Bluetooth Headphones",
        "category": "Electronics",
        "price": 1999,
        "quantity": 1,
        "total_amount": 1999,
        "payment_method": "Credit Card",
        "order_status": "Shipped"
    },
    {
        "order_id": "O1003",
        "customer_name": "Arjun Singh",
        "city": "Mumbai",
        "product": "Running Shoes",
        "category": "Fashion",
        "price": 2499,
        "quantity": 1,
        "total_amount": 2499,
        "payment_method": "Cash on Delivery",
        "order_status": "Processing"
    },
    {
        "order_id": "O1004",
        "customer_name": "Priya Sharma",
        "city": "Delhi",
        "product": "Smart Watch",
        "category": "Electronics",
        "price": 3499,
        "quantity": 1,
        "total_amount": 3499,
        "payment_method": "Debit Card",
        "order_status": "Delivered"
    },
    {
        "order_id": "O1005",
        "customer_name": "Kiran Patel",
        "city": "Chennai",
        "product": "Laptop Backpack",
        "category": "Accessories",
        "price": 1299,
        "quantity": 3,
        "total_amount": 3897,
        "payment_method": "UPI",
        "order_status": "Shipped"
    }
]

for x in ecommerce_data:
    if x['payment_method'] == 'UPI':
         print(x['customer_name'])
    if x['quantity']>1:
        print(x['customer_name'])
    if x['category'] != 'Electronics':
        print(x['customer_name'])