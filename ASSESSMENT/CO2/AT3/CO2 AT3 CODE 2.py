prefixes = ["un", "re", "in", "dis"]
suffixes = ["ing", "ed", "est", "able", "s"]
def parser(word):
    prefix = ""
    suffix = ""
    root = word
    for p in prefixes:
        if root.startswith(p):
            prefix = p
            root = root[len(p):]
            break
    for s in suffixes:
        if root.endswith(s):
            suffix = s
            root = root[:-len(s)]
            break
    return prefix, root, suffix
words = ["happiest", "unbelievable", "running",
         "reordering", "smartphones", "unreadable"]
for word in words:
    print(word, "->", parser(word))
