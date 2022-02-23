# 각 원소의 루트노드가 동일하다면, 사이클 형성된 것

#경로압축기법 소스코드 -> 각 노드에 대하여 find 함수를 호출한 이후에 해당 노드의 루트노드가 바로 부모노드가 된다. 
# 즉, union 연산 시 루트노드에 더 빠르게 접근 가능!
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a= find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b: 
        parent[b] = a
    else:
        parent[a] =b 

v,e = map(int,input().split()) #노드(v)와 간선(e-연산개수)
parent = [0]*(v+1) #부모테이블 자기 자신으로 초기화

for i in range(1,v+1):
    parent[i] = i 

cycle = False

#union연산 수행
for i in range(e):
    a,b = map(int,input().split())
    
    if find_parent(parent,a) == find_parent(parent,b):
        cycle=True
        break 
    else:
        union(parent,a,b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 안 발생 ")