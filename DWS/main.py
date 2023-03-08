import sys
import digitalWalletSystem

if __name__ == "__main__":

    print("Press 1 to create a Digital Wallet System.")
    print("Press 2 to create a user with firstName, lastName and amount.")
    print("Press 3 to get the system overview.")
    print("Press 4 to transfer amount.")
    print("Press 5 to get the user account statement.")
    print("Press 6 to exit the system.")

    dws = None
    while True:
        value = input("Enter your option: ")

        if not dws and int(value) not in [1, 5]: 
                print("You have to create your system before trying to add an user!")
                continue
        
        if int(value) == 1:
            print("Hey, this is a digital wallet system.")
            dws = digitalWalletSystem.DigitalWalletSystem.getInstance()
            print(dws)
        elif int(value) == 2:
            firstName = input("Enter your firstName: ")
            lastName = input("Enter your lastName: ")
            amount = input("Enter your amount: ")
            dws.createUser(firstName, lastName, int(amount))
            print(dws.users, dws.wallets)
        elif int(value) == 3:
            dws.getOverview()
        elif int(value) == 4:
             sender_id =  input("Enter your senderID: ")
             reciever_id = input("Enter your recieverID: ")
             amount = input("Enter your amount: ")
             dws.sendMoney(int(sender_id), int(reciever_id), int(amount))
        elif int(value) == 5:
            user_id =  input("Enter your userID: ")
            dws.getAccountStatement(int(user_id))
        elif int(value) == 6:
            sys.exit(0)
    