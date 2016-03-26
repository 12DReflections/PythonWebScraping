import re

outputList = open("wordRank.txt", "w+")
wordString = open('words.txt').read().lower()

# Tokenize all words to list
wordList = re.findall(r"[\w']+", wordString)



# deduplicate and sort
deduplicatedList = sorted(set(wordList))
print deduplicatedList

for word in deduplicatedList:
	print >> outputList, word

outputList.close() 