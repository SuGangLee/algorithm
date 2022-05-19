#크루스칼 알고리즘으로 최소 신장 트리를 찾고, 가장 비용이 큰 간선을 제거한다. 

def find_parent(parent,x):
    if parent[x] != x:
        find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a
    
 #노드와 간선 개수 입력
n,m = map(int,input().split())
parent = [0]*(n+1)

    #모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges=[]
result = 0 
    
for i in range(1,n+1):
    parent[i] = i
    
    #모든 간선 정보 입력받기
for i in range(m):
    a,b,cost = map(int,input().split())
    #비용 순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append([cost,a,b])
    
edges.sort() 
last=0 #최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선

    #간선 하나씩 확인
for edge in edges:
    cost,a,b = edge
    #사이클이 없는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result +=cost 
        last =cost

print(result-last) # 가장 비용이 큰 간선 제거 
