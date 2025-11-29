from collections import Counter

N = int(input())
A = list(input().split())
M = int(input())
M_list = list(input().split())

N_list = Counter()

for i in A:
    N_list[i] = 1
    
for m in M_list:
    print(N_list[m])