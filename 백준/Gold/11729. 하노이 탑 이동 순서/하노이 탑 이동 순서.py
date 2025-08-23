N = int(input())

answer = []

def hanoi(cur, des, n):
    if n == 0:
        return 0
    
    n_des = 6 - cur - des
    hanoi(cur, n_des, n-1)
    answer.append(f"{cur} {des}")
    hanoi(n_des, des, n-1)
    return 0


hanoi(1,3,N)
print(len(answer))
print("\n".join(answer))