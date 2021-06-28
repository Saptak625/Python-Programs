from essential_generators import DocumentGenerator
import random
generator = DocumentGenerator()
icnums = []
alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

def decryptSubstitution(encryptedMessage, alphabet):
  englishFrequency = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd',
                    'c', 'u', 'm', 'f', 'g', 'p', 'w', 'y', 'b', 'v', 'k', 'j', 'x', 'z', 'q']
  alphabetTransformation = {englishFrequency[i]: alphabet[i] for i in range(len(alphabet))}
  simpleEncryptedMessage = ""
  for i in encryptedMessage:
    if i in alphabetTransformation:
      simpleEncryptedMessage += alphabetTransformation[i]
    else:
      simpleEncryptedMessage += i
  return simpleEncryptedMessage

def calcIC(cipher_text):
  import collections
  #Calculate the Index of Coincidence of a piece of text. Allows for identification of a cipher encryption method.
  # Removing all non alpha and whitespace and uppercasing
  cipher_flat = "".join([x.upper() for x in cipher_text.split() if  x.isalpha()])
  # Setting up variables
  N = len(cipher_flat)
  freqs = collections.Counter( cipher_flat )
  alphabet =  map(chr, range( ord('A'), ord('Z')+1))
  freqsum = 0.0
  # Calculations
  for letter in alphabet:
      freqsum += freqs[ letter ] * ( freqs[ letter ] - 1 )
  IC = freqsum / ( N*(N-1) )
  return IC

for i in range(10000):
    random.shuffle(alphabet)
    encryptedMessage = decryptSubstitution(generator.paragraph(), alphabet)
    icnums.append(calcIC(encryptedMessage))
print(icnums)
print("\n\n\n\n", min(icnums), sum(icnums)/len(icnums), max(icnums))
print(len([i for i in icnums if i>=0.053]))
