#가장 적은 비용으로 모든 노드를 연결할 수 있는 알고리즘으로 그리디 알고리즘에 속한다. 
#1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
#2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
#   - 사이클이 발생하면 최소 신장 트리에 포함 X , 발생 안하면 트리에 포함

#특정 원소가 속한 집합 찾기
from re import A


def find_parent(parent,x):
    if parent[x] != x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합 찾기, 작은 쪽이 부모
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b= find_parent(parent,b)
    if a>b:
        parent[a] = b
    else:
        parent[b]=a 

v,e = map(int,input().split())
parent = [0]*(v+1)

edges =[]
result =0

for i in range(1,v+1): #부모 자기자신으로 초기화
    parent[i] = i

#모든 간선에 대한 정보 입력받기
for i in range (e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b)) #비용순으로 정렬하기위해 튜플의 첫 번째 원소를 비용으로 설정

edges.sort()

for edge in edges:
    cost,a,b= edge
    #사이클이 발생하지 않는 경우(부모노드가 다른 경우) 에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)
    

