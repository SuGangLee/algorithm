#시간 복잡도: O(NlogN)

arr = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[0] # 첫번째원소
    tail = arr[1:] # 나머지 원소

    left_side = [x for x in tail if x <= pivot] #분할된 왼쪽부분
    right_side = [x for x in tail if  x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))