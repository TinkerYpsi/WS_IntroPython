import matplotlib.pyplot as plt
import random


class Player:
    def __init__(self, name, health, attacks, move_strengths):
        self.name = name
        self.health = health
        self.attacks = attacks
        self.attack_strengths = move_strengths
        self.alive = True

    def lose_battle(self, health_penalty):
        if self.health - health_penalty <= 0 and self.alive:
            self.alive = False
            self.health = 0
        else:
            self.health -= health_penalty


attacks = ['lightsaber throw']
attack_strengths = [15]
luke = Player("Luke Skywalker", 100, attacks, attack_strengths)

evil_attacks = ['electrocute']
evil_attack_strengths = [20]
vader = Player("Darth Vader", 100, evil_attacks, evil_attack_strengths)

while luke.alive and vader.alive:
    row = ""
    attack = random.randint(0, 1)                               # random number that is 0 or 1
    if attack == 0:                                             # Luke plays Vader
        current_attack = luke.attacks[0]
        current_strength = luke.attack_strengths[0]

        bonus = 20
        die_roll = random.randint(1, 20)
        # Luke wins if he rolls greater than a 5
        if die_roll > 5:
            # make's winner's successful move more powerful next turn
            luke.attack_strengths[0] += bonus
            vader.lose_battle(current_strength)
            print(luke.name + " attacked " + vader.name + " using " + current_attack + "!")
            print(vader.name + " lost " + str(current_strength) + " health!")
            print(luke.name + "'s " + current_attack + " just gained " + str(bonus) + " power!")
        else:
            print(vader.name + " dodged " + luke.name + "'s " + current_attack + " attack!")
            health_bonus = 7
            if vader.health + health_bonus > 100:
                vader.health = 100
                print(vader.name + " has healed to 100 health!")
            else:
                vader.health += (health_bonus * 2)
                print(vader.name + " has gained " + str(health_bonus * 2) + " health!")
            if luke.health + health_bonus > 100:
                luke.health = 100
                print(luke.name + " has healed to 100 health!")
            else:
                luke.health += health_bonus
                print(luke.name + " has gained " + str(health_bonus) + " health!")
    else:
        print("Darth Vader has dodged!")

if luke.alive and not vader.alive:
    print("Luke Skywalker has defeated Lord Vader!")
elif vader.alive and not luke.alive:
    print("Darth Vader has defeated Luke Skywalker!")
