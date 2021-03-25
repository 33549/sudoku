def findUnknowNumbers(game):
    x=0
    unknowNumbers=[]
    while x<9:
        for i in range(9):
            if game[x][i]==0:
                unknowNumbers.append([x,i])
        x=x+1
    return unknowNumbers