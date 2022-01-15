n = int(input())
max_n = int(1e9)
dp = [[0]*n for i in range(n)]
home= []
for i in range(n):
    l= list(map(int,input().split()))
    home.append(l)

answer = max_n
for color in range(3):
    for i in range(3):
        if color == i:
            dp[0][i] = home[0][i]
        else:
            dp[0][i] = max_n

    for j in range(1,n):
        dp[j][0] = home[j][0] + min(dp[j-1][1],dp[j-1][2])
        dp[j][1] = home[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = home[j][2] + min(dp[j-1][0], dp[j-1][1])

    for i in range(3):
        if color==i:
            continue
        else:
            answer = min(answer,dp[n-1][i])
print(answer)