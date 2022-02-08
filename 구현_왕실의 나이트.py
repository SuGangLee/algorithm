point =list(input())
Night = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]] 

col = ['a','b','c','d','e','f','g','h']
x=col.index(point[0])+1
result = [x,int(point[1])]
count=0
for i in range (len(Night)):
    if (result[0] + Night[i][0]) > 8 or (result[0] + Night[i][0]) < 1 or (result[1] + Night[i][1]) > 8 or (result[1] + Night[i][1]) < 1:
        continue
    else :
        count+=1

print(count)