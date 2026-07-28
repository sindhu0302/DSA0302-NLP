import re

text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
"""

while True:
    print("\nMenu")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print(re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text))

    elif choice == 2:
        print(re.findall(r'\b[6-9]\d{9}\b', text))

    elif choice == 3:
        print(re.findall(r'#\w+', text))

    elif choice == 4:
        print(re.findall(r'@\w+', text))

    elif choice == 5:
        prefix = input("Enter Prefix: ")
        pattern = r'\b' + re.escape(prefix) + r'\w*'
        print(re.findall(pattern, text))

    elif choice == 6:
        suffix = input("Enter Suffix: ")
        pattern = r'\b\w*' + re.escape(suffix) + r'\b'
        print(re.findall(pattern, text))

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
