# Christian Hubner

# The program is designed as a choose your own story kind of adventure, with the user input dictating certain responses in a narrative.

def up_points(number, exsisting_points):
    points_total = int(exsisting_points) + int(number)
    exsisting_points = points_total
    return exsisting_points


def main():
    exsisting_points = 0
    points_total = 0

    print("Welcome to my program.", end="\n")

    # This part of the program requests the number of users and their names and stores their names in a variable for later use
    player_names = ""
    multiple_player_checker = int(input(
        "How adventurers dare brave this journey today?(Enter a number)"))
    number_of_players = multiple_player_checker
    if (multiple_player_checker > 1 and not multiple_player_checker > 5):
        while (int(multiple_player_checker) != 0):
            player_names_input = input(
                "Welcome" + player_names + " enter the name of one adventurer.")
            player_names = str(player_names) + ", " + str(player_names_input)
            multiple_player_checker = int(multiple_player_checker) - 1
    else:
        player_names_input = input("What is your name daring adventurer?")
        player_names = player_names_input

    print("Well then" + player_names + " I hope you're ready." + "\n", sep="")

    turn_counter = number_of_players
    for players in range(number_of_players):
        player_turn = int(number_of_players - turn_counter) + 1
        print("Perhaps something to get you started Player" + str(
            player_turn) + "?")
        beginning_gamble_choice = input(
            "Pick a number and unless fate frowns upon you I'll give you something.")
        if (int(beginning_gamble_choice) == 1 or int(
                beginning_gamble_choice) == 3):
            print(
                "I'm afraid luck does indeed frown upon you today Adventurer, I have nothing for you.")
        else:
            print(
                "Congratulations adventurer here are five points to start your group off.")
            up_points(5, exsisting_points)

    # This part of the code will hold various operators with no true purpose until they can be integrated into riddles further in the development of the proects storyline.
    # For now the user is asked to anser an equation and then they are told the actual answer and if they were right or not.

    power_answer = 2 ** 4
    user_power_answer = input("What do you think 2 to the power of 4 is?")
    print("Your answer was", user_power_answer)
    print("2 to the power of 4 is", power_answer)
    if (int(user_power_answer) == int(power_answer)):
        print("You were correct!" + "\n")
    else:
        print("You were wrong." + "\n")

    multiplication_answer = 2 * 4
    user_multiplication_answer = input("What do you think 2 times 4 is?")
    print("Your answer was", user_multiplication_answer)
    print("2 times 4 is", multiplication_answer)
    if (int(user_multiplication_answer) == int(multiplication_answer)):
        print("You were correct!" + "\n")
    else:
        print("You were wrong." + "\n")

    division_answer = 4 / 2
    user_division_answer = input("What do you think 4 divided by 2 is?")
    print("Your answer was", user_division_answer)
    print("4 divided by 2 is", int(division_answer))
    if (int(user_division_answer) == int(division_answer)):
        print("You were correct!" + "\n")
    else:
        print("You were wrong." + "\n")

    modulus_answer = 7 % 3
    user_modulus_answer = input(
        "What do you think the remainder of 7 divided by 3 is?")
    print("Your answer was", user_modulus_answer)
    print("The remainder of 7 divided by 3 is", modulus_answer)
    if (int(user_modulus_answer) == int(modulus_answer)):
        print("You were correct!" + "\n")
    else:
        print("You were wrong." + "\n")

    floor_division_answer = 7 // 3
    user_floor_division_answer = input(
        "What do you think the whole value without remainders of 7 divided by 3 is?")
    print("Your answer was", user_floor_division_answer)
    print("The whole value without remainders of 7 divided by 3 is",
          floor_division_answer)
    if (int(user_floor_division_answer) == int(floor_division_answer)):
        print("You were correct!" + "\n")
    else:
        print("You were wrong." + "\n")

    addition_answer = 2 + 4
    user_addition_answer = input("What do you think 2 plus 4 is?")
    print("Your answer was", user_addition_answer)
    print("2 plus 4 is", addition_answer)
    if (int(user_addition_answer) == int(addition_answer)):
        print("You were correct!" + "\n")
    else:
        print("You were wrong." + "\n")

    try:
        subtraction_answer = 4 - 2
        user_subtraction_answer = input("What do you think 4 minus 2 is?")
        print("Your answer was", user_subtraction_answer)
        print("4 minus 2 is", subtraction_answer)
        if (int(user_subtraction_answer) == int(subtraction_answer)):
            print("You were correct!" + "\n")
        else:
            print("You were wrong." + "\n")
    except:
        print("I'm sorry an unforseen error has occured.")


main()
