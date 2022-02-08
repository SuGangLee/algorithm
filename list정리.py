list1= list("hello") # h,e,l,l,o 요소
list2= list(range(0,5)) # 0,1,2,3,4 요소
# 리스트의 인덱스는 0~ len(list)-1까지 요소를 갖는다. 
#슬라이싱 : 요소 범위 지정 , list[3:6] -> 3,4,5번째 요소 추출
# 슬라이싱으로 리스트 일부 변경 및 삭제 가능
list3 = ['a','b','c','d','e','f']
list3[1:3] = ['B','C']
list3[4:5] = [] 

# 리스트연산
# +, *(반복) , len(), append(), pop(1) : 위치를 받아와 삭제와 동시에 반환 , 
# remove('이수경'): 항목을 받아와 삭제 
#  sort() 리스트 정렬, sorted() : 정렬된 새로운 리스트 반환

#문자열에서 리스트 만들기 : split() 
string = "my name is dangom" 
string.split( ) 

#얕은 복사 
original = [1,2,3] 
low_copied = original # 같은 메모리 주소 가리킴 , 공유적 존재 

#깊은 복사 
deep_copied = list(original) # 새로운 메모리 생성, 독립적 존재

#리스트 함축 x =[ 출력식 변수의 범위 if 조건]
S= [x**2 for x in range(10)] # S=[0,1,4,9,16....] 
