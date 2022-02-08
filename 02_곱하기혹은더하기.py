l = input() 
# l = list(map(int, input().split())) 로 할 경우, 왜 안돼??
result= int(l[0])


for i in range(len(l)):
    if result <= 1 or int(l[i]) <= 1 :
        result += int(l[i])
    else : 
        result *= int(l[i])

print(result)