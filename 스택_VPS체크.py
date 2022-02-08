import sys
command = list(sys.stdin.readline())
command.pop()

stack=[]
for i in range(len(command)):
    if command[i] == '(':
        stack.append('(')
        print(stack)
    elif command[i] == ')':
        if not stack:
            print('NO')
        stack.pop()

if not stack:
    print('YES')
else : 
    print('NO')

