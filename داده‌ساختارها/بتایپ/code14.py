S = input()
stack = []

for char in S:
    if char != '=':
        stack.append(char)
    elif stack:
        stack.pop()

print(''.join(stack))
