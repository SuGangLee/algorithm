s= list(map(int,input()))
front = s[:len(s)//2]
back = s[len(s)//2:]

if sum(front)==sum(back):
    print('lucky')
else:
    print('ready')
