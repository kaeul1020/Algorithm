T = int(input())
nums= []
for _ in range(T):
    nums.append(int(input()))

for num in nums:
    num = bin(num)[2:]

    for i in range(len(num)):
        if int(num[len(num)-i-1]) == 1:
            print(i,end=' ')