import re

s = input()

numbers = list(map(int,re.sub(r'[^0-9]','',s)))
s=re.sub(r'[0-9]','',s)

sorted(s)
print(s+str((sum(numbers))))