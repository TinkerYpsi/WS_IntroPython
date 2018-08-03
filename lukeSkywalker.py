import random
import time


class Player:
    def __init__(self):
        minInitialHealth = 1
        maxInitialHealth = 100
        minInitialTrait = 1
        maxInitialTrait = 100

        self.health = random.randint(minInitialHealth, maxInitialHealth)
        self.fuel = random.randint(minInitialTrait, maxInitialTrait)
        self.dodge = random.randint(minInitialTrait, maxInitialTrait)
        self.firepower = random.randint(minInitialTrait, maxInitialTrait)
        self.luck = random.randint(minInitialTrait, maxInitialTrait)

    def print_stats(self):
        print("Health: " + str(self.health) + "/100")
        print("Fuel: " + str(self.fuel) + "/100")
        print("Dodge: " + str(self.dodge) + "/100")
        print("Firepower: " + str(self.firepower) + "/100")
        print("Luck: " + str(self.luck) + "/100")

    def set_stats(self, health="0", fuel="0", dodge="0", firepower="0", luck="0"):
        self.health += health
        self.fuel += fuel
        self.dodge += dodge
        self.firepower += firepower
        self.luck += luck
        self.checkBoundaries()

    def check_boundaries(self):
        if self.health > 100:
            self.health = 100
        if self.health < 0:
            self.health = 0
        if self.fuel > 100:
            self.fuel = 100
        if self.fuel < 0:
            self.fuel = 0
        if self.dodge > 100:
            self.dodge = 100
        if self.dodge < 0:
            self.dodge = 0
        if self.firepower > 100:
            self.firepower = 100
        if self.firepower < 0:
            self.firepower = 0
        if self.luck > 100:
            self.luck = 100
        if self.luck < 0:
            self.luck = 0


# biased coin that has luck % of being heads and (100 - luck) % of being false
def flip_coin(luck):
    num = random.randint(0, 100)
    if num < luck:
        return True
    else:
        return False

human = Player()
luke = Player()
luke.name = luke
delay = 2
human.name = input("Hi, I'm Luke, what's your name? ")
print("\nHi there, " + human.name + "!")
time.sleep(delay)

print("\nLet's get a spaceship for you...")
time.sleep(delay)
print("Here's what you got:")
human.printStats()
time.sleep(delay)
answer = input("Ready to fight those space pirates? [Y] or [N]  ")
time.sleep(delay)
if answer == "Y":
    print("Great, let's do this!")
else:
    print("Sergeant, code red! CODE REEEED!! PIRATES ARE EVERYWHERE! ALL HANDS ON DECK")
    print("Well, you head the man " + human.name + ". There's no turning back now!")

while human.health > 0:
    minimumDistance = 10
    maximumDistance = 10000
    randomDistance = random.randint(minimumDistance, maximumDistance)
    print("LOOK! A pirate", randomDistance, "clicks ahead!")
    time.sleep(delay)
    print("Would you like to flee, dodge, or attack?")
    option = input("Press [F] for flee, [D] for dodge, or [A] for attack  ")
    if option == "F":
        chance = flipCoin(human.luck)
        if chance == True:
            print("We escaped with minor damage. Good call, that guy was too much for us to handle.")
            print("-5 damage")
            print("+10 dodge")
            print("-5 fuel")
            human.health = human.changePoints(human.health, -5)
            human.dodge = human.changePoints(human.dodge, 10)
            human.fuel = human.changePoints(human.fuel, -5)
        else:
            print("Oof, we took some big blows before we got out of there, " + human.name)
            time.sleep(delay)
            print("-15 damage")
            print("-5 dodge")
            print("-5 luck")
            human.changePnts(health="-15", dodge="-5", luck="-5")
            luke.changePnts(health="-15", dodge="-5", luck="-5")
    if option == "D":
        chance1 = flipCoin(human.luck)
        chance2 = flipCoin(human.dodge)
        chance3 = flipCoin(100 - human.fuel)
        if chance1 and chance2 and chance3:
            print()






