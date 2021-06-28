import itertools
import random
import math


class Game:
    timeInSeconds = None
    upgradeValues = {"q": [1, 5, 50, 100, 500, 2000, 5000, 10000, 250000, 1000000],
                     "s": [2, 20, 100, 200, 1000, 4000, 10000, 50000, 1000000, 5000000],
                     "m": [1, 1.5, 2, 3, 5, 8, 12, 18, 30, 100]}
    upgradeCosts = {"q": [0, 10, 100, 1000, 10000, 75000, 300000, 1000000, 10000000, 100000000], "s": [0, 15, 150, 1500, 15000, 115000, 450000, 1500000, 15000000, 200000000],
                    "m": [0, 50, 300, 2000, 12000, 85000, 700000, 6500000, 65000000, 1000000000]
                    }

    def __init__(self, time):
        self.timeInSeconds = time * 60


class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.money = 0
        self.accuracy = 0.95
        self.timePerQuestion = 5
        self.levelPerCategory = {"q": 1, "s": 1, "m": 1}
        self.averageScore = []
        self.turnsUsed = []

    def run(self, game):
        turns = int(game.timeInSeconds / self.timePerQuestion)
        for j in range(1):
            self.money = 0
            self.levelPerCategory = {"q": 1, "s": 1, "m": 1}
            index = 0
            streak = False
            for i in range(turns):
                print(i + 1)
                if index == len(self.strategy):
                    self.turnsUsed.append(i)
                    index += 1
                    print("Finished strategy at:" + str(i))
                elif index < len(self.strategy):
                    goal = self.strategy[index]
                    goalInCost = game.upgradeCosts[goal][self.levelPerCategory[goal]]
                    if self.money >= goalInCost:
                        # Upgrade
                        self.levelPerCategory[goal] += 1
                        self.money -= goalInCost
                        index += 1
                        print("Upgrade for "+goal+" for cost of "+str(goalInCost))
                # Answer question
                # Answered question correctly
                if random.random() <= self.accuracy:
                    # Answered correctly
                    print("Answered Correctly!")
                    self.money += math.ceil((game.upgradeValues["q"][self.levelPerCategory["q"] - 1] + (
                        (1 if streak else 0) * game.upgradeValues["s"][self.levelPerCategory["s"] - 1]) * game.upgradeValues["m"][self.levelPerCategory["m"] - 1]))
                    streak = True
                else:
                    # Answered incorrectly
                    print("Answered Incorrectly!")
                    self.money -= math.ceil(game.upgradeValues["q"][self.levelPerCategory["q"] - 1]
                                            * game.upgradeValues["m"][self.levelPerCategory["m"] - 1])
                    streak = False
                print("Current Money: " + str(self.money) + "\n")
            self.averageScore.append(self.money)
            print("Money on round:" + str(self.money) + "\n\n\n")


def myMoneySort(player):
    return sum(player.averageScore) / len(player.averageScore)


player1 = Player(['q', 's', 'm', 'q', 's', 'm', 'q', 's', 'm', 'q', 's', 'm'])
player1.run(Game(10))
print("Player Stats:")
print("Money: " + str(int(myMoneySort(player1))) + str(player1.averageScore) +
      "---Turns Used: " + str(player1.turnsUsed) +
      "---Strategy: " + str(player1.strategy))


# def myTurnSort(player):
#     return sum(player.turnsUsed) / len(player.turnsUsed)


# playersList.sort(key=myTurnSort)
# for i in range(20):
#     print()
# for i in range(len(playersList)):
#     print(str(i + 1) + ". Money: " + str(playersList[i].money) +
#           "---Turns Used: " + str(playersList[i].turnsUsed) +
#           "---Strategy: " + str(playersList[i].strategy))
