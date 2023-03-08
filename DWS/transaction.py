import random
import datetime

class Transcation:
    def __init__(self, sender_id, reciever_id, amount, operation = "SENT"):
        self.id = random.randint(0, 1000) 
        self.sender_id = sender_id
        self.reciever_id = reciever_id
        self.amount = amount
        self.date = datetime.datetime.now()
        self.operation = operation  # RECIEVED

    def __str__(self) -> str:
        return "Transaction %s is created."%self.id
