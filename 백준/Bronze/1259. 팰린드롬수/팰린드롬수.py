results=[]

while True:
    n  = input()
    if n == "0": 
        print(*results, sep="\n")
        break
    if n == n[::-1] :
        results.append("yes")
    else:
        results.append("no")