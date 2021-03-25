import findUnknownNumbers as fun
import findColonsSutunsSquare as fcss
def findPossibility(game):
    unknownNumbers=fun.findUnknowNumbers(game)
    squares=fcss.findSquares(game)
    squaresid=[]
    possibilityes=[]
    for i in range(len(unknownNumbers)):
        x=fcss.findSquare(fcss.findColonsandSutun(unknownNumbers[i][0],unknownNumbers[i][1])[0],fcss.findColonsandSutun(unknownNumbers[i][0],unknownNumbers[i][1])[1])
        squaresid.append(x)

    j=0
    while j<len(squaresid):
        possibilityes.append([0])
        araf = []
        for l in range(1,10):
            if l in fcss.getSquare(squaresid[j],squares):
                continue

            elif l in game[unknownNumbers[j][0]]:
                continue

            elif l in fcss.findSutuns(game)[unknownNumbers[j][1]]:
                continue
            else:
                araf.append(l)
                possibilityes[j]=araf


        j = j + 1


    return possibilityes