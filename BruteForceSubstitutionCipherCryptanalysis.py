import itertools

encryptedMessage = input("Enter encrypted message: ").lower()

alphabet = [ chr(i) for i in range(ord('a'), ord('z')+1) ]
itertools_permutations = itertools.permutations(alphabet)
combinations = []
for combin in itertools_permutations:
  combination = [val for val in combin]
  combinations.append({ (combination[i], chr(i+ord('a'))) for i in range(len(combination)) })

messageList = []
for alphabetTransformation in combinations:
  simpleEncryptedMessage = ""
  for i in encryptedMessage:
    if i in alphabetTransformation:
      simpleEncryptedMessage += alphabetTransformation[i]
    else:
      simpleEncryptedMessage += i
  messageList.append(simpleEncryptedMessage)

print(messageList)
