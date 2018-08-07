import os.path
import sys


class Player:
    def __init__(self, name, health=100, xp=0, habits=[]):
        self.name = name
        self.health = health
        self.xp = xp
        self.habits = habits
        self.successes = [0] * len(habits)
        self.failures = [0] * len(habits)
        self.alive = True

    # frequency is number of times per week habit should be done
    def add_habit(self, habit_name=""):
        if habit_name == "":
            habit_name = input("New habit description: ")
        self.habits.append(habit_name)
        self.successes.append(0)
        self.failures.append(0)

    def check_habit(self, habit, status):
        index = get_index(self, habit)
        if index == -1:
            print("ERROR: Habit not found!")
            return

        health_bonus = 5
        health_penalty = 10
        xp_bonus = 5
        xp_penalty = 10
        if status == True:
            self.successes[index] += 1
            self.xp += xp_bonus
            if self.health + health_bonus >= 100:
                self.health = 100
                # extra XP bonus is awarded if player maintains 100 health
                self.xp += xp_bonus
            else:
                self.health += health_bonus
        else:
            self.failures[index] += 1
            self.xp -= xp_penalty
            if self.health - health_penalty <= 0:
                self.alive = False
                self.xp = 0
            else:
                self.health -= health_penalty

    def print_basic_stats(self):
        print("NAME: " + self.name)
        print("HEALTH: " + str(self.health))
        print("XP: " + str(self.xp))

        total_success = 0
        total_failure = 0
        for success in self.successes:
            total_success += success
        for failure in self.failures:
            total_failure += failure
        print("TOTAL SUCCESSES: " + str(total_success))
        print("TOTAL FAILURES: " + str(total_failure))

        success_ratio = total_success / (total_success + total_failure)
        print("CONSISTENCY: " + str(success_ratio) + "%\n")

    def get_data(self, log_exists=False):
        num_habits = len(self.habits)

        # adds a header row if log doesn't already exists
        if not log_exists:
            header = "Habit,Successes,Failures,Consistency"
            data = [None] * num_habits + 1
            data[0] = header
        else:
            data = [None] * num_habits


        # iterate through all habits
        for habit in range(0, num_habits):
            index = get_index(self, habit)
            row = ""
            row += habit
            row += ","
            num_successes = self.successes[index]
            row += str(num_successes)
            row += ","
            num_failures = self.failures[index]
            row += str(num_failures)
            success_ratio = num_successes / (num_successes + num_failures)
            row += success_ratio
            data[index] = row

        return data

    def log_habits(self):
        for habit in self.habits:
            answered = False
            while not answered:
                habit_status = input("Did you do " + habit + " today?  [Y] or [N]   ")
                if habit_status == 'Y' or habit_status == 'y':
                    self.check_habit(habit, True)
                    answered = True
                if habit_status == 'N' or habit_status == 'n':
                    self.check_habit(habit, False)
                    answered = True
                else:
                    print("Be sure to type either [Y] or [N] as your answer.")






def get_index(player, habit):
    location = 0
    for index in player.habits:
        if index == habit:
            return location
        else:
            location += 1

    # sentinel to indicate that 'habit' is not in the player's list of habits
    return -1


# create new player with 0 XP and no habits
player = Player("Patrick")
looping = True
while looping:
    print("Hi there", player.name)
    decision = input("Please press [1] to log habits, [2] to add a habit, [3] to see your stats, or [4] to quit: ")
    log = 1
    add = 2
    stats = 3
    quit = 4
    while decision != log or decision != add or decision != quit:
        if decision == log:
            player.log_habits()
        if decision == add:
            player.add_habit()
        if decision == stats:
            player.print_basic_stats()
        if decision == quit:
            sys.exit(0)
        else:
            print("Incorrect usage!")
            decision = input("Please press [1] to log habits, [2] to add a habit, [3] to see your stats, or [4] to quit: ")


    filename = 'habit_log.csv'
    path = "C:/User/Documents/WS_IntroPython/habit_log.csv"
    path += str(filename)
    log_exists = os.path.isfile(filename)
    if log_exists:
        # data is a List of strings to be written to file
        data = player.get_data(log_exists)

    # w+ means that we will write to the csv file
    # and create one if 'habit_log.csv' doesn't already exist
    with open(filename,'w+') as file:
        for line in data:
            file.write(line)
            file.write('\n')
    file.close()

    print("Nice :)")
    print("Would you like to do something else or leave?")
    decision = input("Please press [1] to leave or any button to stay")
    leave = 1
    if decision == leave:
        looping = False