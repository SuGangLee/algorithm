seven=[]
for i in range (9):
    seven.append(int(input()))
total = sum(seven)

for i in range(len(seven)-1):
    for j in range(i+1,len(seven)) : 
        if total - (seven[i]+seven[j])==100:
            num1=seven[i]
            num2=seven[j]
seven.remove(num1)
seven.remove(num2)    
  
print(seven.sort())