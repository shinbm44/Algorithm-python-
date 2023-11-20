import sys
input = sys.stdin.readline

treeNumber, needLength = map(int, input().split())

treelist = list(map(int, input().split()))

left , right = 0, max(treelist)

while(left <= right):
    sum = 0
    mid = (left + right) // 2

    for i in treelist:
        if i > mid:
            sum += i - mid

    
    if sum >= needLength:
        left = mid + 1
        
    else:
        right = mid - 1
        
        
print(right)

