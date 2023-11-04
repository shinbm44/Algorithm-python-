import sys
input = sys.stdin.readline

inputNumber = int(input())

li = [i for i in range(1, inputNumber+1)]
i = 1

while(True):
    

    if(len(li) == 1 ):
        break

    if (i % 2 != 0):
        i += 1
        del(li[0])
    else:
        i += 1
        li.append(li[0])
        del(li[0])

print(li[0])


 