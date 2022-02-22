#노드의 개수가 적을 경우 유리
INF = int(1e9)
#A->B노드를 이동할 떄 n번 노드를 거쳐서 이동하는 경로 중 비용 최솟값 찾기
#A -> n -> B

#플로이드 워셜 알고리즘 : n=1을 거쳐서 이동하는 경로 중 최솟값 찾기-> D23, D24, D32, D34, D42, D43 이 여섯가지 경우 중 하나. 
#  D23 = min(D23/1을 거치지 않고 곧 바로 이동,D2->1 + D1->3/1거쳐 이동) 

n,m = map(int,input().split()) # n=노드개수, m=간선
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기자신 -> 자기자신으로 가는 비용은 0 
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    #a->b로 가는 비용,c
    a,b,c = map(int,input().split())
    graph[a][b] =c

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

#수행 결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] ==INF:
            print ("&",end=' ')
        else:
            print(graph[a][b],end=" ")
    print()
    
