list=[]
num= int(input())

for i in range(num) :
    x,y = map(int,input().split())
    list.append([x,y])
#sort() 함수는 key 값을 기준으로 정렬되고 기본값은 오름차순
# 첫번쨰 아이템을 기준으로 오름차순으로 정렬한 후 두번쨰 아이템을 기준으로 정렬한다. 
list.sort(key = lambda x: (x[0],x[1]))

for i in range(num):
    print(list[i][0], list[i][1])
