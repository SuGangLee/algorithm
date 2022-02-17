#우선순위 큐 라이브러리 > 최소 힙 구조 사용- 값이 낮은 데이터를 먼저 삭제 하는 
#튜플 데이터를 (거리,노드)로 큐에 삽입 
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) 


n,m,start = map(int,input().split())#노드, 간선 개수 입력

# 각노드에 연결되어있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range (n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

def dijkstra (start):
    q=[]
    heapq.heappush(q,(0,start)) 
    distance[start] = 0
    while q: #큐가 비어있지 않다면
        dist,now = heapq.heappop(q) #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        # 처리된 적 있는 노드라면 무시
        if distance[now] < dist :
            continue
        #현재 노드와 인접한 다른 노드들 확인 
        for i in graph[now]:
            cost = dist +i[1]
            if cost < distance[i[0]]:
                distance [i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
count = 0
max_distance= 0 # 도달할 수 있는 노드중에서, 가장 멀리 있는 노드와의 최단 거리
for d in distance:
    if d != INF:
        count+=1
        max_distance  = max(max_distance,d)

print(count-1, max_distance)
