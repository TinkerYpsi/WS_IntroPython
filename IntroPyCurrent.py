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
