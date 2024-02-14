def solution(record):
    dic_id_to_name = {}
    messages= []
    for re in record:
        string = re.split(" ")
        if string[0] == "Enter":
            dic_id_to_name[string[1]] = string[2]
            messages.append((string[0],string[1]))
        elif string[0] == "Leave":
            messages.append((string[0], string[1]))
        elif string[0] == "Change":
            dic_id_to_name[string[1]] = string[2]
    real_messages =[]
    for a,b in messages:
        if a == "Enter":
            real_messages.append(dic_id_to_name[b] + "님이 들어왔습니다.")
        else:
            real_messages.append(dic_id_to_name[b] + "님이 나갔습니다.")
    return real_messages

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))