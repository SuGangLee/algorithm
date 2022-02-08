#특정한 조건이 부합할 때만 사용가능 하지만 매우 빠름: 최악의 경우 O(N+K)
# 데이터의 크기가 한정되어 있고, 데이터의 크기가 많이 중복되어 있을수록 유리 
#일반적으로 가장 큰 데이터가 1,000,000 넘지 않을 때 유용 
# 가장 큰 데이터 값만큼의 크기를 가진 별도의 리스트를 선언하여 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시킨다

import random
arr = [ random.randint(15) for _ in range(100)]

sort_list = [0]*(max(arr)+1)

for i in range(len(arr)):
    sort_list[arr[i]] +=1 

for i  in range(len(sort_list)):
    for j in range(sort_list[i]):
        print(i,end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력 
    