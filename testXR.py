#Question 10
# Setup Code
# Expected Task: Implement a class with methods for casting spells, reducing health points, and determining the winner.

class WizardDuel:
    def __init__(self,name) -> None:
        self.name = name
        self.__health = 100
    def decreaseHealth(self,number):
        self.__health -= number

    @staticmethod
    def spell1(Wizard):
        #Spell reduces by 10
        Wizard.decreaseHealth(10)
        print(Wizard)
    @staticmethod
    def spell2(Wizard):
        #Spell reduces by 20
        Wizard.decreaseHealth(20)
        print(Wizard)
    @staticmethod
    def spell3(Wizard):
        #Spell reduces by 50
        Wizard.decreaseHealth(50)
        print(Wizard)
    def __str__(self) -> str:
        return f"{self.name} has {self.__health} health left."
    def checkHealth(self):
        if self.__health<= 0:
            return False
    def won(self):
        return f"{self.name} wins with {self.__health} health points left."
    
#The duel Start
Harry = WizardDuel('Harry')
Draco = WizardDuel('Drace')
print(Harry," ",Harry)

#They start fighting
Harry.spell1(Draco)
print(Draco)
#Darco fight back Twice
Draco.spell3(Harry)
Draco.spell3(Harry)

if not(Harry.checkHealth()):
    print(f"After a duel between Harry and Draco, {Draco.won()}")