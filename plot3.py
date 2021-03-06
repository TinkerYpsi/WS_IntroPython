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

    def play_attack(self, opponent):
        index = random.randint(0, len(self.attacks) - 1)
        current_attack = self.attacks[index]
        current_strength = self.attack_strengths[index]

        bonus = 20
        die_roll = random.randint(1, 20)
        # Luke wins if he rolls greater than a 5
        if die_roll > 5:
            # make's winner's successful move more powerful next turn
            self.attack_strengths[index] += bonus
            vader.lose_battle(current_strength)
            print(self.name + " attacked " + vader.name + " using " + current_attack + "!")
            print(vader.name + " lost " + str(current_strength) + " health!")
            print(self.name + "'s " + current_attack + " just gained " + str(bonus) + " power!")
        else:
            print(vader.name + " dodged " + self.name + "'s " + current_attack + " attack!")
            health_bonus = 7
            if vader.health + health_bonus > 100:
                vader.health = 100
                print(vader.name + " has healed to 100 health!")
            else:
                vader.health += (health_bonus * 2)
                print(vader.name + " has gained " + str(health_bonus * 2) + " health!")
            if self.health + health_bonus > 100:
                self.health = 100
                print(self.name + " has healed to 100 health!")
            else:
                self.health += health_bonus
                print(self.name + " has gained " + str(health_bonus) + " health!")


attacks = ['lightsaber throw', 'slice', 'fast swing', 'RAGE']
attack_strengths = [15, 30, 20, 50]
luke = Player("Luke Skywalker", 100, attacks, attack_strengths)

evil_attacks = ['electrocute', 'choke', 'evil laugh', 'lightsaber slash']
evil_attack_strengths = [20, 20, 15, 50]
vader = Player("Darth Vader", 100, evil_attacks, evil_attack_strengths)
# vader_health_list will be a list of his health after every attack i.e. [100, 70, 30, 0]
vader_health_list = [vader.health]
luke_health_list = [luke.health]
data = []                                   # create empty list to fill with strings containing health and round info
attack_num = 0
attack_list = [attack_num]                  # attack_list will be a list: [0, 1, 2, 3, ... , 23, 24, attack_num]
row = str(attack_num) + "," + str(luke.health) + "," + str(vader.health)
data.append(row)                            # append round 0 info to data

while luke.alive and vader.alive:
    row = ""                                                    # set row back to empty string every turn
    attack = random.randint(0, 1)                               # random number that is 0 or 1
    if attack == 0:                                             # Luke plays Vader
        luke.play_attack(vader)
    else:
        vader.play_attack(luke)
    attack_num += 1
    attack_list.append(attack_num)
    luke_health_list.append(luke.health)
    vader_health_list.append(vader.health)
    row += str(attack_num) + "," + str(luke.health) + "," + str(vader.health)
    data.append(row)

if luke.alive and not vader.alive:
    print("Luke Skywalker has defeated Lord Vader!")
elif vader.alive and not luke.alive:
    print("Darth Vader has defeated Luke Skywalker!")

plt.xlabel('Combat Round')
plt.ylabel('Health')
plt.title('Health over time')
# create an x-axis that goes from 1 to total_attacks
# create a y-axis that goes from 0 to 100
plt.axis([0, attack_num, 0, 100])
# Vader is red circles and Luke is green triangles
plt.plot(attack_list, vader_health_list, 'ro', attack_list, luke_health_list, 'g^')
plt.grid(True)
plt.show()

header = "Round," + luke.name + "," + vader.name
filename = "health_log.csv"
with open(filename, 'w+') as file:
    file.write(header)
    file.write('\n')
    for row in data:
        file.write(row)
        file.write('\n')
file.close()