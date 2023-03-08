import user


class DigitalWalletSystem:
    __instance = None

    def __init__(self):
        self.users = {}
        self.wallets = {}
        self.counter = 0

    #Making it singletone 
    @staticmethod
    def getInstance():
        if DigitalWalletSystem.__instance == None:
            DigitalWalletSystem.__instance = DigitalWalletSystem()
        else:
            print("You have already created a system!")
        return DigitalWalletSystem.__instance

    def createUser(self, first_name, last_name, amount=100):
        print(("Request to create a user: {0} {1}.").format(first_name, last_name))
        self.counter += 1
        userObj = user.User(self.counter, first_name, last_name, amount)
        self.users[self.counter] = userObj
        self.wallets[self.counter] = userObj.walletObj

    def getAccountStatement(self, user_id):
        print("Request to get the account statement.")
        if self.users.get(user_id, None) == None: 
            print("Invalid user ID")
            return
        return self.wallets.get(user_id).getAccountStatement(user_id)

    def getOverview(self):
        print("Get the overview of the system.")
        if not self.wallets:
            print("Empty wallet")
        else:
            for id, obj in self.wallets.items():
                print(("Wallet with ID: {0}, Amount: {1}.").format(id, obj.amount))

    def sendMoney(self, sender_id, reciever_id, amount):
        if amount < 0: # Validate amount.
            print("Invalid amount!")
            return
        if self.users.get(sender_id, None) == None: # Validate sender ID.
            print("Invalid sender!")
            return
        if self.users.get(reciever_id, None) == None: #Validate reciever ID.
            print("Invalid reciever!")
            return 

        walletsenderObj = self.wallets.get(sender_id)
        if walletsenderObj.amount < amount: # Check for the requested amount.
            print("Insufficient amount!")
            return
        walletsenderObj.amount = walletsenderObj.amount-amount
        walletsenderObj.send(sender_id, reciever_id, amount)

        walletrecObj = self.wallets.get(reciever_id)
        walletrecObj.amount = walletrecObj.amount+amount
        walletrecObj.recieve(sender_id, reciever_id, amount)

