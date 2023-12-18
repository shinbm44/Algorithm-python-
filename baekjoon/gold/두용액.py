import sys
input = sys.stdin.readline

num = int(input())

li = list(map(int, input().split()))
li.sort()

start = 0
end = num - 1 
checkNum = abs(li[0] + li[num-1])
result_li = list()
result_li.append(li[0])
result_li.append(li[num-1])

while(start < end):
    val = li[start] + li[end]
    if abs(val) < checkNum:
        result_li[0] = li[start]
        result_li[1] = li[end]
        checkNum = abs(val)
        if val == 0:
            break

    if val < 0:
        start += 1
    else:
        end -= 1

print(result_li[0],result_li[1])



