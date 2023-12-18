import sys 
input = sys.stdin.readline

inputNumber = int(input())
li = []
for i in range(inputNumber):
    
    inputStr = input().split()

    

    if inputStr[0] == "push_front":
        li.insert(0, int(inputStr[1]))
    
    elif inputStr[0] == "push_back":
        li.append(int(inputStr[1]))

    elif inputStr[0] == "pop_front":
        if len(li) == 0:
            print(-1)
            continue
        else:
            print(li[0])
            del(li[0])

    elif inputStr[0] == "pop_back":
        if len(li) == 0:
            print(-1)
            continue
        else:
            print(li[-1])
            del(li[-1])
    
    elif inputStr[0] == "size":
        print(len(li))
    
    elif inputStr[0] == "empty":
        if len(li) == 0:
            print(1)
        else:
            print(0)
    
    elif inputStr[0] == "front":
        if len(li) == 0:
            print(-1)
        else:
            print(li[0])
    
    elif inputStr[0] == "front":
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])
