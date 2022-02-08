
tower=[]

def hanoi (n,start,end) :
    if n==1 : 
        tower.append([start,end])
        return
    hanoi(n-1,start,6-start-end) #1단계
    tower.append([start,end]) #2단계 
    hanoi(n-1,6-start-end,end)#3단계 

n=int(input())

hanoi(n,1,3)

print(len(tower)) #횟수 출력

for x,y in tower : #2차원 리스트 요소출력 
    print (x,y)

