def combineAray(aray):
    emptyAray=aray
    aray=[]
    x=0
    while x<len(emptyAray):
        for i in range(len(emptyAray[x])):
            aray.append(emptyAray[x][i])
        x=x+1

    return aray
