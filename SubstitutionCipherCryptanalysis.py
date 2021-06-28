from langdetect import detect_langs

encryptedMessage = input("Enter encrypted message: ").lower()

englishFrequency = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd',
                    'c', 'u', 'm', 'f', 'g', 'p', 'w', 'y', 'b', 'v', 'k', 'j', 'x', 'z', 'q']
unigrams = ['a', 'i']
bigrams = ['of', 'to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he',
           'by', 'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no', 'us', 'am']
trigrams = ['the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'any', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has',
            'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use']
quadrams = ['that', 'with', 'have', 'this', 'will', 'your', 'from',
            'they', 'know', 'want', 'been', 'good', 'much', 'some', 'time']


def frequencyAnalysis(message):
  allCharacters = {}
  for i in encryptedMessage:
    if i in allCharacters:
      allCharacters[i] += 1
    else:
      if i.isalpha():
        allCharacters[i] = 1

  tupleList = [(allCharacters[key], key) for key in allCharacters]

  def mySort(e):
    return e[0]
  tupleList.sort(key=mySort, reverse=True)
  return tupleList


frequencyAnalysis = frequencyAnalysis(encryptedMessage)
print(frequencyAnalysis)


def permutateFrequencies(frequencyList, n=3):
  # Make ranges of characters
  frequencies = [i[0] for i in frequencyList]
  characters = [i[1] for i in frequencyList]
  rangeList = []
  frequenciesChecked = []
  for freq in frequencies:
    if freq in frequenciesChecked:
      continue
    currentRange = [i for i in range(freq - n + 1, freq + 1)][::-1]
    frequenciesChecked.append(freq)
    lettersInRange = []
    for num in currentRange:
      if num in frequencies:
        index = frequencies.index(num)
        if index != -1:
          while frequencies[index] >= num:
            lettersInRange.append(characters[index])
            index += 1
            if index >= len(frequencies):
              break
    rangeList.append((currentRange, lettersInRange))
  # Generating character range list
  rangeCharacters = {}
  for currentTuple in rangeList:
    for letter in currentTuple[1]:
      if letter in rangeCharacters:
        rangeCharacters[letter].append(currentTuple[0])
      else:
        rangeCharacters[letter] = [currentTuple[0]]
  finalRangeCharacters = {
      i: rangeCharacters[i] for i in rangeCharacters if len(rangeCharacters[i]) > 1}
  perms = 1
  for i in finalRangeCharacters:
    perms *= len(finalRangeCharacters[i])
  print(perms)
  # Generate pseudo range lists
  import copy
  pseudorangeList = [rangeList]
  for character in finalRangeCharacters:
    newPseudorangeList = []
    for rangeKey in finalRangeCharacters[character]:
      # Iterate through rangeKeys
      for currentPerm in pseudorangeList:
        # Find rangeKey in currentPerm
        newPerm = copy.deepcopy(currentPerm)
        for ind in range(len(currentPerm)):
          if character in currentPerm[ind][1] and currentPerm[ind][0] != rangeKey:
            newPerm[ind][1].remove(character)
        newPseudorangeList.append(newPerm)
    pseudorangeList = newPseudorangeList
  # Permutate to create new frequency lists
  import itertools
  newFrequencyLists = []
  for currentRangeList in pseudorangeList:
    # Getting range list
    currentFrequencyLists = [[]]
    for currentTuple in currentRangeList:
      permutations = [i for i in itertools.permutations(currentTuple[1])]
      #print("Permutations", permutations)
      for perm in permutations:
        for currentList in currentFrequencyLists:
          newCurrentFrequencyLists = []
          newCurrentFrequencyLists.append(
              copy.deepcopy(currentList) + list(perm))
      currentFrequencyLists = newCurrentFrequencyLists
    newFrequencyLists += currentFrequencyLists
  return newFrequencyLists

newFrequencies = permutateFrequencies(frequencyAnalysis)
print(newFrequencies)
print(len(newFrequencies))

def decryptSubstitution(alphabet):
  alphabetTransformation = {englishFrequency[i]: alphabet[i] for i in range(len(alphabet))}
  simpleEncryptedMessage = ""
  for i in encryptedMessage:
    if i in alphabetTransformation:
      simpleEncryptedMessage += alphabetTransformation[i]
    else:
      simpleEncryptedMessage += i
  return simpleEncryptedMessage

solutions = [decryptSubstitution(alphabet) for alphabet in newFrequencies]

#Find Solution that is most englishishy
def sortByEnglishMatch(e):
  prob = 0
  for i in detect_langs(e):
    if str(i)[0:2] == 'en':
      prob = float(str(i)[3:])
  if ' ' not in e:
    prob -= 0.2
  return prob
print("\n\n\n\n\n")
for i in range(len(solutions)):
  print(str((i+1))+". ", solutions[i]+'\n')
solutions.sort(key=sortByEnglishMatch, reverse=True)
