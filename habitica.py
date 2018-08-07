import os.path
import sys
from habitica_player import Player


def execute_decision(decision):
    log = 1
    add = 2
    stats = 3
    leave = 4
    if decision == log:
        player.log_habits()
    elif decision == add:
        player.add_habit()
    elif decision == stats:
        player.print_basic_stats()
    elif decision == leave:
        sys.exit(0)
    else:
        print("Incorrect usage!")
        decision = input("Please press [1] to log habits, [2] to add a habit, [3] to see your stats, or [4] to quit:  ")


# create new player with 0 XP and no habits
player = Player("Patrick")
filename = "habit_log.csv"
path = "C:/User/Documents/WS_IntroPython/" + filename
log_exists = os.path.isfile(filename)

if log_exists:
    # initialize player's stats by reading from existing habit log
    player.read_log(path)

looping = True
while looping:
    print("Hi there", player.name)
    decision = input("Please press [1] to log habits, [2] to add a habit, [3] to see your stats, or [4] to quit:  ")
    decision = int(decision)
    execute_decision(decision)
    # prints player's important stats at top
    player.export_basic_stats(filename)

    # data is a List of strings to be written to file
    data = player.export_details(log_exists)

    # w+ means that we will write to the csv file
    # and create one if 'habit_log.csv' doesn't already exist
    with open(filename,'w+') as file:
        for line in data:
            file.write(line)
            file.write('\n')
        if data != []:
            print("Habits logged at: " + path)
        else:
            print("No habits to log :(")
    file.close()

    print("Nice :)")
    print("Would you like to do something else or leave?")
    decision = input("Please press [1] to leave or any button to stay:  ")
    leave = 1
    if decision == leave:
        looping = False

