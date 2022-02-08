import sys
n = int(sys.stdin.readline())

queue=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        queue.append(command[1])

    elif command[0]=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.pop(0)) # pop()은 마지막 원소 삭제. pop(index) index위치에 있는 요소 삭제&print
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1]) 

      