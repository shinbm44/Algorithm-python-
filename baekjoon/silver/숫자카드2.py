import sys
input = sys.stdin.readline

numberFirst = int(input())
firstList = list(map(int, input().split()))

numberSecond = int(input())
SecondList = list(map(int, input().split()))

countDic = {}
for num in firstList:
    countDic[num] = countDic.setdefault(num, 0) + 1
    

firstList.sort()
def binary_search(val, start, end):
    if start > end:
        return 0
    
    mid = (end + start) // 2

    if val < firstList[mid]:
        return binary_search(val , start, mid-1)
    elif val > firstList[mid]:
        return binary_search(val , mid+1, end)
    elif firstList[mid] == val:
        return countDic.get(val)
    else:
        return 0

    

    
for i in SecondList:
    print(binary_search(i, 0, len(firstList)-1), end = " ")
    

