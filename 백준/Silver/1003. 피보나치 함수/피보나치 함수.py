T = int(input())


for _ in range(T):
    N = int(input())
    n_list = [(1, 0), (0,1)]
    if N > 1 :
        for i in range(2, N+1):
            n_list.append((n_list[i-2][0]+n_list[i-1][0], 
                           n_list[i-2][1]+n_list[i-1][1]))
    print(*n_list[N])