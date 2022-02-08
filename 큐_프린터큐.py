test = int(input())
count=0

for i in range (test):
    num, index = map(int, input().split())
    q_importance = list(map(int, input().split()))
    value = list(range(len(q_importance)))
    value[index] = 'target' # 값으로만 비교하면 동일한 값이 여러 개 있을 때 안되니까 배열로 비교 >< 
    print('insert',q_importance)
    while(1): 
        if max(q_importance) == q_importance[0]:
            count+=1
            if 'target' == value[0]:
                print('result',count)
                break
            else:
                del q_importance[0]
                del value[0]
                print('max',q_importance)               
        else: 
            q_importance.append(q_importance[0])
            value.append(value[0])
            del q_importance[0]
            del value[0]
            print('not max',q_importance)
            