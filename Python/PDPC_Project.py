"""
To connect sql and python we need to install mysql-connector-python package
from pip install
"""
# Import mysql.connector
import mysql.connector

# Connectivity
con = mysql.connector.connect(
    user = 'root',
    password = '1234',
    database = 'bank',
    host = 'localhost'
)

crsr = con.cursor()

# Create Table

query = """
CREATE TABLE ACCOUNTS (
    AC_NO INT PRIMARY KEY AUTO_INCREMENT,
    CUSTOMER_NAME VARCHAR(50) NOT NULL,
    I_AMOUNT DECIMAL(10,2) NOT NULL CHECK(I_AMOUNT > 0),
    BALANCE DECIMAL (10,2)
)

"""
crsr.execute(query)
con.commit()
crsr.close()
con.close()
print('Table Created Sucessfully...!')

# Functionalites

def create_account():
    name = input('enter your name : ')
    amnt = float(input('enter your initial amount : '))
    bal = float(input('enter your balance : '))
    
    query = """
    INSERT INTO ACCOUNTS(CUSTOMER_NAME,I_AMOUNT,BALANCE)
    VALUES(%s,%s,%s)
    """
    crsr.execute(query,(name,amnt,bal))
    con.commit()
    print('Account created sucessfully...!')

def deposit():
    no = int(input('enter your account number : '))
    amnt = float(input('enter your amount : '))
    if amnt > 0:
        query = """
        UPDATE ACCOUNTS SET BALANCE = BALANCE + %s
        WHERE AC_NO = %s
        """
    crsr.execute(query,(amnt,no))
    con.commit()
    print('Deposit Sucessful...!')

def withdraw():
    amnt = float(input('Enter the amount : '))
    ac_num = int(input('Enter the Account number :'))
    
    query = """
    SELECT BALANCE FROM ACCOUNTS WHERE AC_NO = %s;
    """
    crsr.execute(query,(ac_num,))
    balance = crsr.fetchone()
    
    # If balance is gerater than amnt then withdraw is sucessful or else not sucessful.
    if balance != None:
        bal = balance[0]
        if bal >= amnt:
            query1 = """
            UPDATE ACCOUNTS SET BALANCE = BALANCE - %s
            WHERE AC_NO = %s
            """
            crsr.execute(query1,(amnt,ac_num))
            con.commit()
            print('Amount Debited Sucessfully...!')
        else:
            print('Insuficient Funds....!')
    else:
        print('Account not found....!')

def check_balance():
    ac_no = int(input('Enter the Account NUmber : '))
    
    query = """
    SELECT BALANCE FROM ACCOUNTS WHERE AC_NO = %s
    """
    crsr.execute(query,(ac_no,))
    balance = crsr.fetchone()
    con.commit()
    if balance != None:
        print('-------- Your Balance----------')
        print('Balance : ',balance[0])
    else:
        print('Account not Found....!')

def fund_transfer():
    sender = int(input('Enter the sender account number : '))
    reciever = int(input('Enter the reciever account number : '))
    amount = int(input("Enter the amount to be sent : "))
    
    query = """
    SELECT BALANCE FROM ACCOUNTS WHERE AC_NO = %s
    """
    crsr.execute(query,(sender,))
    bal = crsr.fetchone()
    
    try:
        if bal != None:
            res = bal[0]
            if res >= amount:
                query1 = """
                UPDATE ACCOUNTS SET BALANCE = BALANCE - %s
                WHERE AC_NO = %s
                """
                crsr.execute(query1,(amount,sender))
                
                # Reciever
                
                query2 = """
                UPDATE ACCOUNTS SET BALANCE = BALANCE + %s
                WHERE AC_NO = %s
                """
                crsr.execute(query2,(amount,reciever))
                con.commit()
                print("Money Sucessfully sent")
            else:
                print('Insufficient funds....!')
        else:
            print("Account not found....!")
    except Exception as e:
        con.rollback()
        print('Fund Transfer Failed....!')
        print(e)

def delete_account():
    account = int(input("Enter the account number : "))
    
    query = """
    DELETE FROM ACCOUNTS WHERE AC_NO = %s
    """
    crsr.execute(query,(account,))
    
    if crsr.rowcount > 0:
        con.commit()
        print("Account Deleted Sucessfully....!")
    else:
        print('Account not Found....!')

def view_all_accounts():
    query = """
    SELECT * FROM ACCOUNTS
    """
    crsr.execute(query)
    res = crsr.fetchall()
    
    print('--------- All Account Details---------')
    for r in res:
        print('\n Account Number : ',r[0])
        print('\n Account Holder Name : ',r[1])
        print('\n Initial Amount : ',r[2])
        print('\n Account Balance : ',r[3])
        print('--------------------------------')
    con.commit()

# Interface

print('<------------------- BANK MANAGEMENT SYSTEM ------------------>')

while True:
    print('\n1. CREATE ACCOUNT.')
    print('2. DEPOSIT AMOUNT.')
    print('3. WITHDRAW AMOUNT')
    print('4. CHECK BALANCE.')
    print('5. FUND TRANSFER.')
    print('6. DELETE ACCOUNT.')
    print('7. VIEW ALL ACCOUNTS.')
    print('8. EXIT.')
    
    option = int(input('Enter your option : '))
    
    match (option):
        case 1 : create_account()
        case 2 : deposit()
        case 3 : withdraw()
        case 4 : check_balance()
        case 5 : fund_transfer()
        case 6 : delete_account()
        case 7 : view_all_accounts()
        case 8 :
            print('THANK YOU VISIT AGAIN.....!')
            break
        case _ : print('Invalid Option....!')