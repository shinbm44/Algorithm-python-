import sys
input = sys.stdin.readline

itemNumber, wantNumber = map(int,input().split())

data = [int(input()) for i in range(itemNumber)]

left, right = 1, max(data) 

def searchNumber(start, end):
    if start > end:
        return end
    mid = (start + end) // 2
    result = 0
    for item in data:
        result += (item // mid)

    if result >= wantNumber:
        return searchNumber(mid+1, end)
    else:
        return searchNumber(start, mid-1)
    
print(searchNumber(left, right))


