
balance = 1000

# Functionalites
def deposit():
    amount = int(input('enter the amount :'))
    if amount > 0:
        print(f'{amount}\- deposited sucessfully.')
        return amount
    else:
        print(f'Invalid Amount')
        return 0
    
def withdraw ():
    amount = int(input('enter the amount :'))
    if amount <= balance:
        print(f'{amount}\- withdrawed sucessfully.')
        return amount
    else:
        print(f'Invaild amount enterd')
        return 0

def check_balance ():
    print(f'Available Balance is {balance}\-.')

def change_pin ():
    old_pin = int(input('enter the pin :'))
    if old_pin == pin:
       new_pin = int(input('enter the new pin :'))
       print('PIN changed sucessfully.')
       return new_pin
    else:
        print('wrong pin entered')
        return pin

# login 
print('---------> WELCOME TO ATM <--------')
pin = 5439
input_pin = int(input('enter the pin :'))
is_correct = False
chances = 5

for i in range(1,chances+1):
    if pin == input_pin:
        is_correct = True
        break
    else:
        if chances-i != 0:
            print(f'Wrong pin entered \n {chances-i} left')
            input_pin = int(input('enter the pin :'))
        else:
            break

# access
if is_correct:
    while True:
        print('TO DEPOSIT PRESS --> 1')
        print('TO WITHDRAW PESS --> 2')
        print('TO CHECK BALANCE PRESS --> 3')
        print('TO CHANGE PIN PRESS --> 4')
        print('PRESS 5 FOR EXIT')
        
        selection = int(input('enter your option :'))
        if selection == 1:
            balance += deposit()
        elif selection == 2:
            balance -= withdraw()
        elif selection == 3:
            check_balance()
        elif selection == 4:
            pin = change_pin()
        elif selection == 5:
            print ('THANK YOU AND VISIT AGAIN')
            break
else:
    print('Account has been blocked for 24 hours')