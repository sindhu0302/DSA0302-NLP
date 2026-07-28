# DFA for strings ending with "ab"

transition = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}

start_state = 'q0'
final_state = 'q2'

string = input("Enter Input String: ")

state = start_state
path = [state]

for ch in string:
    if ch not in ['a', 'b']:
        print("Invalid Input")
        exit()

    state = transition[state][ch]
    path.append(state)

print("Transition Path:")
print(" → ".join(path))

if state == final_state:
    print("Accepted")
else:
    print("Rejected")
