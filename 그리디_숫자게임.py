N,M = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(M)]
s=[]
for i in range(N):
    s.append(min(arr[i]))

print(max(s))