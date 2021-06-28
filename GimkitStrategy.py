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
        for j in range(10):
            self.money = 0
            self.levelPerCategory = {"q": 1, "s": 1, "m": 1}
            index = 0
            streak = False
            for i in range(turns):
                if index == len(self.strategy):
                    self.turnsUsed.append(i)
                    index += 1
                elif index < len(self.strategy):
                    goal = self.strategy[index]
                    goalInCost = game.upgradeCosts[goal][self.levelPerCategory[goal]]
                    if self.money >= goalInCost:
                        # Upgrade
                        self.levelPerCategory[goal] += 1
                        self.money -= goalInCost
                        index += 1
                # Answer question
                # Answered question correctly
                if random.random() <= self.accuracy:
                    # Answered correctly
                    self.money += math.ceil((game.upgradeValues["q"][self.levelPerCategory["q"] - 1] + (
                        (1 if streak else 0) * game.upgradeValues["s"][self.levelPerCategory["s"] - 1]) * game.upgradeValues["m"][self.levelPerCategory["m"] - 1]))
                    streak = True
                else:
                    # Answered incorrectly
                    self.money -= math.ceil(game.upgradeValues["q"][self.levelPerCategory["q"] - 1]
                                            * game.upgradeValues["m"][self.levelPerCategory["m"] - 1])
                    streak = False
            self.averageScore.append(self.money)

def permutations(listCombination, numSet):
  first_permutations=[]
  first_permutations.append(listCombination)
  for i in range(len(['q', 's', 'm'])):
    if listCombination.count(['q', 's', 'm'][i])<numSet[i]:
      newList=list(listCombination)
      newList.append(['q', 's', 'm'][i])
      first_permutations+=permutations(newList, numSet)
  return first_permutations

filtered_permutations=permutations([], [5, 5, 5])
# Making players and running them
playersList = [Player(list(i)) for i in filtered_permutations]
for player in playersList:
    player.run(Game(10))


def myMoneySort(player):
    return sum(player.averageScore) / len(player.averageScore)


playersList.sort(key=myMoneySort, reverse=True)
f=open("GimkitStrategy.txt", "w")
for i in range(len(playersList)):
    f.write(str(i + 1) + ". Money: " + str(int(myMoneySort(playersList[i]))) + str(playersList[i].averageScore) +
          "---Turns Used: " + str(playersList[i].turnsUsed) +
          "---Strategy: " + str(playersList[i].strategy)+"\n")
    print(i)
    #print(str(i + 1) + ". Money: " + str(int(myMoneySort(playersList[i]))) + str(playersList[i].averageScore) +
    #      "---Turns Used: " + str(playersList[i].turnsUsed) +
    #     "---Strategy: " + str(playersList[i].strategy))
f.close()
print("Finished!")
# def myTurnSort(player):
#     return sum(player.turnsUsed) / len(player.turnsUsed)


# playersList.sort(key=myTurnSort)
# for i in range(20):
#     print()
# for i in range(len(playersList)):
#     print(str(i + 1) + ". Money: " + str(playersList[i].money) +
#           "---Turns Used: " + str(playersList[i].turnsUsed) +
#           "---Strategy: " + str(playersList[i].strategy))
