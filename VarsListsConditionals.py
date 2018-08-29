# Create some player stats
name = "Garf"   # Name (string)
age = 135       # Age in years (int)
height = 2.3    # Height in meters (float)

# Print our character's stats
print("Hello world, my name is " + name + ", I'm " + str(age) + " years old and I'm " + str(height) + " meters tall.")

# Let's age our character a few years
print("Old age:", age)
age += 5
# Notice that we didn't need to use str() to convert "age" when using this print syntax
print("New age:", age)

# Maybe our character has taken some magic growing potion
print("Old height:", height, "m")
height *= 1.5
print("New height:", round(height, 2), "m")

# Put some inventory into containers
backpack = {"cat", "baseball bat", "star dust"}  # This is a set because it is unordered and contains no duplicates
utilityBelt = ["knife", "string", "knife", "dog"]  # This is a list because it has an order and may contain duplicates

# Print the contents of our backpack
print("\nMy backpack contains:")
print(backpack)

# When printing the contents of a set or a list, you may use the syntax,
# for [variable to hold each element] in [array or set]:
for item in backpack:
    print(item)

# Print the contents of our utility belt
print("\nItems in my utility belt:")
for item in utilityBelt:
    print(item)

# Create a new container and put our other containers inside it
# The wooden chest is a list that contains mixed item types: it
# has a set (backpack) and a list (utilityBelt)
woodenChest = [backpack, utilityBelt]

print("\nThings in my wooden chest:")
for item in woodenChest:
    print(item)

# Print just the first two items in the utility belt
print("\nFirst two items in the utility belt:")
# To do this, we pick an iterator variable (can be called anything, but we'll call it "i"),
# and we'll have  increment within a specified range. The "for" loop will execute while the
# iterator variable is less than the maximum value of the "range" function. In other words,
# "i" will increment by 1 after each loop and the loop will continue executing until the
# iterator equals the maximum value.
for i in range(0, 2):
    print(utilityBelt[i])

# Print just the first two items in the backpack
# BUT... this doesn't work because sets don't have an order to them
print("\nFirst two items in the utility belt:")
for i in range(0, 2):
    print(backpack[i])
