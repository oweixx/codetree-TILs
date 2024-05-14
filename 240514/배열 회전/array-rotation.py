import sys
input = sys.stdin.readline

def rotate(x) :
    temp = maps[x][x]

    for i in range(x, m-x-1) :
        maps[x][i] = maps[x][i+1]
    for i in range(x, n-x-1) :
        maps[i][m-x-1] = maps[i+1][m-x-1]
    for i in range(x, m-x-1) :
        maps[n-x-1][m-i-1] = maps[n-x-1][m-i-2]
    for i in range(x, n-x-1) :
        maps[n-i-1][x] = maps[n-i-2][x]
    maps[x+1][x] = temp


n, m, k = map(int,input().split())

maps = []
for _ in range(n) :
    s = list(map(int,input().split()))
    maps.append(s)

minnum = min(n,m)
minnum = minnum//2

for _ in range(k) :
    for i in range(minnum) :
        rotate(i)
for i in maps :
    print(*i)