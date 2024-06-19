div = 1000000007
n, m = map(int,input().split())

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, m+1) :
    dp[0][i] = 1

for i in range(1, n) :
    for j in range(m, 0, -1) :
        for k in range(j//2, 0, -1) :
            dp[i][j] = (dp[i][j] + dp[i-1][k])%div

print(sum(dp[n-1])%div)