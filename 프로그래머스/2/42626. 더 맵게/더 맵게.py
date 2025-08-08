from heapq import heappop, heappush, heapify

def solution(scoville, K):
    cnt = 0
    
    heapify(scoville)
    
    while len(scoville) > 1 and scoville[0] < K:
        
        f_min = heappop(scoville)
        s_min = heappop(scoville)
        
        mix = f_min + (s_min*2)
        
        
        heappush(scoville, mix)
            
        cnt += 1
        
        # print(cnt, scoville)
    
    if scoville[0] >= K :
        return cnt 
    else:
        return -1