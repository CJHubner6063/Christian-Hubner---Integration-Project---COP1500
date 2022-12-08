# Christian Hubner

# The program is designed as a choose your own story kind of adventure, with the user input dictating certain responses in a narrative.

# This function will collect points and return an updated sum

def up_points(number, exsisting_points):
    points_total = int(exsisting_points) + int(number)
    exsisting_points = points_total
    return exsisting_points
    return points_total


def main():
    # A try function is used effectively on the whole body of code to provide a general error message in the event that any errors were missed
    try:
        exsisting_points = 0
        # The error checker is used with while and try, except functions to loop users who enter incorrect input and provide an error message
        error_checker = 1

        print("Welcome to my program.", end="\n")

        # This part of the program requests the number of users and their names and stores their names in a variable for later use
        player_names = ""

        while (error_checker == 1):
            try:
                multiple_player_checker = int(input(
                    "How adventurers dare brave this journey today?(Enter a number)"))
                # This part of the code prevents users from entering a specific invalid input and terminates the code along a narrative
                if (multiple_player_checker == 0):
                    print("Since there are no players the game is over")
                    quit()
                error_checker = 0
            except:
                print(
                    "Please enter a whole number value greater than 0 such as '1','2','5', or '24'")

        error_checker = 1

        number_of_players = multiple_player_checker
        if (multiple_player_checker > 1 and not multiple_player_checker > 99):
            while (int(multiple_player_checker) != 0):
                player_names_input = input(
                    "Welcome" + player_names + " enter the name of one adventurer.")
                player_names = str(player_names) + ", " + str(
                    player_names_input)
                multiple_player_checker = int(multiple_player_checker) - 1
        elif (multiple_player_checker > 99):
            # Thus part of the code prevents users from ultilizing far too many loops and terminates the code following the narrative
            print("We will not speak to so many adventurers, begone!")
            quit()
        else:
            player_names_input = input("What is your name daring adventurer?")
            player_names = player_names_input

        print("Well then" + player_names + " I hope you're ready." + "\n",
              sep="")

        # This part of the code interacts with the number of players and the predefined function

        turn_counter = number_of_players
        for players in range(number_of_players):
            player_turn = int(number_of_players - turn_counter) + 1
            print("Perhaps something to get you started Player" + str(
                player_turn) + "?")
            turn_counter = turn_counter - 1
            error_checker = 1
            while (error_checker == 1):
                try:
                    beginning_gamble_choice = int(input(
                        "Pick a number and unless fate frowns upon you I'll give you something."))
                    if (int(beginning_gamble_choice) == 1 or int(
                            beginning_gamble_choice) == 3):
                        print(
                            "I'm afraid luck does indeed frown upon you today Adventurer, I have nothing for you." + "\n")
                        error_checker = 0
                    else:
                        print(
                            "Congratulations adventurer, enjoy your feeling of success." + "\n")
                        up_points(5, exsisting_points)
                        error_checker = 0
                except:
                    print(
                        "Please enter a whole number value such as '1','2','5', or '24'")

        error_checker = 1

        # This part of the code is a bunch of similarly set up levels that use required pieces of code and set them in the narrative of the project

        while (error_checker == 1):
            print("You enter a room with a riddle on its wall.")
            try:
                power_answer = 2 ** 4
                user_power_answer = input(
                    "What do you think 2 to the power of 4 is?")
                print("Your answer was", user_power_answer)
                if (int(user_power_answer) == int(power_answer)):
                    print("You were correct!" + "\n")
                    error_checker = 0
                else:
                    print("You were wrong." + "\n")
                    error_checker = 0
            except:
                print(
                    "Please enter a number value such as '1','2','5.3', or '24.7'")
        print("2 to the power of 4 is", power_answer)
        print("You exit the room and enter another." + "\n")

        error_checker = 1

        while (error_checker == 1):
            print("The room you enter has another riddle upon its wall")
            try:
                multiplication_answer = 2 * 4
                user_multiplication_answer = input(
                    "What do you think 2 times 4 is?")
                print("Your answer was", user_multiplication_answer)
                if (int(user_multiplication_answer) == int(
                        multiplication_answer)):
                    print("You were correct!" + "\n")
                    error_checker = 0
                else:
                    print("You were wrong." + "\n")
                    error_checker = 0
            except:
                print(
                    "Please enter a number value such as '1','2','5.3', or '24.7'")
        print("2 times 4 is", multiplication_answer)
        print("You exit the room and enter another." + "\n")

        error_checker = 1

        while (error_checker == 1):
            print("The room you enter has another riddle upon its wall")
            try:
                division_answer = 4 / 2
                user_division_answer = input(
                    "What do you think 4 divided by 2 is?")
                print("Your answer was", user_division_answer)
                if (int(user_division_answer) == int(division_answer)):
                    print("You were correct!" + "\n")
                    error_checker = 0
                else:
                    print("You were wrong." + "\n")
                    error_checker = 0
            except:
                print(
                    "Please enter a number value such as '1','2','5.3', or '24.7'")
        print("4 divided by 2 is", int(division_answer))
        print("You exit the room and enter another." + "\n")

        error_checker = 1

        while (error_checker == 1):
            print("The room you enter has another riddle upon its wall")
            try:
                modulus_answer = 7 % 3
                user_modulus_answer = input(
                    "What do you think the remainder of 7 divided by 3 is?")
                print("Your answer was", user_modulus_answer)
                if (int(user_modulus_answer) == int(modulus_answer)):
                    print("You were correct!" + "\n")
                    error_checker = 0
                else:
                    print("You were wrong." + "\n")
                    error_checker = 0
            except:
                print(
                    "Please enter a number value such as '1','2','5.3', or '24.7'")
        print("The remainder of 7 divided by 3 is", modulus_answer)
        print("You exit the room and enter another." + "\n")

        error_checker = 1

        while (error_checker == 1):
            print("The room you enter has another riddle upon its wall")
            try:
                floor_division_answer = 7 // 3
                user_floor_division_answer = input(
                    "What do you think the whole value without remainders of 7 divided by 3 is?")
                print("Your answer was", user_floor_division_answer)
                print(
                    "The whole value without remainders of 7 divided by 3 is",
                    floor_division_answer)
                if (int(user_floor_division_answer) == int(
                        floor_division_answer)):
                    print("You were correct!" + "\n")
                    error_checker = 0
                else:
                    print("You were wrong." + "\n")
                    error_checker = 0
            except:
                print(
                    "Please enter a number value such as '1','2','5.3', or '24.7'")
            print("The whole value without remainders of 7 divided by 3 is",
                  floor_division_answer)
            print("You exit the room and enter another." + "\n")

        error_checker = 1

        while (error_checker == 1):
            print("The room you enter has another riddle upon its wall")
            try:
                addition_answer = 2 + 4
                user_addition_answer = input("What do you think 2 plus 4 is?")
                print("Your answer was", user_addition_answer)
                if (int(user_addition_answer) == int(addition_answer)):
                    print("You were correct!" + "\n")
                    error_checker = 0
                else:
                    print("You were wrong." + "\n")
                    error_checker = 0
            except:
                print(
                    "Please enter a number value such as '1','2','5.3', or '24.7'")
        print("2 plus 4 is", addition_answer)
        print("You exit the room and enter another." + "\n")

        error_checker = 1

        while (error_checker == 1):
            print("The room you enter has another riddle upon its wall")
            try:
                subtraction_answer = 4 - 2
                user_subtraction_answer = input(
                    "What do you think 4 minus 2 is?")
                print("Your answer was", user_subtraction_answer)
                if (int(user_subtraction_answer) == int(subtraction_answer)):
                    print("You were correct!" + "\n")
                    error_checker = 0
                else:
                    print("You were wrong." + "\n")
                    error_checker = 0
            except:
                print(
                    "Please enter a number value such as '1','2','5.3', or '24.7'")
        print("4 minus 2 is", subtraction_answer)
        print("You exit the room and enter another." + "\n")
    except:
        print("I'm sorry an unforseen error occured.")

    print(
        "Congratulations on completing the practice dungeon! Now go find some real ones with monsters even scarier than math!")


main()
