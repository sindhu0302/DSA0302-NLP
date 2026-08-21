text = """John and Mary went to the park.
He brought a ball.
She wanted to play with it.
The dog chased him excitedly.
Finally, they all went home."""

coreference = {
    "He": "John",
    "She": "Mary",
    "it": "ball",
    "him": "John",
    "they": ["John", "Mary", "dog"]
}

print("Coreference Resolution:")
for mention, antecedent in coreference.items():
    print(mention, "->", antecedent)
