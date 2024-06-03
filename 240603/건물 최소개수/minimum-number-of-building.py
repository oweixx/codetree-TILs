n = int(input())

lst = []
for _ in range(n) :
    a, b = map(int,input().split())
    lst.append(b)

count = 0
stack = []
for i in lst :
    if len(stack) != 0 and stack[-1] > i :
        while len(stack) != 0 :
            if stack[-1] > i :
                count += 1
                stack.pop()
            else :
                break
        
        if len(stack) == 0 and i != 0 :
            stack.append(i)
        elif len(stack) != 0 and stack[-1] != i :
            stack.append(i)
    
    elif i != 0 :
        if len(stack) == 0 :
            stack.append(i)
        elif stack[-1] != i :
            stack.append(i)

    #print(stack, count)
print(count + len(stack))