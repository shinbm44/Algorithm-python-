import sys 
input = sys.stdin.readline

inputNumber = int(input())
li = []

for i in range(inputNumber):

    inputStr = input().split()

    if inputStr[0] == "push":
        li.append(int(inputStr[1])) 
        continue
    elif inputStr[0] == "pop":
        if len(li) == 0:
            print(-1)
        else:
            print(li[0])
            del(li[0])
        continue

    elif inputStr[0] == "size":
        print(len(li))
        continue
    
    elif inputStr[0] == "empty":
        if len(li) == 0:
            print(1)
        else:
            print(0)
        continue
    
    elif inputStr[0] == "front":
        if (len(li) == 0):
            print(-1)
        else:
            print(li[0])
        continue

    elif inputStr[0] == "back":
        if (len(li) == 0):
            print(-1)
        else:
            print(li[-1])
        continue