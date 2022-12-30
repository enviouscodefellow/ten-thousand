from random import randint
from collections import Counter

class GameLogic:
    def roll_dice(dice):
        roll = []
        for die in range(0, dice):
            roll.append(randint(1, 6))
            # print(roll)
        return tuple(sorted(roll))


    def calculate_score(dice):
        score_dice = 0
        dice_counter = Counter(dice)
        # dice_items = dice_total.items()
        dice_scoring_tupl = tuple(
            [
                (tuple(), 0),
                ((1,), 100),
                ((1, 1), 200),
                ((1, 1, 1), 1000),
                ((1, 1, 1, 1), 2000),
                ((1, 1, 1, 1, 1), 3000),
                ((1, 1, 1, 1, 1, 1), 4000),
                ((2,), 0),
                ((2, 2), 0),
                ((2, 2, 2), 200),
                ((2, 2, 2, 2), 400),
                ((2, 2, 2, 2, 2), 600),
                ((2, 2, 2, 2, 2, 2), 800),
                ((3,), 0),
                ((3, 3), 0),
                ((3, 3, 3), 300),
                ((3, 3, 3, 3), 600),
                ((3, 3, 3, 3, 3), 900),
                ((3, 3, 3, 3, 3, 3), 1200),
                ((4,), 0),
                ((4, 4), 0),
                ((4, 4, 4), 400),
                ((4, 4, 4, 4), 800),
                ((4, 4, 4, 4, 4), 1200),
                ((4, 4, 4, 4, 4, 4), 1600),
                ((5,), 50),
                ((5, 5), 100),
                ((5, 5, 5), 500),
                ((5, 5, 5, 5), 1000),
                ((5, 5, 5, 5, 5), 1500),
                ((5, 5, 5, 5, 5, 5), 2000),
                ((6,), 0),
                ((6, 6), 0),
                ((6, 6, 6), 600),
                ((6, 6, 6, 6), 1200),
                ((6, 6, 6, 6, 6), 1800),
                ((6, 6, 6, 6, 6, 6), 2400),
                ((1, 2, 3, 4, 5, 6), 1500),
                ((2, 2, 3, 3, 4, 6), 0),
                ((2, 2, 3, 3, 6, 6), 1500),
                ((1, 1, 1, 2, 2, 2), 1200),
            ],
        )
        dice_scoring_list = list(dice_scoring_tupl)

        dice_scoring_dict = dict((key, value) for key, value in dice_scoring_tupl)
        dice_scoring_counter_list = []
        for key in dice_scoring_dict:
            dice_scoring_counter_list.append(Counter(key))
        # print(dice_scoring_counter_list)
        dice_scoring_dict_values = dice_scoring_dict.values()
        # print(list(dice_scoring_dict_values))
        counter_scoring_tupl = tuple(zip(dice_scoring_counter_list, dice_scoring_dict_values))
        print(counter_scoring_tupl)
        # counter_scoring_dict = dict((key, value) for key, value in counter_scoring_tupl)

        print(dice)
        score_dice = dice_scoring_dict.get(dice)
        return score_dice

        # if not dice:
        #     return 0
        # elif dice:
        #     score_dice = counter_scoring_dict.get(dice_counter)


# print(GameLogic.roll_dice(6))
print(GameLogic.calculate_score(GameLogic.roll_dice(6)))

