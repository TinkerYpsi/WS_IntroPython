import random

print("Welcome to my game!\n")
userName = input("What is your name? ")
print("\nWelcome, " + userName + "!")

print("\nLet's select a spaceship for you...")
randomSeed = input("Pick a number from 1 to 1000: ")
randomSeed = int(randomSeed)
random.seed(randomSeed)

# Starting ranges for character traits
minInitialHealth = 10
maxInitialHealth = 100
minInitialTrait = 1
maxInitialTrait = 10

# Select random character traits
health = random.randint(minInitialHealth, maxInitialHealth)
fuel = random.randint(minInitialTrait, maxInitialTrait)
dodge = random.randint(minInitialTrait, maxInitialTrait)
firepower = random.randint(minInitialTrait, maxInitialTrait)
luck = random.randint(minInitialTrait, maxInitialTrait)

print("Here's what you got:")
print("Health: " + str(health))
print("Fuel: " + str(fuel))
print("Dodge: " + str(dodge))
print("Firepower: " + str(firepower))
print("Luck: " + str(luck))

# Select random character traits
enemyHealth = random.randint(minInitialHealth, maxInitialHealth)
enemyFuel = random.randint(minInitialTrait, maxInitialTrait)
enemyDodge = random.randint(minInitialTrait, maxInitialTrait)
enemyFirepower = random.randint(minInitialTrait, maxInitialTrait)
enemyLuck = random.randint(minInitialTrait, maxInitialTrait)

print("The galaxy has been under attack and we need you to wipe out some space pirates in Quadrant 4 Section 15")
accept = input("Do you accept the challenge? [Y] or [N]")

if accept == "Y" or accept == "y":
    print("Take off!")
    print("Look, an angry pirate is shooting at us!")
    scan = input("Would you like to scan his ship? [Y] or [N]")
    if scan == "Y" or scan == "y":
        print("Scanning...")
        print("Here's the info for his ship:")
        print("Health: " + str(enemyHealth))
        print("Fuel: " + str(enemyFuel))
        print("Dodge: " + str(enemyDodge))
        print("Firepower: " + str(enemyFirepower))
        print("Luck: " + str(enemyLuck))
        print("Would you like to flee, dodge, or attack?")
        option = input("Press [F] for flee, [D] for dodge, or [A] for attack")
    else:
        print("Would you like to flee, dodge, or attack?")
        option = input("Press [F] for flee, [D] for dodge, or [A] for attack")







