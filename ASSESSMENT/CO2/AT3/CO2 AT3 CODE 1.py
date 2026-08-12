import re
from nltk.stem import PorterStemmer
ps = PorterStemmer()
text = "infection infectious infected infect organization organizing"
words = re.findall(r"[a-zA-Z]+", text.lower())
for word in words:
    print(word, "->", ps.stem(word))
