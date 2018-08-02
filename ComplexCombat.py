import random
random.seed()


# **************  Create a creature class **************
class Creature(object):

    def __init__(self, name, creature_type):

        # Players and monsters will have different stats ranges
        if creature_type == 'player':
            min_health = 20
            max_health = 40
            min_trait = 3
            max_trait = 10
        else:
            min_health = 5
            max_health = 25
            min_trait = 1
            max_trait = 6

        # Assign the variables given in the constructor to the object's internal variables
        self.name = name
        self.health = random.randint(min_health, max_health)
        self.strength = random.randint(min_trait, max_trait)
        self.dexterity = random.randint(min_trait, max_trait)

    # A function that will print the player or monster's stats
    def print_stats(self):
        print("Name:", self.name)
        print("Health:", self.health)
        print("Strength:", self.strength)
        print("Dexterity:", self.dexterity, "\n")


# Create a player
player = Creature('Jiggly Jim', 'player')
player.print_stats()

# monster1 = Creature('slime ball', 'monster')
# monster2 = Creature('sentient shrub', 'monster')
# monster3 = Creature('rabid mongoose', 'monster')

monsters = [Creature('slime ball', 'monster'),
            Creature('sentient shrub', 'monster'),
            Creature('rabid mongoose', 'monster')]

for monster in monsters:
    monster.print_stats()


def do_combat(this_player, this_monster):

    print("You have encountered a ", this_monster.name, sep='')
    combat_round = 1
    while this_player.health > 0 and this_monster.health > 0:
        print("\nRound", combat_round)
        print(this_player.name, "'s health: ", this_player.health, sep='')
        print(this_monster.name, "'s health: ", this_monster.health, "\n", sep='')

        # Roll a die
        die_roll = random.randint(1, 20)

        # If the roll is higher than the monster's dexterity, score a hit
        if die_roll > this_monster.dexterity:
            print("You hit the monster!")
            this_monster.health -= this_player.strength
        else:
            print("The monster dodged your attack!")

        # Roll a die
        die_roll = random.randint(1, 20)

        # If the roll is higher than the character's dexterity, score a hit
        if die_roll > this_player.dexterity:
            print("You've been hit!")
            this_player.health -= this_monster.strength
        else:
            print("You dodged the monster!")

        combat_round += 1

    # End the battle
    print("\nEnd battle!")
    print(this_player.name, "'s health: ", this_player.health, sep='')
    print(this_monster.name, "'s health: ", this_monster.health, "\n", sep='')

    if this_player.health > 0:
        print(this_player.name, " is victorious over the ", this_monster.name, "!\n", sep='')
        return True
    else:
        print(this_player.name, " has been slain by the ", this_monster.name, "!\n", sep='')
        return False


while len(monsters) > 0:
    # Do combat with the first monster in the list
    player_won = do_combat(player, monsters[0])

    if player_won:
        # Remove the first monster in the list. All other monsters move forward one place
        monsters.pop(0)
    else:
        print("You're dead. The game is over. Go home")
        quit()

print("Success! You have slain all the monsters!")