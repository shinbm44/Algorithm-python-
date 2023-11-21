import sys
input = sys.stdin.readline

N = int(input())

mapList = [list(map(int, input().strip())) for _ in range(N)]


dx = [0,1,-1,0]
dy = [1,0,0,-1]

result = []


def bfs(y, x):
    eachCount = 1
    q = [(y,x)]
    while q:
        ey,ex = q.pop()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if mapList[ny][nx] ==1:
                    mapList[ny][nx] = 0
                    eachCount += 1
                    q.append((ny,nx))
    return eachCount    


for j in range(N):
    for i in range(N):
        if mapList[j][i] == 1:
            mapList[j][i] = 0
            result.append(bfs(j,i))
            

result.sort()
print(len(result))
for i in range(1, len(result)):
    print(result[i])

