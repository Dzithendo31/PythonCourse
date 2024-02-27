from datetime import datetime
class Car:
    #add the values
    def __init__(self, name,engine,doors):
        self.name = name
        self.engine = engine
        self.doors = doors
    
    def horn(self):
        return "Helloe Babbi"
    



ferrari = Car("Benx","V*",23)

print(ferrari.horn())


##Bank Account
class bankAccount():
    def __init__(self, AccNo,AccHolder,balance):
        self.AccountNum = AccNo
        self.Name = AccHolder
        self.balance = balance
        self.transID = 0
        self.trans = []
    
    def displayBalance(self):
        return f"Your Balance is R{self.balance}"
    def withdraw(self,amount):
        
        if amount > self.balance:
            return f"Unsuccesful balance is {self.balance}"
        else:
            #it there, the money is there..
            self.balance = self.balance - amount
            self.trans.append(self.saveTransaction("Withdraw",amount))
            return f"Successful, Balnace is {self.balance}"
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        self.trans.append(self.saveTransaction("Withdraw",amount))
        return f"Successful, Balance is now {self.balance}"
    
    def getBankStatement(self):
        print(f"#  {'id':^6}{'Date':^10}{'Amount':^10}")
        for tran in self.trans:
            print(f"#  {tran['id']:^6}{tran['time']:^10}{tran['amount']:^10}")

    def saveTransaction(self,type,amount):
        #Get the time we got
        item = {}
        item['id'] = self.transID + 1
        item['time'] = f"{datetime.now():%d %b}"
        item['type'] = type
        item['amount'] = amount
        return item



tina = bankAccount(125674234,"Thina",153_000)

#withdraw
tina.withdraw(3000)
tina.withdraw(3000)
tina.getBankStatement()
