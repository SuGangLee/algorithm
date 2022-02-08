
l = list(map(int, input().split()))

l.sort()
result = 0
count = 0 # 현재그룹에 포함된 모험가 수
for i in l:
    count += 1
    if count >= i : # 현재 그룹에 포함된 모험가 수가 현재 공포도 이상
        result += 1
        count = 0
print (result)

