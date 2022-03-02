class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f"my name is {self.name}")

    def run(self, run):
        print(f"Run like crazy")


player1 = PlayerCharacter("Magic Man", 43)

print(player1.name, player1.age)
print(player1.run('Run'))
