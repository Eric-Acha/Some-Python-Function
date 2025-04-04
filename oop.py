# oop

class playerCharacter:

    membership = True  # Class obj attribute

    def __init__(self, name, age):
        if (self.membership):

            self.name = name
            self.age = age

    def shout(self):
        print(f"My name is {self.name} and i am {self.age} years old.")


player1 = playerCharacter('eric', 33)
player2 = playerCharacter('emma', 3)
player1.attack = 30
player2.attack = 100

print(player1.attack)
print(player2.attack)
print(player1.shout())
print(player2.shout())
print(player1.membership)
print(player2.membership)
