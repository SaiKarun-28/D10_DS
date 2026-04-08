balance = 1000

def deposit():
    amount = int(input('Enter Your Amount: '))
    if amount > 0:
        print(f'{amount}/- is credited successfully..!')
        return amount
    else:
        print('Invalid amount! \nPlz enter valid amount..!')
        return 0

def withdraw():
    amount = int(input('Enter Your Amount: '))
    if amount <= balance:
        print(f'{amount}/- is debited successfully..!')
        return amount
    else:
        print('Insufficient Fund..!')
        return 0

def check_balance():
    print(f'Available balance is: {balance}/-')

print('<---------- WELCOME TO 10K CODERS BANK ---------->')
db_pin = 1289
input_pin = int(input('Enter your pin: '))
chance = 3
is_pin_correct = False

for i in range(1,chance+1):
    if input_pin == db_pin:
        is_pin_correct = True
        break
    else:
        if chance - i != 0:
            print(f'Wrong pin, You have only {chance-i} chances left!')
            input_pin = int(input('Enter your pin: '))
        else:
            break

if is_pin_correct:
    while True:
        print('\nTO ADD MONEY PRESS -> 1')
        print('TO TAKE MONEY PRESS -> 2')
        print('TO CHECK BALANCE PRESS -> 3')
        print('TO EXIT FROM THE APP PRESS -> 4')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            balance += deposit()
        elif choice == 2:
            balance -= withdraw()
        elif choice == 3:
            check_balance()
        elif choice == 4:
            print('THANK YOU, VISIT AGAIN..!')
            break
        else:
            print('Invalid Choice, Plz enter valid option..!')
else:
    print('Your Account has been blocked for 24hrs..!')