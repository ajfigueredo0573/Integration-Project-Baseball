# Alejandro Figueredo
# An integration of everything I have learned about programming!
def greeting_the_user():
    name = input("Who do I have the pleasure to work with?\n")
    print(("Hello!" * 2), name)


def introducing_user_to_project():
    print("Welcome to my Integration Project!")
    print(" This project should help baseball players to:\n "
          "Calculate their stats after a certain amount of games")
    greeting_the_user()


introducing_user_to_project()

# Getting information on the player
print("Now let's start with some basic information on the player we are "
      "going to evaluate")
player_name = input("Player's full name\n")
player_team = input("Player's team\n")
player_position = input("Player's position\n")

# Getting information on how the player did on the game
# Times on base == hits + walks(BB) + hit by pitches(HBP)
# Getting on base by an error counts as a missed at bat
# Legal AB's count just outs and hits
amount_of_games = int(input("How many games did the player participated in? "))


def calculate_player_stats_for_game(ab_per_game, on_base_per_game):
    if on_base_per_game > 0:
        number_of_hits = int(input("How many total hits on the day?\n"))
        if on_base_per_game > number_of_hits:
            sac_fly = int(input("Any sac fly or bunts?\n"))
            walks_bb = int(input("How many times did you walked?\n"))
        else:
            walks_bb = 0
            sac_fly = 0
    else:
        number_of_hits = 0
        walks_bb = 0
        sac_fly = 0

    number_of_hit_bp = on_base_per_game - (number_of_hits + walks_bb)
    legal_ab = ab_per_game - (walks_bb + number_of_hit_bp + sac_fly)

    base_hits = int(input("Of the " + str(
        number_of_hits) + " hits that " + player_name + " got on last night's "
                                                        "game, how many were "
                                                        "base hits?\n"))
    if base_hits != number_of_hits:
        doubles = int(input("How many were doubles?\n"))
        if (base_hits + doubles) != number_of_hits:
            triples = int(input("How many were triples?\n"))
            if (base_hits + doubles + triples) != number_of_hits:
                home_runs = int(input("How many were HR?\n"))
            else:
                home_runs = 0
        else:
            triples = 0
            home_runs = 0
    else:
        doubles = 0
        triples = 0
        home_runs = 0

    # Calculations Numeric operators: + (addition), - (subtraction), *
    # (multiplication), ** (power function),
    # / (division), // (floor division),
    # % (module division, which finds the remainder) String Operator: + (which
    # concatenates two strings without a space between them) AVG(average,
    # also known as BA)represents how many times the
    # player collected a hit per 10 at bats. OBP(on-base percentage, also
    # known as OBA)represents how many times the
    # hitter got on base every 10 at bats. This stat counts hits, walks,
    # and hit by pitches. Slugging % expresses total
    # bases (including all extra base hits) divided by at bats.
    # Slugging % = (base_hits + (2 *doubles) + (3 * triples) +
    # (4 * home_runs))/(ab_per_game)
    doubles *= 2
    triples *= 3
    home_runs *= 4
    player_avg = number_of_hits / legal_ab
    player_obp = on_base_per_game / ab_per_game
    player_slugging = \
        (base_hits + doubles + triples + home_runs) / ab_per_game
    avg_meaning = ((player_avg * (10 ** 3)) // ((10 % 9) * 100))

    # Results
    print("The " + player_position,
          player_name + " from " + player_team + " is hitting " +
          format(player_avg, '.3f') + "/" + format(player_obp, '.3f') + "/" +
          format(player_slugging, '.3f'))

    print(" ")
    print(
        "In other words, this hitter is getting on base " +
        format(avg_meaning, '.0f') + " times\nevery 10 at bats.")


game_number = 1

for games in range(amount_of_games):
    print("You are entering stats for game number", game_number)
    number_of_ab = int(input("How many AB's?\n"))
    times_on_base = int(input("How many times did the player get on base?\n"))
    calculate_player_stats_for_game(number_of_ab, times_on_base)
    game_number += 1
print(" ")
decision = input('Do you wish to look at more options?\n')
while (decision != 'yes') and (decision != 'no'):
    decision = input('Invalid Input. Try again.\n'
                     'Do you wish to look at more options?\n')

continue_to_next_option = True
if decision == "no":
    continue_to_next_option = False
    print("Okay! See you next time!")
else:
    print("Okay! Select one of these options:")
    print("a) Add one more game")
    print("b) Add n amount of games")
    print("c) Exit the program")
    choice_from_user = input("Please, insert your option")
    while choice_from_user != "a" and choice_from_user != "b" and \
            choice_from_user != "c":
        choice_from_user = input("Invalid input! Please, try again")
    if ('a' == choice_from_user) or (choice_from_user == 'b') or (
            choice_from_user == "c"):
        if choice_from_user == "a":
            print("Let's work on it")
        elif choice_from_user == "b":
            print("Okay")
            amount_of_games_added = int(input("How many more games are you "
                                              "adding?"))
        else:
            print("Exiting...")


# Citation: MacLennan, Ashley. "A complete beginner's guide to baseball stats:
# Batting statistics, and what they
# mean". https://www.blessyouboys.com/2019/1/8/18171919/baseball-stats-
# for-beginners-batting-average-on-base
# -percentage-explained#:~:text=The%20next%20part%20of%20understanding
# ,%2C%20and%20slugging%20(
# SLG).&text=A%20fourth%20batting%20stat%20of,base%20percentage%20and%
# 20slugging%20percentage.
