def int2time(i):
    return i//100*60 + i%100

def solution(schedules, timelogs, startday):
    answer = 0
    
    holidays = [6-startday,7-startday]
    if holidays[0] < 0 : holidays[0]+=7
    if holidays[1] < 0 : holidays[1]+=7
    
    for people in range(len(schedules)):
        flag = True
        
        for j in range(len(timelogs[people])):
            
            if j in holidays:
                continue
            
            print(int2time(schedules[people])+10, int2time(timelogs[people][j]))
            if int2time(schedules[people])+10 < int2time(timelogs[people][j]):
                flag = False
                break
        if flag:
            answer+=1
    return answer