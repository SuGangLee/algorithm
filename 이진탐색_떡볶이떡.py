n ,m= map(int,input().split())

arr = list(map(int,input().split())) 

arr.sort()

start=0
end = max(arr)
total = 0
while start<=end:
    mid = (start + end)//2
    print("mid:",mid)
    for i in arr:
        if i < mid:
            continue
        else:
            total += i % mid 
    print("total:",total)
    
    if total < m :
        end= mid-1
    elif total >= m:
        result = mid  #떡 양 충분할 시 , 딱m충족이 아닌 적어도m 
        start = mid+1 
    total=0
    
  
print(result)