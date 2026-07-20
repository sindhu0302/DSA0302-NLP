import re

# Product list
products = [
    "Laptop",
    "Laptop Bag",
    "Gaming Laptop",
    "Mouse",
    "Wireless Mouse",
    "Keyboard",
    "Mechanical Keyboard",
    "Smart Phone",
    "Phone Charger",
    "Bluetooth Speaker"
]

keyword = input("Enter search keyword: ")

# Exact Search
exact = [p for p in products if re.fullmatch(keyword, p)]

# Prefix Search
prefix = [p for p in products if re.match(keyword, p)]

# Suffix Search
suffix = [p for p in products if re.search(keyword + r"$", p)]

# Partial Search
partial = [p for p in products if re.search(keyword, p)]

# Case-Insensitive Search
ignore_case = [p for p in products if re.search(keyword, p, re.IGNORECASE)]

print("\nExact Search:", exact)
print("Total:", len(exact))

print("\nPrefix Search:", prefix)
print("Total:", len(prefix))

print("\nSuffix Search:", suffix)
print("Total:", len(suffix))

print("\nPartial Search:", partial)
print("Total:", len(partial))

print("\nCase-Insensitive Search:", ignore_case)
print("Total:", len(ignore_case))
