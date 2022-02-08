
n = int(input())
num = list(map(int, input().split()))
stack=[]

for i in range(len(num)):
    for j in range(i,len(num)):
        if num[i] < num[j] :
            stack.append(num[j])
            break
        if j == len(num)-1 :
            stack.append(-1)

print(stack)