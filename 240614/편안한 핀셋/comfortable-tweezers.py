n = int(input())
arr = [[False]*1001 for _ in range(1001)]
check = [[0]*1001 for _ in range(1001)]

count = 0
for i in range(n) :
    a, b = map(int,input().split())
    arr[a][b] = True
    temp = 0
    for x,y in [(-1,0), (1,0), (0,-1), (0,1)] :
        nx,ny = a + x, b + y
        if 0<=nx<=1000 and 0<=ny<=1000 :
            check[nx][ny] += 1
            if check[nx][ny] == 3 and arr[nx][ny]:
                count += 1
                temp += 1
            if check[nx][ny] > 3 and arr[nx][ny]:
                count -= 1

    if temp == 3:
        count += 1

    print(count)