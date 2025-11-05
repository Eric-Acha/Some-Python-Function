# oop

class playerCharacter:

    membership = True  # Setting the Class obj attribute

    def __init__(self, name, age):
        if (self.membership): #Passing the class obj attribute

            self.name = name
            self.age = age

    def shout(self):
        print(f'My name is {self.name} and i am {self.age} years old.')
        return 'done'


player1 = playerCharacter('emma', 3)

print(player1.shout())
