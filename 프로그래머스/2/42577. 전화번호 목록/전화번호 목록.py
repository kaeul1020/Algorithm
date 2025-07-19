def solution(phone_book):
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        cur_p, nxt_p = phone_book[i], phone_book[i+1]
        if len(cur_p) < len(nxt_p) and cur_p == nxt_p[:len(cur_p)]:
            return False
        
    return True