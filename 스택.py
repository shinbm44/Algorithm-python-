import sys
input  = sys.stdin.readline

inputNumber = int(input())

li = []
for i in range(inputNumber):
    inputStr = input().split()
    if inputStr[0] == "push":
        number = int(inputStr[1])
        li.append(number)
        continue
    elif inputStr[0] == "top":
        if (len(li) == 0):
            print(-1)
        else:
            print(li[-1])
        continue
    elif inputStr[0] == "pop":
        if(len(li) == 0 ):
            print(-1)
        else: 
            print(li.pop())
        continue
    elif inputStr[0] == "size":
        print(len(li))
        continue
    elif inputStr[0] == "empty":
        if (len(li) == 0):
            print(1)
        else:
            print(0)
