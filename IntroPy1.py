import random

print("Welcome to my game!\n")
userName = input("What is your name? ")
print("\nWelcome, " + userName + "!")

print("\nLet's select some character stats for you...")
randomSeed = input("Pick a number from 1 to 1000: ")
randomSeed = int(randomSeed)
random.seed(randomSeed)

# Select random character traits
health = random.randint(10, 30)
charisma = random.randint(1, 10)
strength = random.randint(1, 10)
dexterity = random.randint(1, 10)
intelligence = random.randint(1, 10)


