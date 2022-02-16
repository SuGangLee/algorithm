n,m = map(int,input().split())
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

for x in range(1,n+1):
    for y in range(n):
        if x==y:
            graph[x][y] = 0

for i in range(m):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x]=1

x, k = map(int,input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

distance = graph[1][k] + graph [k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)

         

