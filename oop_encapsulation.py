# Encapsulation

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # I can add a method to encapsulate this object

    def greetings(self):
        print(f"Hello {self.name}, you are {self.age} years old.")


player1 = PlayerCharacter('John', 35)

player1.greetings()
