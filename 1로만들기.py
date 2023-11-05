import sys
input = sys.stdin.readline

inputNumber = int(input())

li = [0] * (inputNumber + 1)


for i in range(2, inputNumber+1):
    li[i] = li[i-1] + 1
    if i % 3 == 0:
        li[i] = min(li[i], li[i // 3] + 1)
    if i % 2 == 0:
        li[i] = min(li[i], li[i // 2] + 1)
print(li[inputNumber])
