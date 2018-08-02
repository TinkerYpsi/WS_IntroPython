# **************  Create a class with several variables **************
class Spell(object):

    name = None
    ingredients = set()
    power = None


fireball = Spell()
fireball.name = 'fireball'
fireball.ingredients = {'potato', 'magic water'}
fireball.power = 10

print("Spell Name: ", fireball.name)
print("Ingredients: ", fireball.ingredients)
print("Power: ", fireball.power)


# ************** Initialize variables upon creation **************
class Spell(object):

    def __init__(self, name, ingredients, power):
        self.name = name
        self.ingredients = ingredients
        self.power = power


lightning = Spell('lightning', {'newt', 'sandbag'}, 15)

print("\nSpell Name: ", lightning.name)
print("Ingredients: ", lightning.ingredients)
print("Power: ", lightning.power)


# **************  Add a class function **************
class Spell(object):

    def __init__(self, name, ingredients, power):
        self.name = name
        self.ingredients = ingredients
        self.power = power

    def print_info(self):
        print("\nSpell Name: ", self.name)
        print("Ingredients: ", self.ingredients)
        print("Power: ", self.power)


freeze = Spell('freeze', {'belly button lint', 'magic water'}, 5)
slow = Spell('slow', {'belly button lint', 'newt'}, 2)
freeze.print_info()
slow.print_info()


# **************  Do something with the spell objects **************

# Create a set of all spells in the game
spells = {freeze, slow, fireball, lightning}


# Create a function to determine which spells we can cast and to print them
def print_current_spells(inventory):
    # Create an empty set we will add to in a moment
    current_spells = set()

    # Iterate through all the spells in the game...
    for spell in spells:
        # If myItems contains all the items in the spell ingredients list...
        if spell.ingredients.issubset(inventory):
            #  Add that spell to 'mySpells'
            current_spells.add(spell)

    # Iterate over all your spells and print the name of each
    print("\nSpells you can cast:")
    for spell in current_spells:
        print(spell.name)


# Create a set of items you currently have
myInventory = {'newt', 'belly button lint', 'magic water'}

# Print which spells you can cast with that inventory
print_current_spells(myInventory)

# Remove an item from your inventory and add a new one
print("\nYou dropped some belly button lint")
myInventory.remove('belly button lint')
print("You picked up a sandbag")
myInventory.add('sandbag')

# Print an updated list of spells you can cast
print_current_spells(myInventory)