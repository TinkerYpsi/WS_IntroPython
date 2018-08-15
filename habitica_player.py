import csv
import time

def get_index(player, habit):
    location = 0
    for index in player.habits:
        if index == habit:
            return location
        else:
            location += 1

    # sentinel to indicate that 'habit' is not in the player's list of habits
    return -1



class Player:
    def __init__(self, name, health=100, xp=0):
        self.name = name
        self.health = health
        self.xp = xp
        self.habits = []
        self.successes = []
        self.failures = []
        self.consistency = []
        self.total_success = 0
        self.total_failure = 0
        self.total_consistency = 0
        self.alive = True

    # frequency is number of times per week habit should be done
    def add_habit(self, habit_name=""):
        while habit_name == "":
            habit_name = input("New habit description: ")
        self.habits.append(habit_name)
        self.successes.append(0)
        self.failures.append(0)
        self.consistency.append(0)
        print("Added habit!")

    def check_habit(self, habit, success):
        index = get_index(self, habit)
        if index == -1:
            print("ERROR: Habit not found!")
            return

        health_bonus = 5
        health_penalty = 10
        xp_bonus = 5
        xp_penalty = 10
        if success:
            self.successes[index] += 1
            self.total_success += 1
            self.update_total_consistency()
            self.consistency[index] = (self.successes[index] / (self.successes[index] + self.failures[index])) * 100
            self.xp += xp_bonus
            if self.health + health_bonus >= 100:
                self.health = 100
                # extra XP bonus is awarded if player maintains 100 health
                self.xp += xp_bonus
            else:
                self.health += health_bonus
        else:
            self.failures[index] += 1
            self.total_failure += 1
            self.update_total_consistency()
            self.consistency[index] = (self.failures[index] / (self.successes[index] + self.failures[index])) * 100
            self.xp -= xp_penalty
            if self.health - health_penalty <= 0:
                self.alive = False
                self.xp = 0
            else:
                self.health -= health_penalty

    def update_total_consistency(self):
        if self.total_success + self.total_failure == 0:
            self.total_consistency = 0
        else:
            self.total_consistency = (self.total_success / (self.total_success + self.total_failure)) * 100

    def get_basic_stats(self):
        header = "Name,Health,XP,Total Success,Total Failure,Overall Consistency"
        data = [header]
        row = ""
        row += self.name + ","
        row += str(self.health) + ","
        row += str(self.xp) + ","
        row += str(self.total_success) + ","
        row += str(self.total_failure) + ","
        row += str(self.total_consistency)
        data.append(row)
        return data

    def print_basic_stats(self):
        print("NAME: " + self.name)
        print("HEALTH: " + str(self.health))
        print("XP: " + str(self.xp))
        print("TOTAL SUCCESSES: " + str(self.total_success))
        print("TOTAL FAILURES: " + str(self.total_failure))
        print("CONSISTENCY: " + str(self.total_consistency) + "%\n")

    def get_details(self):
        header = "Habit,Successes,Failures,Consistency"
        data = [header]
        # iterate through all habits
        for habit in self.habits:
            i = get_index(self, habit)
            row = ""
            row += str(habit) + ","
            row += str(self.successes[i]) + ","
            row += str(self.failures[i]) + ","
            row += str(self.consistency[i])
            data.append(row)
        return data

    def delete_all_habit_data(self):
        self.habits = []
        self.successes = []
        self.failures = []
        self.consistency = []

    def read_log(self, path):
        try:
            file = open(path, "r")
        except FileNotFoundError or FileExistsError as e:
            print("A log does not exist at: " + path)
            return

        reader = csv.reader(file)
        i = 0
        habit_data_deleted = False

        for line in reader:
            if i == 1:
                self.name = line[0]
                self.health = int(line[1])
                self.xp = int(line[2])
                self.total_success = int(line[3])
                self.total_failure = int(line[4])
                self.total_consistency = float(line[5])

            elif i > 3:
                if not habit_data_deleted:
                    self.delete_all_habit_data()
                    habit_data_deleted = True
                habit = line[0]
                successes = int(line[1])
                failures = int(line[2])
                consistency = float(line[3])
                self.habits.append(habit)
                self.successes.append(successes)
                self.failures.append(failures)
                self.consistency.append(consistency)

            i += 1
        file.close()

    def export_data(self, filename):
        data = self.get_basic_stats()
        header = data[0]
        header_data = data[1]
        details = self.get_details()

        with open(filename, 'w+') as file:
            file.write(header)
            file.write('\n')
            file.write(header_data)
            file.write('\n\n')

            for line in details:
                file.write(line)
                file.write('\n')
            if len(details) > 1:                       # if there's more than just the header line
                print("Habits logged!")
            else:
                print("No habits to log :(")

        file.close()
        return data

    def log_habits(self):
        for habit in self.habits:
            answered = False
            while not answered:
                habit_status = input("Did you do " + habit + " today?  [Y] or [N]   ")
                if habit_status == 'Y' or habit_status == 'y':
                    self.check_habit(habit, True)
                    answered = True
                elif habit_status == 'N' or habit_status == 'n':
                    self.check_habit(habit, False)
                    answered = True
                else:
                    print("Be sure to type either [Y] or [N] as your answer.")

