#1. union , find 연산으로 이루어짐 

#특정 원소가 속한 집합 찾기
"""def find_parent(parent,x): #이렇게 되면 
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x """
#경로압축기법 소스코드 -> 각 노드에 대하여 find 함수를 호출한 이후에 해당 노드의 루트노드가 바로 부모노드가 된다. 
# 즉, union 연산 시 루트노드에 더 빠르게 접근 가능!
def find_parent(parent,x): #이렇게 되면 
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

#union연산 수행
for i in range(e):
    a,b = map(int,input().split())
    union(parent,a,b)

print("각 원소가 속한 집합:",end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')

print()
print("부모테이블:",end='')
for i in range(1,v+1):
    print(parent[i],end=' ')
