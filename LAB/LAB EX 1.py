import re

text = "Python Programming"

pattern = "Python"

result = re.search(pattern, text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")
    
