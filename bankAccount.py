from datetime import datetime


class bankAccount:
    intrestRate = 0.02
    Customer = 0

    def __init__(self, AccNo, AccHolder, balance):
        self.AccountNum = AccNo
        self.Name = AccHolder
        self.__balance = balance
        self.transID = 0
        self.trans = []
        bankAccount.Customer += 1

    @classmethod
    def updateInterest(cls, rate):
        bankAccount.intrestRate = rate

    @classmethod
    def getTotalAccounts(cls):
        return bankAccount.Customer

    @staticmethod
    # They don't take clas nor self
    # why use static methods:
    # methods that are bound to a class rather than an instance of the class.

    def displayBalance(self):
        return f"Your Balance is R{self.__balance}"

    def withdraw(self, amount):

        if amount > self.__balance:
            return f"Unsuccesful balance is {self.__balance}"
        else:
            # it there, the money is there..
            self.__balance = self.__balance - amount
            self.trans.append(self.saveTransaction("Withdraw", amount))
            return f"Successful, {self.displayBalance(self)}"

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        self.trans.append(self.saveTransaction("Withdraw", amount))
        return f"Successful, {self.displayBalance(self)}"

    def getBankStatement(self):
        print(self.Name)
        print(f"#  {'id':^6}{'Date':^10}{'Amount':^10}")
        for tran in self.trans:
            print(f"#  {tran['id']:^6}{tran['time']:^10}{tran['amount']:^10}")
        print(f"\n{'Balance:':#>16}{self.__balance:>10}\n\n")

    def saveTransaction(self, type, amount):
        # Get the time we got
        item = {}
        item["id"] = self.transID + 1
        item["time"] = f"{datetime.now():%d %b}"
        item["type"] = type
        item["amount"] = amount
        return item

    def applyIntrest(self):
        self.__balance = self.__balance + self.__balance * self.intrestRate

    # get and Sets
    def getBalance(self):
        return self.__balance

    def updateBalance(self, amount):
        self.__balance += amount


# create more
# Savings Account
# - More intrest for you
# - 0.05
# -
# Checking Account
# - Higer intrest Rate
# - There is a transaction fee
# - R1 per trans


class savingsAccount(bankAccount):
    intrestRate = 0.05

    # def __init__(self, AccNo, AccHolder, balance):
    #     super().__init__(AccNo, AccHolder, balance)

    # def applyIntrest(self):
    #     self.__balance = self.__balance + self.__balance * savingsAccount.intrestRate


class checkingAccount(bankAccount):
    def __init__(self, AccNo, AccHolder, balance):
        super().__init__(AccNo, AccHolder, balance)

    def withdraw(self, amount):
        self.chargeFee()
        return super().withdraw(amount)

    def deposit(self, amount):
        self.chargeFee()
        return super().deposit(amount)

    def chargeFee(self):
        self._bankAccount__balance -= 17


def main():
    tina = bankAccount(125674234, "Thina", 100_000)

    tinaX = savingsAccount(12567422344, "Sara", 100_000)

    tinaXR = checkingAccount(125674223, "John", 100_000)
    # Task 01
    tina.applyIntrest()
    tinaX.applyIntrest()
    tinaXR.applyIntrest()
    tina.getBankStatement()
    tinaXR.getBankStatement()
    tinaX.getBankStatement()

    # withdraw
    tina.withdraw(3000)
    tinaX.withdraw(3000)
    tinaXR.withdraw(3000)
    tina.getBankStatement()
    tinaX.getBankStatement()
    tinaXR.getBankStatement()
    print(bankAccount.getTotalAccounts())


main()
