T = int(input())
N_list = [int(input()) for _ in range(T)]
for n in N_list:
    n_table = [0 for _ in range(12)]
    n_table[1] = 1
    n_table[2] = 2
    n_table[3] = 4
    for i in range(4, n+1):
        n_table[i] = sum(n_table[i-3:i])
            
    print(n_table[n])