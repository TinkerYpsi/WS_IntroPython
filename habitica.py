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
    def add_habit(self, habit):
        self.habits.append(habit)
        self.successes.append(0)
        self.failures.append(0)

    def check_habit(self, habit, status):
        health_bonus = 5
        health_penalty = 10
        xp_bonus = 5
        xp_penalty = 10
        if status == True:
            self.successes[get_index(self, habit)] += 1
            self.xp += xp_bonus
            if self.health + health_bonus >= 100:
                self.health = 100
                # extra XP bonus is awarded if player maintains 100 health
                self.xp += xp_bonus
            else:
                self.health += health_bonus
        else:
            self.failures[get_index(self, habit)] += 1
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
player = Player("player")
player.add_habit("Bike 10 miles")

print("Hi there", player.name)

for habit in player.habits:
    answered = False
    while not answered:
        habit_status = input("Did you do " + habit + " today?  [Y] or [N]   ")
        if habit_status == 'Y' or habit_status == 'y':
            player.check_habit(habit, True)
            answered = True
        if habit_status == 'N' or habit_status == 'n':
            player.check_habit(habit, False)
            answered = True
        else:
            print("Be sure to type either [Y] or [N] as your answer.")

player.print_basic_stats()
