#탐사여부 - 결과 리스트 - 재귀함수 : 깊이가 M이 되면 반복문 탈출, 탐색하지 않았을 경우에 진행 (for 중복제거) , 탐색시작 시 탐색 여부 바꾸고 탐색 내용 추가, 탐색 후 탐색 내용 pop)


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
