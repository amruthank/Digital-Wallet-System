import transaction

class Wallet:
    def __init__(self, id, amount):
        self.id = id 
        self.amount = amount 
        self.trasactions = []

    def send(self, sender_id, reciever_id, amount):
        print(("Request is to send the amount {2} from user {0} to user {1}.").format(sender_id, reciever_id, amount))
        self.trasactions.append(transaction.Transcation(sender_id, reciever_id, amount, "SENT"))

    def recieve(self, sender_id, reciever_id, amount):
        print("Recieve function is called.")
        self.trasactions.append(transaction.Transcation(sender_id, reciever_id, amount, "RECIEVED")) 

    def getAccountStatement(self, user_id):
        if len(self.trasactions) == 0:
            return "No transaction hostory is found!"
        
        print("*****Displaying transaction history for user*****", user_id)
        for transcation in self.trasactions:
            if transcation.operation == "SENT":
                print(("{0}: Sent from user {1} to user {2} and the amount is {3}.").format(transcation.date, transcation.sender_id, transcation.reciever_id, transcation.amount))
            else:
                print(("{0}: Recieved from user {2} to user {1} and the amount is {3}.").format(transcation.date,transcation.sender_id, transcation.reciever_id, transcation.amount))

    def __str__(self) -> str:
        return "Wallet %s is created."%self.id