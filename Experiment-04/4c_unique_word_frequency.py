from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import gutenberg

sample = gutenberg.raw("austen-emma.txt")
tokens = word_tokenize(sample)

word_frequency = Counter(tokens[:50])

print("EXPERIMENT 4c: UNIQUE WORD FREQUENCY")

for word, frequency in word_frequency.items():
    print(word, ":", frequency)
