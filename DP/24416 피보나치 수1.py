def fib(n):
    global ret
    if(n==1 or n==2):
        ret += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def dpd(n):
    global dp
    global dp_count
    for i in range(3,n+1):
        dp_count+=1
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

import sys
n = int(sys.stdin.readline())
ret =0
dp = [0]*(n+1)
dp_count = 0
dp[1] = 1
dp[2] = 1

fib(n)
dpd(n)
print(ret, dp_count)

