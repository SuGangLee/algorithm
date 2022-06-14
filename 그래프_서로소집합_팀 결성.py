#같은 팀 여부 확인
def find_parent(parent,x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    if find_parent(parent,a) !=  find_parent(parent,b):
        if a > b:
            parent[a] = b
        else:
            parent[b]=a

N,M = map(int,input().split())
parent =[ i for i in range(N+1)]

    
for _ in range(M):
    method, a,b = map(int,input().split())
    if method == 0:
        union_parent(parent,a,b)
    elif method ==1:
        if find_parent(parent,a) != find_parent(parent,b):
            print('NO')
        else:
            print('yes')



