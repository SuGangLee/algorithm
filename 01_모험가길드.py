
l = list(map(int, input().split()))

l.sort()
result = 0
"""count = 0 # 현재그룹에 포함된 모험가 수
for i in l:
    count += 1
    if count >= i : # 현재 그룹에 포함된 모험가 수가 현재 공포도 이상
        result += 1
        count = 0
print (result)"""
i=0
#2번째 풀이 
#인덱스가 리스트의 길이를 넘어가면 break
while True :
    i+=l[i]
    if i > len(l)-1:
        break
    else: result+=1

print(result)



