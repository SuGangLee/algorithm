N ,K = map(int, input().split())

circle = [ i for i in range (1,N+1)]

result = [] 
serial = K-1

while(len(circle)) :
    if serial >= len(circle) : #serial이 2이고 len이 1인 경우 발생하므로 > 필요 7 3 예제에서 
        serial = serial % len(circle)
    else : 
        result.append(str(circle.pop(serial)))
        serial += (K-1)

print("<",", ".join(result),">",sep='')
