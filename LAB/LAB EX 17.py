from nltk.corpus import wordnet

word = "car"

synsets = wordnet.synsets(word)

for syn in synsets[:3]:
    print(syn.name())
    print(syn.definition())
