# For this example, we'll need to generate some random numbers. Random functions are not part of the base language,
# so we need to import the "random" module. If you've used other programming languages, modules are the Python
# equivalent to "libraries" in C/C++ and "packages" in Java. Essentially, they give us extra functions that extend
# the basic functionality of the language.
import random
# "random.seed()" initializes the random number generator with a "seed" value to generate all subsequent values from.
# If you want the same results each time you run the program, you can seed the random number generator with a fixed
# value. Because the numbers are generated based upon an algorithm, if you provide the same starting point, the list
# of values generated from that starting point will always be the same. This can sometimes be useful for testing, but
# we won't do that here.
random.seed()

# **************  Create a character and a monster**************
cName = "Jiggly Jim"
cHealth = 25
cStrength = 4
cDexterity = 10

mName = "slime ball"
mHealth = 20
mStrength = 6
mDexterity = 8

# We've seen in some other examples that you can concatenate (combine) strings and variables by separating them
# with commas as arguments to the "print" function. When you do this, by default, Python will add a space between
# each item. In this case, we don't want to add a space between the character's / the monster's name and and the
# possessive apostrophe, so we can add sep='' as our final argument to specify no separating character. When we do that,
# however, we'll have to remember to manually add a space at the end of the string to maintain separation from the
# cHealth / mHealth variable that follows it.
print(cName, "'s health: ", cHealth, sep='')
print(mName, "'s health: ", mHealth, "\n", sep='')

print("Doing combat!\n")

# Roll a die
# Unlike "range()", which, in practice, is exclusive of the maximum value provided, "random.randomint([min], [max])
# will generate a value between the minimum and maximum, including the minimum and maximum values.
dieRoll = random.randint(1, 20)

# If the roll is higher than the monster's dexterity, score a hit
if dieRoll > mDexterity:
    mHealth -= cStrength

# Roll a die
dieRoll = random.randint(1, 20)

# If the roll is higher than the character's dexterity, score a hit
if dieRoll > mDexterity:
    cHealth -= mStrength

print(cName, "'s health: ", cHealth, sep='')
print(mName, "'s health: ", mHealth, "\n", sep='')


# We'll want to perform multiple rounds of combat, so we can create a function that allows us to run that code
# multiple times without having to copy it multiple times.
def do_combat():
    global cName
    global cHealth
    global cStrength
    global cDexterity
    global mName
    global mHealth
    global mStrength
    global mDexterity

    print("Doing combat!")

    # Roll a die
    die_roll = random.randint(1, 20)

    # If the roll is higher than the monster's dexterity, score a hit
    if die_roll > mDexterity:
        mHealth -= cStrength

    # Roll a die
    die_roll = random.randint(1, 20)

    # If the roll is higher than the character's dexterity, score a hit
    if die_roll > mDexterity:
        cHealth -= mStrength

    print(cName, "'s health: ", cHealth, sep='')
    print(mName, "'s health: ", mHealth, "\n", sep='')


# We want to run the combat function until our character or the monster's health is less than or equal to zero
while cHealth >= 0 and mHealth >= 0:
    do_combat()

# Depending on who won the battle, print a different message
if cHealth > 0:
    print(cName, " is victorious over the ", mName, "!", sep='')
else:
    print(cName, " has been slain by the ", mName, "!", sep='')
