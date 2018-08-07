import csv


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
    def __init__(self, name, health=100, xp=0, habits=[], successes=[], failures=[], consistency=[]):
        self.name = name
        self.health = health
        self.xp = xp
        self.habits = habits
        if successes != [] and failures != [] and consistency != []:
            self.successes = successes
            self.failures = failures
            self.consistency = consistency
        else:
            self.successes = [0] * len(habits)
            self.failures = [0] * len(habits)
            self.consistency = [0] * len(habits)
        self.alive = True

    # frequency is number of times per week habit should be done
    def add_habit(self, habit_name=""):
        while habit_name == "":
            habit_name = input("New habit description: ")
        self.habits.append(habit_name)
        self.successes.append(0)
        self.failures.append(0)
        print("Added habit!")

    def check_habit(self, habit, status):
        index = get_index(self, habit)
        if index == -1:
            print("ERROR: Habit not found!")
            return

        health_bonus = 5
        health_penalty = 10
        xp_bonus = 5
        xp_penalty = 10
        if status:
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

    def export_basic_stats(self, filename):
        header = "Name,Health,XP,Total Success,Total Failure,Overall Consistency"
        data = ""
        data += self.name + ","
        data += str(self.health) + ","
        data += str(self.xp) + ","

        total_success = 0
        total_failure = 0
        for success in self.successes:
            total_success += success
        for failure in self.failures:
            total_failure += failure

        data += str(total_success) + ","
        data += str(total_failure) + ","

        if total_success + total_failure == 0:
            consistency = 0
        else:
            consistency = total_success / (total_success + total_failure)
        data += str(consistency)

        with open(filename, 'w+') as file:
            file.write(header)
            file.write('\n')
            for line in data:
                file.write(line)
                file.write('\n\n')
        file.close()

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

        if total_success + total_failure == 0:
            success_ratio = 0
        else:
            success_ratio = total_success / (total_success + total_failure)
        print("CONSISTENCY: " + str(success_ratio) + "%\n")

    def export_details(self, log_exists=False):
        num_habits = len(self.habits)

        # adds a header row if log doesn't already exists
        if not log_exists:
            header = "Habit,Successes,Failures,Consistency"
            data = [None] * (num_habits + 1)
            data[0] = header
        else:
            data = [None] * num_habits

        # iterate through all habits
        for habit in self.habits:
            i = get_index(self, habit)
            row = ""
            row += str(habit)
            row += ","
            num_successes = self.successes[i]
            row += str(num_successes)
            row += ","
            num_failures = self.failures[i]
            row += str(num_failures)
            if num_successes + num_failures == 0:
                success_ratio = 0
            else:
                success_ratio = num_successes / (num_successes + num_failures)
            row += str(success_ratio)
            data[i] = row

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

    def read_log(self, path):
        try:
            file = open(path, "r")
        except FileNotFoundError or FileExistsError as e:
            print("ERROR READING LOG: A log does not exist at: " + path)
            return

        reader = csv.reader(file)
        i = 0
        for line in reader:
            if i != 0 and i != 1 and i != 2 and i != 3:
                habit = line[0]
                successes = line[1]
                failures = line[2]
                consistency = line[3]
                self.habits.append(habit)
                self.successes.append(successes)
                self.failures.append(failures)
                self.consistency.append(consistency)
            i += 1
        file.close()