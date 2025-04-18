word = input()

result = 1
for i in range(len(word)//2):
    if word[i] != word[len(word)-i-1]:
        result = 0
        break
print(result)