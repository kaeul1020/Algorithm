T = int(input())

for _ in range(T):
    p = list(input())
    n = int(input())
    xs = input()[1:-1].split(",", -1)
    if xs == ['']:
        xs = []
    
    error = False
    flag_front, start, end = True, 0, len(xs)
    
    for cmd in p:
        if cmd == "R":
            flag_front = not(flag_front)
            continue
        if start == end:
            error = True
            break
        if flag_front:
            start += 1
        else :
            end -= 1
            
    if error:
        print("error")
    else:
        if flag_front:
            xs = xs[start:end]
        else:
            xs = xs[start:end][::-1]
        
        print('[', end="")
        for i, x in enumerate(xs):
            if len(xs)-1 != i:
                print(f"{x},", end="")
            else:
                print(f"{x}", end="")
        print("]")