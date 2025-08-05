from collections import deque

def solution(progresses, speeds):
    answer = []
    
    q = deque([])
    for p, s in zip(progresses, speeds):
        if (100-p)%s == 0 :
            q.append((100-p)//s)
        else :
            q.append((100-p)//s +1 )
    
    print(q)
    
    while q :
        cur = q.popleft()
        
        cnt = 1
        for _ in range(len(q)):
            nxt = q[0]
            
            if cur < nxt :
                break
            else :
                q.popleft()
                cnt += 1
        
        answer.append(cnt)


    return answer