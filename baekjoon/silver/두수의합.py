import sys
input = sys.stdin.readline

num = int(input())
li = list(map(int, input().split()))
li.sort()
target = int(input())

start = 0
end = num-1
val = 0
cnt =0 
while(start < end):
    val = li[start] + li[end] 
   
    if val > target:
        end -= 1
    elif val < target:
        start += 1
    else:
        cnt+=1
        start+=1
        end-=1
print(cnt)





