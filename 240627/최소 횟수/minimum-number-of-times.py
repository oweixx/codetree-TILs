from collections import deque
a, b = map(int,input().split())

def bfs() :
    q = deque()
    q.append(a)

    while q :
        x = q.popleft()
        if x == b :
            break
        if x*2 <=100001 and dp[x*2] == 0:
            q.append(x*2)
            dp[x*2] = dp[x]
        if 0<= x-1 <= 100001 and dp[x-1] == 0 :
            q.append(x-1)
            dp[x-1] = dp[x] + 1
        if 0<= x+1 <= 100001 and dp[x+1] == 0 :
            q.append(x+1)
            dp[x+1] = dp[x] + 1


dp = [0]*100002
bfs()
print(dp[b])