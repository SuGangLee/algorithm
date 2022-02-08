N,M,K = map(int,input().split())
arr=list(map(int,input().split()))

count=0

result=0
arr.sort()

for i in range(M):
     if count < K: 
        result+=arr[-1]
        count+=1
     else:
         result+=arr[-2]
         count=0
print(result)

#반복되는 수열은 K+1 [6,6,6,5] 
#count = int(m/(k+1)) * k  
#count += m%(k+1) -> M이 나누어떨어지지 않는 경우, 나머지만큼 큰 수가 더해짐 
