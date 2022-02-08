size_x,size_y = map(int,input().split())
x,y,d=map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(size_y)]
count=1

while True:
    arr[y][x] = 2
    #break 체크
    if arr[y][x-1] !=0  and arr[y][x+1] !=0  and arr[y-1][x] !=0  and arr[y+1][x] !=0  :
        break
        
    if d == 0:
        if arr[y][x-1]==0:
            x=x-1
            d=3
            count+=1
            print('왼쪽이동')
        else:
            d=3 
    elif d==1: 
        if arr[y-1][x] == 0:
            y=y-1
            d=0
            count+=1
            print('위쪽이동')
        else:
            d=0
    elif d==2: 
        if arr[y][x+1] == 0:
            x=x+1
            d=1
            count+=1
            print('오른쪽이동')
        else:
            d=1
    elif d==3: 
        if arr[y+1][x] == 0:
            y=y+1
            d=2
            count+=1
            print('아래쪽이동')
        else:
            d=2

print(count)