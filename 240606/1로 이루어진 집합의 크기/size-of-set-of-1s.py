from collections import deque
def bfs(i,j) :
    q = deque()
    q.append((i,j))
    check[i][j] = True
    maps[i][j] = temp
    count = 1
    while q :
        x, y = q.popleft()

        for nx, ny in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] :
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and not check[nx][ny] :
                maps[nx][ny] = temp
                check[nx][ny] = True
                q.append((nx,ny))
                count += 1

    sum_count.append(count)

n, m = map(int,input().split())

maps = []
sum_count = [0,0]
for _ in range(n) :
    s = list(map(int,input().split()))
    maps.append(s)

check = [[False]*m for _ in range(n)]
temp = 1
for i in range(n) :
    for j in range(m) :
        if maps[i][j] == 1 and not check[i][j] :
            temp += 1
            bfs(i,j)

new_count = []
for i in range(n) :
    for j in range(m) :
        if not maps[i][j] :
            temp = 1
            s = set()
            for nx, ny in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)] :
                if 0<=nx<n and 0<=ny<m and maps[nx][ny] :
                    s.add(maps[nx][ny])
            
            for x in s :
                temp += sum_count[x]
            new_count.append(temp)
            

#print(sum_count)
#print(new_count)

result = 0
if len(new_count) == 0 :
    if max(sum_count) != n*m :
        result = max(sum_count) + 1
    else :
        result = max(sum_count) - 1

else :
    result = max(max(sum_count)+1, max(new_count))

print(result)