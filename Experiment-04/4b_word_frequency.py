from nltk.tokenize import word_tokenize
from nltk.corpus import gutenberg

sample = gutenberg.raw("austen-emma.txt")
tokens = word_tokenize(sample)

words = tokens[:50]
word_frequency = [words.count(word) for word in words]

print("EXPERIMENT 4b: WORD FREQUENCY")
print(list(zip(words, word_frequency)))
