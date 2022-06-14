from itertools import combinations

N,M = map(int,input().split())
inf = 1000
graph = [ list(map(int,input().split())) for _ in range(N)] 
home =[]
chiken = []

for i in range(N):
    for j in range(N):
        if graph[i][j] ==1:
            home.append((i,j))
        if graph[i][j] ==2:
            chiken.append((i,j))


#치킨집 뽑는 조합
test = list(combinations(chiken, M))

#각 조합에서의 치킨거리를 모두 합해 도시의 치킨거리를 구하는 함수
def get_sum(test):
    result = 0
    for hx,hy in home:
        temp = inf
        for cx,cy in test:
            temp = min(temp,abs(hx-cx)+abs(hy-cy))
        result += temp 
    return result
            
result = inf

#도시의 치킨거리까지를 비교해서 가장 작은 도시 치킨 거리를 출력한다. 
for i in test:
    result = min(result , get_sum(i))


print(result)


            
        



        


