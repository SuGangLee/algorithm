result = int(input())
i=0

while (1) :
    if result - 2**i == 0:
        print(i)
        break
    if result - 2**i > 0 : 
        i+=1
    else :
        print(i-1, end=' ')
        result=result - 2**(i-1)
        i=0
    


