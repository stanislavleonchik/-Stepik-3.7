exceptDictionary = {}
numOfKnownWords = int(input())
knownWords = []
for i in range(numOfKnownWords):
    knownWords.append(input().lower())
numOfStrings = int(input())
textStrings = []
for i in range(numOfStrings):
    textStrings.append(input().lower())
for sentence in textStrings:
    for word in sentence.split():
        if word not in knownWords:
            exceptDictionary[word] = 1
for i in exceptDictionary.keys():
    print(i)