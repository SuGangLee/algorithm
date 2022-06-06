
#다시 풀어.. 다시 ...... 틀렸어 그냥....
food_time =list(map(int,input().split()))
k = int(input())
rotation =0
#시간 초과- 우선 순위 큐 사용해~!~
while k!=0:
    if food_time[rotation] !=0:
        food_time[rotation] -=1
        rotation+=1
        if rotation == len(food_time):
            rotation=0
        k-=1
    while food_time[rotation] == 0:
        rotation+=1
        if rotation == len(food_time):
            rotation=0


print(rotation+1,'번째 음식 먹을 차례')

