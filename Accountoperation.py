accountName = "Ope"
accountBalance = 100
accountPassword = "blessing"
while true:
    operation = print("Hi, hit on any of the buttons below and lets get started")

    print("press b to get the balance")
    print("press d to make a deposit")
    print("press w for withdrawer")
    print("press s to show the account balance")
    print("press q to quit")
    print(" ")
    
    action = input("welcome, what do you want to do")
    action = action.lower()
    action = action(0)
    print(" ")

    if action == "b":
        print("get balance")
        userpassword = input("please enter the account password")
        if userpassword != accountPassword:
            print("incorrect password")
        else:
            print("your account balace is: ", accountBalance)

    elif action == "s":
        print("show the account details")
        userpassword = input("please enter the account password")
        if userpassword != accountPassword:
            print("incorrect password")
        else:
            print("account name: ", accountName)
            print("account balance: ", accountBalance)
            print("account password: ", accountPassword)
    
    elif action == "d":
        print("make a deposit")
        amountToDepsit = input("enter the amount to deposit")
        accountBalance += amountToDeposit #accountBalance = accountBalance+amountToDeposit

    elif action == "w":
        print("withdrawer")
        amountWithdraw = input("How much do you want to withdraw")
        if amountWithdraw < 0:
            print("you cant withdraw a negative amount")
        else:
            if amountWithdraw > accountBalance:
                print("you cant withdraw above your account balance")
        else:
            accountBalance -= amountWithdraw # accountBalance = accounrBalance - amountWithdraw
            print("the new account balance is: ", accounrBalance)

    else:
        break
    print("done")







