import math
import itertools
# Input
num = int(input('Enter number of feet: '))
limit = int(input('Number of Possible Solutions: '))

# Processing
numOf12 = math.ceil(num / 12)
numOf16 = math.ceil(num / 16)
numOf20 = math.ceil(num / 20)

# Sum Function


def sum(lst):
    return int((lst[0] * 12) + (lst[1] * 16) + (lst[2] * 20))


permutations = [n for n in itertools.product([i for i in range(
    numOf12 + 1)], [i for i in range(numOf16 + 1)], [i for i in range(numOf20 + 1)])]

permDict = {}
for combination in permutations:
    permSum = sum(combination)
    if permSum in permDict.keys():
        permDict[permSum].append(combination)
    else:
        permDict[permSum] = [combination]

# Logic
print('Solutions: ')
printed = 0
for i in range(100):
    currentKey = num + i
    if currentKey in permDict.keys():
        printed += 1
        print(f'{currentKey}: {permDict[currentKey]}')
    if printed >= limit:
        break
