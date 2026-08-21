
# ATM PROJECT 
# ________________________

Balance = 15000
correct_pin = 1234

print("______ Welcome to the ATM______")

pin = int(input("Enter your 4 digit pin: "))

if correct_pin==pin :
    print("1. Check your balance")
    print("2. Withdraw Amount")
    print("3. deposit Amount")
    print("4. exit")

    Choice = int(input("Enter Your Number: "))
    if Choice == 1 :
        print("Your Balance is:",Balance)

    elif Choice == 2 :
        amount=int(input("Enter Your amount: "))
        if amount<=Balance :
            BAL=Balance-amount
            print("Collect Your cash ")
            print("Your new balance is:", Balance)

        else:
            print("Insufficient Balance")

    elif Choice == 4 :
        Deposit_Amount= int(input("Enter Your amount"))
        if Deposit_Amount >= 0 :
            balance= Balance + Deposit_Amount
            print("Your cash was successfully added")
            print("Your new balalnce is :", balance)

        else:
            print("Invalid amount")

else:
    print("Incorrect PIN")
        
            



    





                

  
  
        




   






        

        
