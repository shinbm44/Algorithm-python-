import sys
input = sys.stdin.readline

inputNumber = int(input())

li = [0 for i in range(1001)]

li[0] = 0
li[1] = 1 
li[2] = 2

for i in range(3, 1001):
    li[i] = li[i-1] + li[i-2]

print(li[inputNumber])
