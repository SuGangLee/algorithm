import time
import random

#정렬이 거의 되어있는 상황에 유리, 최선의 시간복잡도 O(N)
arr2 = [random.randint(1,11) for _ in range(10)]


for i in range (1,len(arr2)):
    for j in range(i,0,-1):
        if arr2[j] < arr2[j-1]: 
            arr2[j],arr2[j-1] =  arr2[j-1],arr2[j]
        else: 
            break
print(arr2 )