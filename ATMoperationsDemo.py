#ATMoperationsDemo.py -->file name or Main program
from ATMExcept import WithDrawError, DepositError, InsufficientFundError
from ATMMenu  import menu
from ATMoperations import deposit, withdraw,balenq

while(True):
    try:
        menu()
        ch = int(input("Enter Your Choice:"))
        match (ch):
            case 1:
                try:
                  deposit()
                except DepositError:
                    print("\tDON'T ENTER NEGATIVE OR ZERO FOR DEPOSIT AMOUNT")
                except ValueError:
                    print("\tDON'T ENTER ALPHANUMERIC,SPECIAL SYMBOLS AND STRINGS")
            case 2:
                try:
                  withdraw()
                except WithDrawError:
                    print("\tDON'T ENTER NEGATIVE OR ZERO FOR WITHDRAW AMOUNT")
                except InsufficientFundError:
                    print("\tYOUR ACCOUNT DOES NOT CONTAINS SUFFICIENT FUNDS")
                except ValueError:
                    print("\tDON'T ENTER ALPHANUMERIC,SPECIAL SYMBOLS AND STRINGS")
            case 3:
                balenq()
            case 4:
                print("\tThanks for using this project")  #EXIT
                break
            case _:
                print("\tYour Selection of Operations is Wrong---try again")
    except ValueError:
        print("\tDon't enter alphanumeric,strings and special symbols for integer choice----TRY AGAIN")