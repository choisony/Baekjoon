import sys
n,m = map(int,sys.stdin.readline().split())
graph= []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
dp = [[0]* (n+1) for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j]+ dp[i][j-1] - dp[i-1][j-1] + graph[i-1][j-1]

for _ in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)
    
    
###-----시간초과----------------------------------
# n,m = map(int,input().split())
# graph= []
# for _ in range(n):
#     graph.append(list(map(int,input().split())))
#
# to_sum = [[0]*n for _ in range(n)]
# temp = 0
# for i in range(n):
#     for j in range(n):
#         temp += graph[i][j]
#         to_sum[i][j] = temp
# #### to_sum 은 그래프에서 i행 j열까지의 합
#
# ###[1,2,3,4,5,6,7,8,9,10] 이라는 배열이 있을 때
# ###각 열까지의 합의 배열은
# ###[1,3,6,10,15,21,28,36,45,55] 인데
# ### 6 ~ 9열까지의 합은 (9열까지의 합) - (5열까지의 합)이다
# ### 45 - 15 = 30
# ### 6+7+8+9 = 30
# ### 이 원리를 이용해서 풀었음
#
# for i in range(m):
#     x1,y1,x2,y2 = map(int,input().split())
#     x1 -=1
#     y1 -=1
#     x2 -=1
#     y2 -=1
#     ans = 0
#     for j in range(x1,x2+1):
#         if y1 > 0:
#             ans += to_sum[j][y2] - to_sum[j][y1-1]
#             continue
#         elif y1 ==0 and j==0:
#             ans += to_sum[j][y2]
#             continue
#         elif y1 ==0 and j!=0:
#             ans += to_sum[j][y2] - to_sum[j-1][n-1]
#             continue
#     print(ans)
