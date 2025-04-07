class User:  # parent class
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('Do nothing')


class Wizard(User):  # child class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        # by adding User here, it will enable it to be called by wizard
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):  # child class
    def __init__(self, name, num_arrows):
        self.name = name

        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

# I can define another function and give it the attack method


def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)

# Another way to demonstrate this is by using a for loop

for char in [wizard1, archer1]:
    char.attack()
