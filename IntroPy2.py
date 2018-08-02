import random

print("Welcome to my game!\n")
userName = input("What is your name? ")
print("\nWelcome, " + userName + "!")

print("\nLet's select some character stats for you...")
randomSeed = input("Pick a number from 1 to 1000: ")
randomSeed = int(randomSeed)
random.seed(randomSeed)

# Starting ranges for character traits
minInitialHealth = 10
maxInitialHealth = 30
minInitialTrait = 1
maxInitialTrait = 10

# Select random character traits
health = random.randint(minInitialHealth, maxInitialHealth)
charisma = random.randint(minInitialTrait, maxInitialTrait)
strength = random.randint(minInitialTrait, maxInitialTrait)
dexterity = random.randint(minInitialTrait, maxInitialTrait)
intelligence = random.randint(minInitialTrait, maxInitialTrait)

print("Here's how you turned out:")
print("Health: " + str(health))
print("Charisma: " + str(charisma))
print("Strength: " + str(strength))
print("Dexterity: " + str(dexterity))
print("Intelligence: " + str(intelligence))

move = input("Would you like to attack, charm, manipulate, or run away?")
print("Heads or tails?")
guess = input("H or T:")
if guess is "H":
    guess = int(1)
else:
    guess = int(0)
chance = random.randomint(0, 1)
if guess == 1:
    if chance == 1:
        print("Heads! You guessed correctly!")
    else:
        print("Oof! It was tails.")
else if guess == 0:
    if chance == 0:
        print("Tails! You guessed correctly!")
    else:
        print("Oof! It was heads.")

randomNum = random.randomint(1, 10)

if move == "run away":
    if dexterity > oppDexterity:
        if guess == chance:
            if randomNum > 3:
                print("With your clearly superior dexterity, you managed to outmaneuver your opponent")
                print("+2 dexterity")
                print("+2 health")
                dexterity += 2
                health += 2
            else:
                print("Even with your greater dexterity and luck, you managed to trip and fall :(")
                print("-2 health")
                health -= 2
        else:
            if randomNum > 7:
                print("You defied the odds! Even with your terrible luck, you outran your opponent")
                print("+1 dexterity")
                dexterity += 1
            else:
                print("Today is not your lucky day. While running away, you slipped and hit your head on the table")
                print("-15 health")
                health -= 15
    else:
        if guess == chance:
            if randomNum > 7:
                print("Today is clearly your lucky day. Even though your opponent has the legs of a cheetah, you managed to outmaneuver him. Well done!")
                print("+2 dexterity")
                print("+5 health")
                dexterity += 2
                health += 5
            else:
                print("It almost looked like you were getting away, but then you tripped on a cord and now you have a black eye :(")
                print("-5 health")
                health -= 5
