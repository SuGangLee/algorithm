INF = int(1e9)
n,m = map(int,input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신으로 가는 경로는 0으로 초기화 
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] =0 

#각 간선의 값으로 초기화
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1

x, k = map(int,input().split())

#K를 거쳐가 X에 도달하는 최솟값 점화식
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

#K를 거쳐가 X에 도달하는 거리 
distance = graph[1][k]+graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)
