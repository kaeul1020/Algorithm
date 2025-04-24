N = int(input())
line_dot = 2

for n in range(0, N):
    line_dot += line_dot-1

print(line_dot*line_dot)


