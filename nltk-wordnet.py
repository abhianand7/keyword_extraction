from nltk.corpus import wordnet

syns = wordnet.synsets("program")

print syns

print(syns[0].name())

print (syns[0].lemmas()[0].name())

print (syns[0].lemmas())

print(syns[0].definition())

print(syns[0].examples())

print (wordnet.synsets("good"))



