import findColonsSutunsSquare as fcss
import solution
import findUnknownNumbers as fun
game=[
      [0,7,0,0,0,0,0,0,9],
      [5,1,0,4,2,0,6,0,0],
      [0,8,0,3,0,0,7,0,0],
      [0,0,8,0,0,1,3,7,0],
      [0,2,3,0,8,0,0,4,0],
      [4,0,0,9,0,0,1,0,0],
      [9,6,2,8,0,0,0,3,0],
      [0,0,0,0,1,0,4,0,0],
      [7,0,0,2,0,3,0,9,6]]


#print(len(fun.findUnknowNumbers(game)))


squares = fcss.findSquares(game)

i=0
# while i in range(len(a)):
#       if i> len(a):
#             i=0
b = fun.findUnknowNumbers(game)
a = solution.findPossibility(game)
print(a)
for i in range(len(a)):
      d=True
      for l in range(len(b)):
            if len(a[i]) == 1 and len(a[l]) == 1:
                  d2=False
            if fcss.findSquare(fcss.findColonsandSutun(b[i][0],b[i][1])[0],fcss.findColonsandSutun(b[i][0],b[i][1])[1])==fcss.findSquare(fcss.findColonsandSutun(b[l][0],b[l][1])[0],fcss.findColonsandSutun(b[l][0],b[l][1])[1]):
                  for j in range(len(a[l])):
                        if a[i][0]==a[l][j]:
                              d=False
                              print("log1", a[i][0], a[l][0])
                              break

            elif fcss.findColonsandSutun(b[i][0],b[i][1])[1]==fcss.findColonsandSutun(b[l][0],b[l][1])[1]:
                  for j in range(len(a[l])):
                        if a[i][0] == a[l][j]:
                              d=False
                              print("log2", a[i][0], a[l][0])
                              break

            elif fcss.findColonsandSutun(b[i][0],b[i][1])[0]==fcss.findColonsandSutun(b[l][0],b[l][1])[0]:
                  for j in range(len(a[l])):
                        if a[i][0] == a[l][j]:
                              d=False
                              print("log3",a[i],a[l])
                              break 
      if d==False:
            print("log123")
            continue
      elif len(a[i]) == 1:
            game[b[i][0]][b[i][1]] = a[i][0]
      else:
            continue

print(game)
print("--------------------------------------------------------")