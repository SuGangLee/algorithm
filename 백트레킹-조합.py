N, M  = map(int,input().split())

visited = [False]*N
result = []

def solve(depth, N,M) :
    if depth == M :
        print(' '.join(map(str,result)))
        return 
    for i in range(len(visited)) : 
        if visited[i] == False :  
            visited[i]=True
            result.append(i+1)
            solve(depth+1,N,M) # 깊이 우선 탐색 
            visited[i]=False
            result.pop()
            
solve(0,N,M)

