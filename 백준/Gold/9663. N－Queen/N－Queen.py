N = int(input())

# | 방향 x
isused1= [True for _ in range(N)]

# / 방향 대각선 : x+y
isused2= [True for _ in range(N*2-1)]

# \ 방향 대각선 : x-y+n-1
isused3=[True for _ in range(N*2-1)]


def check(cur, cnt):
    if cur == N:
        return cnt+1
    for x in range(N):
        if not(isused1[x] and isused2[x+cur] and isused3[x-cur+N-1]):
            continue
        isused1[x] = False
        isused2[x+cur] = False
        isused3[x-cur+N-1] = False
        
        cnt = check(cur+1, cnt)
        
        isused1[x] = True
        isused2[x+cur] = True
        isused3[x-cur+N-1] = True
    return cnt


print(check(0, 0))