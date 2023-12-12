import sys

input = sys.stdin.readline

case = int(input())


def check(list1, index, start, end):
    while start <= end:
        mid = (start + end)//2

        if list1[mid] == index:
            return 1
        
        elif list1[mid] > index:
            end = mid -1
        else:
            start = mid+1
    
    return 0
    

while case:
    num1 = int(input())
    list1 = list(map(int, input().split()))
    list1.sort()
    
    num2 = int(input())
    list2 = list(map(int, input().split()))
    

    for i in list2:
        print(check(list1, i, 0, num1-1))



