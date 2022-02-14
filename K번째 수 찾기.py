def solution(array, commands):
    slice = []
    answer =[]
    for i in range (0,len(commands)):
            slice = array[commands[i][0]-1:commands[i][1] ]
            slice.sort()
            print(slice[commands[i][2]-1])
            answer.append(slice[commands[i][2]-1])
            
    return answer
array = [1,2,3,4,5,6,7]
command = [[2,5,3],[4,4,1],[1,7,3]]

solution(array,command)


def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))