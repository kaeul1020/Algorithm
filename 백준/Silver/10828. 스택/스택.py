import sys

N = int(input())

stack = []
for _ in range(N):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "size":
        print(len(stack))
    elif stack == []:
        if cmd[0] in ['pop','top']:
            print("-1")
        elif cmd[0] == "empty":
            print("1")
    else :
        if cmd[0] == "pop":
            print(stack.pop())
        elif cmd[0] == "empty":
            print("0")
        elif cmd[0] == "top":
            print(stack[-1])