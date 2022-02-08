n = int(input())
flag=1
for i in range (0,n-1):
    command=list(input())
    size=int(input())
    array = list(map(int,input().rstrip()[1:-1].split(","))) #rstrip()[1:-1]: 맨 앞,뒤 문자 제거, 이코드의 경우 []문자 제거
    for j in range (0,len(command)-1):
        if command[j] == 'R':
            array.reverse()
        elif command[j] == 'D' :
            if not array:
                print('error')
                flag=0
                break
            else:
                del array[0]
    if flag==1:
        print(array)
