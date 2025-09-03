import sys

M = int(sys.stdin.readline().rstrip())

s = [False for _ in range(21)]

for _ in range(M):
    cmd_list = sys.stdin.readline().rstrip().split(" ")
    
    cmd = cmd_list[0]
    if len(cmd_list) == 2: 
        x = int(cmd_list[1])
        
    if cmd == "all":
        s = [True for _ in range(21)]
    elif cmd == "empty":
        s = [False for _ in range(21)]
    elif cmd == "add":
        s[x] = True
    elif cmd == "remove":
        s[x] = False
    elif cmd == "check":
        print(int(s[x]))
    elif cmd == "toggle" : 
        s[x] = not (s[x])
