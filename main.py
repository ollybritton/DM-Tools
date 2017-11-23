from color import *
import os

def nested_quicksort(xs):
    if len(xs) <= 1:
        return xs

    pivot = xs[0][1]
    lt, gt, eq = [], [], []

    for item in xs:
        if item[1] < pivot:
            lt.append(item)

        elif item[1] > pivot:
            gt.append(item)

        else:
            eq.append(item)

    return nested_quicksort(lt) + eq + nested_quicksort(gt)


def initiave_tracker():
    # Initiave Tracker
    display("<yellow>Please enter the player's name, followed by initiave. For example, \"john 15\". The players name can be only one word long.</yellow>")
    players = []

    while True:
        current = xinput("<cyan>Type the player's name or \"exit\" >>></cyan>", ["cyan", "black", "bright"])

        if current == "exit" or current == "":
            break

        else:
            players.append([current.split(" ")[0], int(current.split(" ")[1])])

    players = nested_quicksort(players)[::-1]
    os.system("clear")

    xinput("<cyan>Press enter when you are ready to start combat.</cyan>", ["cyan", "black", "bright"])
    counter = 0

    while True:
        os.system("clear")
        display("<yellow>" + players[counter][0] + "</yellow><red>, initiave: " + str(players[counter][1]) + "</red><pink>, up next: " + players[(counter + 1) % (len(players))][0] + ".</pink>")
        display("<green>Commands: exit, remove, skip, or next.</green>")

        choice = xinput("<cyan>>>></cyan>", ["cyan", "black", "bright"])
        if choice == "exit":
            break

        elif choice == "remove":
            del players[counter]

        elif choice == "skip" or choice == "next" or choice == "":
            counter = (counter + 1) % (len(players))



def encounter_calculator():
    # Initiave Tracker
    choice = xinput("<cyan>Do you want to use the [a]verage level or enter the levels for all the [p]layers? >>></cyan>", ["cyan", "bright", "black"])
    scores = []

    if choice == "a" or choice == "":
        player_num = int(xinput("<cyan>How many players are there? >>></cyan>", ["cyan", "bright", "black"]))
        average = int(xinput("<cyan>What is the average level? >>></cyan>", ["cyan", "bright", "black"]))

        for i in range(player_num):
            scores.append(average)

    elif choice == "p":
        player_num = int(xinput("<cyan>How many players are there? >>></cyan>", ["cyan", "bright", "black"]))

        for i in range(player_num):
            scores.append(int(xinput("<cyan>What is player " + str(i + 1) + "'s level? >>></cyan>", ["cyan", "bright", "black"])))

    encounter_difficulty = xinput("<cyan>What difficulty do you want? [e]asy, [m]edium, [h]ard or [d]eadly? >>></cyan>", ["cyan", "bright", "black"])

    level = []

    easy = [25, 50, 75, 125, 250, 300, 350, 450, 550, 600, 800, 1000, 1100, 1250, 1400, 1600, 2000, 2100, 2400, 2800]
    medium = [50, 100, 150, 250, 500, 600, 750, 900, 1100, 1200, 1600, 2000, 2200, 2500, 2800, 3200, 3900, 4200, 4900, 5700]
    hard = [75, 150, 225, 375, 750, 900, 1100, 1400, 1600, 1900, 2400, 3000, 3400, 3800, 4300, 4800, 5900, 6300, 7300, 8500]
    deadly = [100, 200, 400, 500, 1100, 1400, 1700, 2100, 2400, 2800, 3600, 4500, 5100, 5700, 6400, 7200, 8800, 9500, 10900, 12700]


    if encounter_difficulty == "e":
        level = easy

    elif encounter_difficulty == "m":
        level = medium

    elif encounter_difficulty == "h":
        level = hard

    elif encounter_difficulty == "d":
        level = deadly

    xp_threshold = 0

    for score in scores:
        xp_threshold += level[score - 1]

    display("<red>Your XP threshold is " + str(xp_threshold) + ".</red>")

    challenge_ids = ["0", "1/8", "1/4", "1/2", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "30"]
    challenge_xp = [10, 25, 50, 100, 200, 450, 700, 1100, 1800, 2300, 2900, 3900, 5000, 5900, 7200, 8400, 10000, 11500, 13000, 15000, 18000, 20000, 22000, 25000, 33000, 41000, 50000, 62000, 115000]

    for i in range(len(challenge_xp)):
        monster_challenge = challenge_ids[i]
        monster_xp = challenge_xp[i]

        if monster_xp > xp_threshold:
            break

        else:
            display("<green>Challenge " + monster_challenge + " - " + str(monster_xp) + "xp.</green>")
            for i in range(6):
                if i == 0:
                    display("<blue> - 1 monster</blue><yellow>, " + str(monster_xp * 1) + "xp.</yellow>")

                elif i == 1:
                    if monster_xp*1.5 > xp_threshold:
                        break

                    display("<blue> - 2 monsters</blue><yellow>, " + str(monster_xp * 1.5) + "xp.</yellow>")

                elif i == 2:
                    if monster_xp*2 > xp_threshold:
                        break

                    display("<blue> - 3-6 monsters</blue><yellow>, " + str(monster_xp * 2) + "xp.</yellow>")

                elif i == 3:
                    if monster_xp*2.5 > xp_threshold:
                        break

                    display("<blue> - 7-10 monsters</blue><yellow>, " + str(monster_xp * 2.5) + "xp.</yellow>")

                elif i == 4:
                    if monster_xp*3 > xp_threshold:
                        break

                    display("<blue> - 11-14 monsters</blue><yellow>, " + str(monster_xp * 3) + "xp.</yellow>")

                elif i == 5:
                    if monster_xp*4 > xp_threshold:
                        break

                    display("<blue> - 15+ monsters</blue><yellow>, " + str(monster_xp * 4) + "xp.</yellow>")

            print("")

    input()

def random_stuff():
    # Initiave Tracker
    return



def main():
    while True:
        os.system("clear")
        display("<red>DM Tools - Please select from the options below.</red>")

        # 1. Initiave Tracker
        # 2. Encounter Calculator
        # 3. Random Name Generator
        choices = ["Initiave Tracker", "Encounter Calculator", "Random Stuff"]

        display("<green>1. Initiave Tracker</green>")
        display("<green>2. Encounter Calculator</green>")
        display("<green>3. Random Stuff</green>")

        choice = int(xinput("<cyan>>>> </cyan>", ["cyan", "black", "bright"])) - 1

        if choices[choice] == "Initiave Tracker":
            initiave_tracker()

        elif choices[choice] == "Encounter Calculator":
            encounter_calculator()

        elif choices[choice] == "Random Stuff":
            random_stuff()

        else:
            os.system("clear")
            display("<red>Sorry, that's not an option.")

main()
