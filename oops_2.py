# inheritance
class User():
    def __init__(self, name, email):
        self.name = name
        self._email = email

    # prints username
    def printUserName(self):
        print(f"username:{self.name}")

class Wizard(User):
    def __init__(self,name, email, power="Fireball"):

        # passing values to parent class using super()
        super().__init__(name, email)
        self._power = power

    def Attack(self):
        print(f"Attacking with {self._power}")

class Archer(User):
    def __init__(self,name, email, power="Arrows"):

        # alternate method to pass values to parent class
        User.__init__(self, name, email)
        # super().__init__(name, email)
        self._power = power

    def Attack(self):
        print(f"Attacking with {self._power}")

# lets create a player 1 named james108 and assign wizard power
player_1 = Wizard("james108","james@email.com")

player_1.printUserName() # username:james108
player_1.Attack() # Attacking with Fireball

# lets create a player 2 named ram007 and assign wizard power
player_2 = Archer("ram007","ram@email.com")

player_2.printUserName() # username:ram007
player_2.Attack() # Attacking with Arrows

    