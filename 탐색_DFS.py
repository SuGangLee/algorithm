#깊이우선, stack - 재귀함수
#연결되어있는거 찾을 때 
def dfs(graph,v,visited):
    visited[v] = True # 현재노드 방문처리
    print(v,end=' ')
    for i in graph[v]: #graph[1][0], graph[1][1] ...
            if not visited[i]: 
             dfs(graph,i,visited)

visited= [False]*9
graph = [
 [],
 [2,3,8],
 [1,7],
 [1,4,5],
 [3,5],
 [3,4],
 [7],
 [2,6,8],
 [1,7]
]

dfs(graph,1,visited)
