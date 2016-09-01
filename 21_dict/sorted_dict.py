# As simple as: sorted(dict1, key=dict1.get)

# Well, it is actually possible to do a "sort by dictionary values". Recently I had to do that in a Code Golf (Stack Overflow question Code golf: Word frequency chart). Abridged, the problem was of the kind: given a text, count how often each word is encountered and display list of the top words, sorted by decreasing frequency.

# If you construct a dictionary with the words as keys and the number of occurences of each word as value, simplified here as

d = defaultdict(int)
for w in text.split():
  d[w] += 1
# then you can get list of the words in order of frequency of use with sorted(d, key=d.get) - the sort iterates over the dictionary keys, using as sort-key the number of word occurrences.

for w in sorted(d, key=d.get, reverse=True):
  print w, d[w]