# Score categories
# Change the values as you see fit
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: dice.count(1)
TWOS = lambda dice: dice.count(2)*2
THREES = lambda dice: dice.count(3)*3
FOURS = lambda dice: dice.count(4)*4
FIVES = lambda dice: dice.count(5)*5
SIXES = lambda dice: dice.count(6)*6
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and dice.count(list(set(dice))[0])*dice.count(list(set(dice))[1]) == 6 else 0
FOUR_OF_A_KIND = lambda dice: sum([i for i in dice if dice.count(i) >= 4][:4])
LITTLE_STRAIGHT = lambda dice: 30 if set(dice) == set([1,2,3,4,5]) else 0
BIG_STRAIGHT = lambda dice: 30 if set(dice) == set([2,3,4,5,6]) else 0
CHOICE = lambda dice: sum(dice)


def score(dice, category):
    return category(dice)
