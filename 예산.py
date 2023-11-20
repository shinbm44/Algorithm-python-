import sys
input = sys.stdin.readline

number = int(input())

locations = list(map(int, input().split()))
budget = int(input())
locationsRequestSum = 0

for i in range(len(locations)):
    locationsRequestSum += locations[i] 

start = min(locations)
end = max(locations)

def CalculationBudget(start, end):
  
    if locationsRequestSum <= budget:
        return max(locations)
    
    else:
        while(start <= end):
            total = 0
            mid = (start + end) // 2
            
            for i in locations:
                if i > mid:
                    total += mid
                else:
                    total += i
            
            if total > budget:
                end = mid - 1
            else:
                start = mid + 1
    return end

print(CalculationBudget(start, end))
            
