n = int(input())
command = input().split()
result= [1,1]
for i in (command):   
    if i == 'R':
        if result[1] >= n :
            continue
        else :
            result[1]+=1
    if i == 'L':
        if result[1] <= 1 :
            continue
        else: result[1]-=1
    if i == 'D':
        if result[0] >= n:
            continue
        else: result[0]+=1
    if i == 'U':
        if result[0] <= 1 :
            continue
        else: result[0]-=1

print(result) 