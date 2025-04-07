# To make a variable private in python, add an underscore in front of the variable

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # I can add a method to encapsulate this object

    def greetings(self):
        print(f"Hello {self._name}, you are {self._age} years old.")


player1 = PlayerCharacter('John', 35)

player1.greetings()
