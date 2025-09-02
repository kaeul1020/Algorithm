N= int(input())

for _ in range(N):
    ps = list(input())
    stack=[]
    flag = True

    for p in ps:
        if p == "(":
            stack.append(p)
        else:
            if len(stack) == 0:
                flag = False
                break
            np = stack.pop()
            if np != "(":
                flag = False
                break
    if stack!=[]:
        flag = False
    if flag:
        print('YES')
    else:
        print("NO")
