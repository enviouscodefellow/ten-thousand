from textwrap import dedent
from game_logic import GameLogic

#global variables
round = 0
dice_reroll= 6
unbanked_points = 0
total_points = 0


def welcome():
    print(dedent("""
    Welcome to Ten Thousand
    (y)es to play or (n)o to decline
    """))
    game_start = input('> ')
    game_start = game_start.lower()

    if game_start == 'y':
        new_game_setup()
    elif game_start == 'n':
        print(dedent("OK. Maybe another time"))
    else:
        welcome()


def new_game_setup():
    global round
    round = 0
    global dice_reroll
    dice_reroll= 6
    global unbanked_points
    unbanked_points = 0
    global total_points
    total_points = 0
    round_start()


def round_start(dice=6):
    global round
    global dice_reroll
    roll = GameLogic.roll_dice(dice)
    global unbanked_points
    global total_points
    if dice == 6:
        round += 1
        dice_reroll = 6
        print(dedent(f"""
            Starting round {round}
            """))
    print(dedent(f"""
            Rolling {dice} dice...
            """))
    print(dedent(f"""
    *** {roll} ***
    Enter dice to keep, or (q)uit:
          """))
    roll_save = roll
    dice_to_keep = []
    dice_to_keep = input("> ")
    dice_to_keep = dice_to_keep.lower()


    if dice_to_keep == 'q':
        print(dedent(f"Thanks for playing. You earned {total_points} points"))

    elif dice_to_keep.isdigit() != True:
        print("Please enter only integers (1-6) that match each die you would like to save. No spaces")
        round_start()

    else:
        # print(type(dice_to_keep))
        dice_to_keep_tupl = tuple(dice_to_keep)
        # print(type(dice_to_keep_tupl))
        # print(dice_to_keep_tupl)
        # for each in dice_to_keep_tupl:
        #     print(type(each))
        # dice_to_keep_tupl = [int(i) for a, i in enumerate(dice_to_keep)]
        dice_to_keep_tupl = [int(value) for value in dice_to_keep]
        dice_to_keep_tupl = tuple(dice_to_keep_tupl)
        # print(type(dice_to_keep_tupl))
        # print(dice_to_keep_tupl)
        # for each in dice_to_keep_tupl:
        #     print(type(each))
        # print(dice_to_keep_tupl)
        # print(GameLogic.calculate_score(dice_to_keep_tupl))
        unbanked_points += GameLogic.calculate_score(tuple(dice_to_keep_tupl))
        dice_reroll = dice_reroll - len(dice_to_keep_tupl)
        print(dedent(f"""
        You have {unbanked_points} unbanked points and {dice_reroll} dice remaining
        (r)oll again, (b)ank your points or (q)uit:
        """))
        if dice_reroll > 0:
            roll_again = input("> ")

            if roll_again == "r":
                round_start(dice_reroll)

            elif roll_again == "b":
                total_points += unbanked_points
                print(dedent(f"""
                You banked {unbanked_points} points in round {round}
                Total score is {total_points} points
                """))
                unbanked_points = 0
                round_start()

            elif roll_again == "q":
                print(f"Thanks for playing. You earned {total_points} points")
        else:
            total_points += unbanked_points
            print(dedent(f"""
                You banked {unbanked_points} points in round {round}
                Total score is {total_points} points
                """))
            unbanked_points = 0
            round_start()


welcome()