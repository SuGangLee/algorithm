
#딕셔너리 쓰자 씨발
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
answer = []
command = [ list(record[i].split()) for i in range(len(record)-1)]
dic = {}
        
for i in range(len(record)-1):
    if command[i][0] == "Enter":
        continue
    if command[i][0] == "Leave":
        continue
    if command[i][0] == "Change":
        for j in range(len(command)-1):
            if command[j][1] == command[i][1]:
                    command[j][2] = command[i][2]

print(command) 
for i in range(len(command)):
    dic = {command[i][1]:command[i][2]}

for i in range(len(command)):  
        if command[i][0] == "Enter":
            dic.values
        if command[i][0] == "Leave":
            command[i]
            answer.append(command[i][2]+"님이 나갔습니다.")
print(answer)