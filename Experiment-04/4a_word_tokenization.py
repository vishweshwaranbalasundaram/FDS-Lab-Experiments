import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import gutenberg

nltk.download("gutenberg")
nltk.download("punkt")
nltk.download("punkt_tab")

sample = gutenberg.raw("austen-emma.txt")
tokens = word_tokenize(sample)

print("EXPERIMENT 4a: WORD TOKENIZATION")
print("First 50 tokens:")
print(tokens[:50])
