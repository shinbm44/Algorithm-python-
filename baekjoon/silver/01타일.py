import sys
input = sys.stdin.readline 

num = int(input())

dp = [0] * 1000001

dp[1] = 1
dp[2] = 2 

for i in range(3, num+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[num])
## 프린트





