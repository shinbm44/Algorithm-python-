
while True:
    inputStr = input()
    li=[]

    if inputStr == ".":
        break

    for i in inputStr:
        if i =='(' or i=='[':
            li.append(i)

        elif i ==')':
            if len(li) != 0 and li[-1] == '(':
                li.pop()
            else:
                li.append(i)
            break

        elif i ==']':
            if len(li) != 0 and li[-1] =='[':
                li.pop()
            else:
                li.append(i)
            break
        
    
    if len(li) == 0:
        print("yes")

    else:
        print("no")

            




