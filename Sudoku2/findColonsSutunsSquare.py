import arayFuncs as af
def findSutuns(game):
    colon1 = []
    colon2 = []
    colon3 = []
    colon4 = []
    colon5 = []
    colon6 = []
    colon7 = []
    colon8 = []
    colon9 = []
    for i in range(0,9):
        colon1.append(game[i][0])
        colon2.append(game[i][1])
        colon3.append(game[i][2])
        colon4.append(game[i][3])
        colon5.append(game[i][4])
        colon6.append(game[i][5])
        colon7.append(game[i][6])
        colon8.append(game[i][7])
        colon9.append(game[i][8])
        colons=[colon1,colon2,colon3,colon4,colon5,colon6,colon7,colon8,colon9]
    return colons

def findSquares(game):
    square1_1=[]
    square1_2=[]
    square1_3=[]
    square2_1=[]
    square2_2=[]
    square2_3=[]
    square3_1=[]
    square3_2=[]
    square3_3=[]
    for i in range(3):
        square1_1.append(game[0+i][0:3])
        square1_2.append(game[0+i][3:6])
        square1_3.append(game[0+i][6:9])

        square2_1.append(game[3+i][0:3])
        square2_2.append(game[3 + i][3:6])
        square2_3.append(game[3 + i][6:9])

        square3_1.append(game[6 + i][0:3])
        square3_2.append(game[6 + i][3:6])
        square3_3.append(game[6 + i][6:9])
    square1_1=af.combineAray(square1_1)
    square1_2 = af.combineAray(square1_2)
    square1_3 = af.combineAray(square1_3)
    square2_1 = af.combineAray(square2_1)
    square2_2 = af.combineAray(square2_2)
    square2_3 = af.combineAray(square2_3)
    square3_1 = af.combineAray(square3_1)
    square3_2 = af.combineAray(square3_2)
    square3_3 = af.combineAray(square3_3)

    squares=[square1_1, square1_2, square1_3, square2_1, square2_2, square2_3, square3_1, square3_2, square3_3]


    return squares

def findColonsandSutun(x,y):
    colon=x+1
    sutun=y+1
    return colon,sutun

def findSquare(x,y):
    if x<=3 and y<=3:
        reuslt=1.1
    elif x<=6 and y<=3:
        reuslt = 1.2
    elif x<=9 and y<=3:
        reuslt = 1.3
    elif x<=3 and y<=6:
        reuslt = 2.1
    elif x<=6 and y<=6:
        reuslt = 2.2
    elif x<=9 and y<=6:
        reuslt = 2.3
    elif x<=3 and y<=9:
        reuslt = 3.1
    elif x<=6 and y<=9:
        reuslt = 3.2
    elif x<=9 and y<=9:
        reuslt = 3.3
    return reuslt

def getSquare(x,squares):
    reuslt2=0
    if x==1.1:
        reuslt2=squares[0]

    elif x==1.2:
        reuslt2=squares[1]

    elif x==1.3:
        reuslt2=squares[2]

    elif x==2.1:
        reuslt2=squares[3]

    elif x==2.2:
        reuslt2=squares[4]

    elif x==2.3:
        reuslt2=squares[5]

    elif x==3.1:
        reuslt2=squares[6]

    elif x==3.2:
        reuslt2=squares[7]

    elif x==3.3:
        reuslt2=squares[8]

    return reuslt2