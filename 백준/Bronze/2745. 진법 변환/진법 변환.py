N, B = input().split()
B = int(B)

result = 0

dict = {}

for alphabet in range(ord('A'),ord('Z')+1):
    dict[chr(alphabet)] = alphabet - 55

for i in range(len(N)):

    if N[len(N)-i-1] in dict.keys():
        n = dict[N[len(N)-i-1]]
    else:
        n = int(N[len(N)-i-1])

    result += n*(B**i)

print(result)