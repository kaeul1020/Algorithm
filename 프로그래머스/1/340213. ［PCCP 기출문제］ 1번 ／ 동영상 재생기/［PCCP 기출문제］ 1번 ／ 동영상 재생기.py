def str2time(i):
    return int(i[:2])*60 + int(i[3:])

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len, pos, op_start, op_end = str2time(video_len), str2time(pos), str2time(op_start), str2time(op_end)
    
    if op_start <= pos < op_end:
            pos = op_end
    
    for command in commands:
        if command == "next":
            pos = min(pos+10, video_len)
        if command == "prev":
            pos = max(pos-10, 0)
        if op_start <= pos < op_end:
            pos = op_end
            
    return f"{'{0:02d}'.format(pos//60)}:{'{0:02d}'.format(pos%60)}"
        
                                                                                                             
    print([video_len, pos, op_start, op_end])
    return answer