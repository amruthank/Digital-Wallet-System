import wallet

class User:
    def __init__(self, count, first_name, last_name, amount):
        self.id = count 
        self.name = first_name+" "+last_name
        self.walletObj = wallet.Wallet(self.id, amount)
    
    def __str__(self) -> str:
        return "User %s is created."%self.id

    
    
