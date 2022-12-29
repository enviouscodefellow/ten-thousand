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
        # dice_total = Counter(dice)
        # dice_items = dice_total.items()
        dice_scoring = tuple(
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

        dice_scoring_dict = dict((key, value) for key, value in dice_scoring)
        # dice_scoring_counter_list = []
        # for key in dice_scoring_dict:
        #     dice_scoring_counter_list.append(Counter(key))

        # for each in dice_scoring_dict:
        #     for each in each:
        #         print(type(each),each)

        # print(dice)
        score_dice = dice_scoring_dict.get(dice)
        return int(score_dice)

        # for key in dice_scoring_dict.keys():
        #     if key == dice:
        #         print(key)
        #         score_dice += dice_scoring_dict[key]
        #     return score_dice


# print(GameLogic.roll_dice(6))
# print(GameLogic.calculate_score(GameLogic.roll_dice(6)))
