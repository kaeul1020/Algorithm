import itertools
import sys

N = int(sys.stdin.readline())
As = list(map(int, sys.stdin.readline().split(' ')))

# operations : +, -, x, /
operations = []

for op, num in zip(['+', '-', 'x', '/'], list(map(int, sys.stdin.readline().split(' ')))):
    for _ in range(num) :
        operations.append(op)

permutations = list(set(itertools.permutations(operations, len(operations))))

result_min, result_max = 10000000000, -10000000000
for j, ps in enumerate(permutations):
    result = As[0]
    for i in range(len(ps)):
        if ps[i] == "+":
            result += As[i+1]
        elif ps[i] == "-":
            result -= As[i+1]
        elif ps[i] == "x":
            result *= As[i+1]
        elif ps[i] == "/":
            result = int(result / As[i+1])
    if result_min > result :
        result_min = result
    if result_max < result:
        result_max = result

print(result_max)
print(result_min)