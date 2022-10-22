source = input()
bomb = input()
len_bomb = len(bomb)

stack = []
for i in source:
    stack.append(i)
    if stack[-1] == bomb[-1] and ''.join(stack[-len_bomb:]) == bomb:
        for j in range(len_bomb):
            stack.pop()
print(''.join(stack)) if stack else print("FRULA")

