import sys
input = sys.stdin.readline

firstNumber = int(input())
firstList = list(map(int, input().split()))

secondNumber = int(input())
secondList = list(map(int, input().split()))

firstList.sort()
def binary_search(search, start, end):
    if start > end :
        return False

    mid = (start + end) // 2
    if search < firstList[mid]:
        return    binary_search(search, start, mid)
    
    elif firstList[mid] < search:
        return    binary_search(search, mid, end)

    else:
        return True
    
for i in secondList:
    if binary_search(i, 0, firstNumber-1):
        print(1)
    else:
        print(0)


