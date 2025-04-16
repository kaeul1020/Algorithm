num1, num2 = map(int, input().split(' '))

for i in range(min(num1, num2), 0, -1):
    if num1%i == 0 and num2%i ==0:
        print(i)
        break

for i in range(max(num1, num2), num1*num2+1, max(num1, num2)):
    if i%num1 == 0 and i%num2 == 0:
        print(i)
        break
