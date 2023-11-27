import sys
import math
input = sys.stdin.readline

Game, win =map(int, input().split())

winRatio = math.trunc((win/Game)*100)

left = 0
right = Game
result = Game

if winRatio >=99:
    print(-1)

else:
    while(left<=right):
        mid = (left +  right) // 2
        if (math.trunc((win+mid)/(Game+mid) * 100)) > winRatio:
            result = mid
            right = mid - 1
        else:
            left = mid + 1 
    print(result)