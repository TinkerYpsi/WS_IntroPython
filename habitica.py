import os.path
import sys
from habitica_player import Player


filename = "habit_log.csv"
path = os.getcwd() + "/" + filename


def run_user_option():
    decision = input("Please press [1] to log habits, [2] to add a habit, [3] to see your stats, or [4] to quit:  ")
    decision = int(decision)
    log = 1
    add = 2
    stats = 3
    leave = 4
    if decision == log:
        player.log_habits()
        player.export_data(filename)
    elif decision == add:
        player.add_habit()
    elif decision == stats:
        player.print_basic_stats()
    elif decision == leave:
        sys.exit(0)
    else:
        print("Incorrect usage!")


# create new player with 0 XP and no habits
player = Player("Patrick")

log_exists = os.path.isfile(filename)
if log_exists:
    # initialize player's stats by reading from existing habit log
    player.read_log(path)

looping = True
while looping:
    print("Hi there", player.name)
    run_user_option()
    print("Would you like to do something else or leave?")
    choice = input("Please press [X] to leave or any button to stay:  ")
    if choice == 'X' or choice == 'x':
        looping = False
    else:
        print("\n")

