n = int(input())

mylist=[]
for i in range(n):
    x= (int(input()))
    mylist.append(x)


search = int(input())

def binary(list,search,start,end) :
    mid = (end + start) // 2
    if list[mid] > search :
        return binary (list,search,start,mid)
    elif list[mid] < search :
        return binary(list,search,mid,end)
    if list[mid] == search :
        return mid

binary(mylist,search,0,n)
