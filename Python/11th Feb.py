# F strings
# p1 = input("enter the name :")
# city = input("city name :")
# i1 = input("instutite name :")
# d1 = input("domain name :")
# print(f"i am {p1}, came to {city} and joined in {i1} for {d1} course.")


# LEAP YEAR
# n = int(input())
# if (n%400 == 0):
#     print(f"{n} is a leap year")
# elif(n%100 == 0):
#     print(f"{n} is not a leap year")
# elif(n%4 == 0):
#     print(f"{n} is a leap year")
    
# ELECTRICITY BILL
# u = int(input("Enter the units :"))
# if (u<=100) :
#     amt = (u*2)
#     print(f"Your bill is {amt}")
# elif (u>100) and (u<=200):
#     extra_units = (u-100)
#     n_amt = (extra_units*3)+200
#     print(f"Your bill is {n_amt}")
# elif (u>200):
#     extra_units_1 = (u-200)
#     m_amt = (extra_units_1*5)+500
#     print(f"Your bill is {m_amt}")
    
    
# y = int(input("Enter the year :"))

# if y % 400 == 0:
#     print(f"{y} is a leap year")
# elif y % 100 == 0:
#     print(f"{y} is not a leap year")
# elif y % 4 == 0:
#     print(f"{y} is a leap year")
# else:
#     print(f"{y} is not a leap year")
    
u = int(input("Enter the units :"))
if (u<=100) :
    amt = (u*2)
    print(f"Your bill is {amt}")
elif (u>100) and (u<=200):
     extra_units = (u-100)
     n_amt = (extra_units*3)+200
     print(f"Your bill is {n_amt}")
elif (u>200):
     extra_units_1 = (u-200)
     m_amt = (extra_units_1*5)+500
     print(f"Your bill is {m_amt}")