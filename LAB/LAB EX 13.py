import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'John'
VP -> 'runs'
""")

parser = ChartParser(grammar)

sentence = ['John', 'runs']

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
