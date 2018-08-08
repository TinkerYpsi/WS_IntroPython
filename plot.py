import matplotlib.pyplot as plt
import random


class Player:
    def __init__(self, name, health, moves, move_strengths):
        self.name = name
        self.health = health
        self.moves = moves
        self.move_strengths = move_strengths
        self.alive = True

    def lose_battle(self, health_penalty):
        if self.health - health_penalty <= 0 and self.alive:
            self.alive = False
            self.health = 0
        else:
            self.health -= health_penalty

    def play_move(self, opponent):
        index = random.randint(0, len(self.moves) - 1)
        current_move = self.moves[index]
        current_strength = self.move_strengths[index]

        bonus = 20
        die_roll = random.randint(1, 20)
        if die_roll > 5:
            self.move_strengths[index] += bonus      # make winner's move more powerful
            opponent.lose_battle(current_strength)
            print(self.name + " attacked " + opponent.name + " using " + current_move + "!")
            print(opponent.name + " lost " + str(current_strength) + " health!")
            print(self.name + "'s " + current_move + " just gained " + str(bonus) + " power!")
            return self
        else:
            print(opponent.name + " dodged your move!")
            health_bonus = 7
            if opponent.health + health_bonus > 100:
                opponent.health = 100
            else:
                opponent.health += (health_bonus * 2)
            if self.health + health_bonus > 100:
                self.health = 100
            else:
                self.health += health_bonus
            return opponent


moves = ['lightsaber throw', 'slice', 'fast swing', 'RAGE']
move_strengths = [15, 30, 20, 50]
luke = Player("Luke", 100, moves, move_strengths)

evil_moves = ['electrocute', 'choke', 'evil laugh', 'lightsaber slash']
evil_move_strengths = [20, 20, 15, 50]
vader = Player("Darth Vader", 100, evil_moves, evil_move_strengths)

move_num = 0
move_list = [move_num]                          # move_list will be a list: [0, 1, 2, 3, ... , 23, 24, move_num]
# vader_health_list will be a list of his health after every move i.e. [100, 70, 30, 0]
vader_health_list = [vader.health]
luke_health_list = [luke.health]
while luke.alive and vader.alive:
    move = random.randint(0, 1)
    if move == 0:
        winner = luke.play_move(vader)
    else:
        winner = vader.play_move(luke)
    move_num += 1
    move_list.append(move_num)                  # append a new number to move_list every move
    luke_health_list.append(luke.health)        # append luke's current health to his health list
    vader_health_list.append(vader.health)      # append vader's current health to his health list

if luke.alive and not vader.alive:
    print("Luke Skywalker has defeated Lord Vader!")
elif vader.alive and not luke.alive:
    print("Darth Vader has defeated Luke Skywalker!")

plt.xlabel('Moves')
plt.ylabel('Health')
plt.title('Health over time')
# create an x-axis that goes from 1 to total_moves
# create a y-axis that goes from 0 to 100
plt.axis([1, move_num, 0, 100])
# Vader is red circles and Luke is green triangles
plt.plot(move_list, vader_health_list, 'ro', move_list, luke_health_list, 'g^')
plt.grid(True)
plt.show()