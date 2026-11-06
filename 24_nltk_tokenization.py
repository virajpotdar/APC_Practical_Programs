from nltk.tokenize import wordpunct_tokenize

sentence = "Python is easy to learn and use."
words = wordpunct_tokenize(sentence)

print("Original sentence:", sentence)
print("Tokens:", words)
