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

        if total_success + total_failure == 0:
            success_ratio = 0
        else:
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
