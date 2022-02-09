#동적프로그래밍이란 
# 1.큰 문제를 작게 나눠서 해결한다.
# 2.작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하게 사용된다. 

d = [0]*100
#1.탑다운 - 재귀적호출 ->거의 사용 x
def fibo(x):
    #종료조건
    if x==1 or x==2:
        return 1
    #이미 계산한 적 있는 문제라면 그대로 반환
    if d[x]!=0:
        return d[x]
    #계산한 적 없는 문제라면 점화식
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]

#2. 바텀업 - 반복문 사용 
d2=[]
d2[1]=1
d2[2]=1
n=99
for i in range(3,n+1):
    d2[i] = d2[i-1]+d2[i-2]