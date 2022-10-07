import re
p = re.compile('(100+1+|01)+')

n = int(input())
for _ in range(n):
    word = input()
    if re.fullmatch(p,word):
        print("YES")
    else:
        print("NO")
