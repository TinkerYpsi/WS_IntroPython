print("Welcome to Dungeons and Dragoons, the game of Napoleonic Conquest!\n")
userName = input("What is your name? ")

# This works because input from the terminal will be saved as a string
print("\nWelcome, " + userName + "!")

# When requesting numerical input, we need to convert the input to our desired data type
age = int(input("How old is your character? "))
trainingDuration = 4
age += trainingDuration
print("You've just endured", trainingDuration, "years of dragoon training. You are now", age, "years old.")