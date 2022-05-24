# lambda 매개변수 : 표현식 을 이용하여 sort 정렬 기준 ( 키) 설정하기

from array import array


n= int(input())

arr = []
for i in range(n):
    data = input().split()
    arr.append( (data[0], int(data[1]) ) )

arr = sorted(arr, key = lambda student:student[1]) #arr의 (name,score) 중에서 score 기준으로 정렬

for student in arr:
    print(student[0],end=' ')
