#ATMoperations.py -->file name treated as module name
from ATMExcept import DepositError, WithDrawError, InsufficientFundError

bal=500.0 #global variable
def deposit():
    damt=float(input("Enter Your Deposit Amount:"))  #implicitely PVM may raise ValueError
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt   #when we modify the global variable inside the function definition then we must write 'global' keywords.
        print("\tYour Account xxxxxxxxxxxx123 Credited with INR:{}".format(damt))
        print("\tYour Account xxxxxxxxxxxx123 Bal after Deposit INR:{}".format(bal))

def withdraw():
    global bal #when we modify the global variable inside the function definition then we must write 'global' keywords.
    wamt = float(input("Enter Your Withdraw Amount:"))  #implicitely PVM may raise ValueError
    if(wamt<=0):
        raise WithDrawError
    elif(wamt+500)>bal: #minimum amount required 500
        raise InsufficientFundError
    else:
        bal=bal-wamt
        print("\tYour Account xxxxxxxxxxxx123 Debited with INR:{}".format(wamt))
        print("\tYour Account xxxxxxxxxxxx123 Bal after Withdraw INR:{}".format(bal))

def balenq():
    print("\tYour Account xxxxxxxxxxxx123 Bal INR:{}".format(bal))