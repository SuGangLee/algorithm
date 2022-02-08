N = int(input())
store= list(map(int,input().split()))
M = int(input())
customer = list(map(int,input().split()))

def binary(arr,target,start,end):
    while start<=end:
        mid = (start+end) // 2
        if target == store[mid] :
            return 'yes'
        elif target < arr[mid]:
            end = mid-1
        elif target > arr[mid]:
            start = mid+1
    return 'none' 

store.sort()

for i in customer:
    result = binary(store,i,0,N-1)
    if result == 'yes':
        print ('yes',end=' ')
    else :
        print('no',end=' ')
    
         
#집합 자료형 이용 
#집합 자료형 이란? 
# 중복이 없고 순서가 0-1 (내림차순)순으로 정렬되어 리스트로 만들어진다.
store_set = set(map(int,input().split()))

for i in customer:
    if i in store_set:
        print('yes')
    else:
        print('no')

