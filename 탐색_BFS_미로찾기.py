from collections import deque
N,M = map(int,input().split())

graph =[]
for i in range(N):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    

    while queue: #큐가 빌 때 까지
        print(queue)
        x,y=queue.popleft()
        
        #네 방향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위 벗어남
            if nx < 0 or ny < 0 or nx >= N or ny >=M :
                continue
            #벽인 경우
            if graph[nx][ny] == 0 :
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단거리기록
            if graph[nx][ny] == 1: 
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    print(graph)
    return graph[N-1][M-1] # 가장 오른쪽 아래까지의 최단거리

print(bfs(0,0))


