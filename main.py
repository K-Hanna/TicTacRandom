import random    
square = [[0,0,0],[0,0,0],[0,0,0]]

def printSquare(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print(str(a[i][j]), end=' ')
        print()
        
def add(x,y,z):
    if square[x][y] == 0:
        square[x][y] = z
        printSquare(square)
        print()
        return 1
    else:
        return 0
       
def check(a,z):
    if a[0][0] == z and a[1][1] == z and a[2][2] == z:
            print('Player ' + str(z) + ' won.')
            return 9
    elif a[0][0] == z and a[0][1] == z and a[0][2] == z:
            print('Player ' + str(z) + ' won.')
            return 9
    elif a[0][0] == z and a[1][0] == z and a[2][0] == z:
            print('Player ' + str(z) + ' won.')
            return 9
    elif a[1][1] == z and a[0][1] == z and a[2][1] == z:
            print('Player ' + str(z) + ' won.')
            return 9
    elif a[1][1] == z and a[1][0] == z and a[1][2] == z:
            print('Player ' + str(z) + ' won.')
            return 9
    elif a[1][1] == z and a[0][2] == z and a[2][0] == z:
            print('Player ' + str(z) + ' won.')
            return 9
    elif a[2][2] == z and a[2][0] == z and a[2][1] == z:
            print('Player ' + str(z) + ' won.')
            return 9
    elif a[2][2] == z and a[0][2] == z and a[1][2] == z:
            print('Player ' + str(z) + ' won.')
            return 9
    else:
        return 0

counter = 0
while counter < 9:
    if counter % 2 == 0:
        x = random.randint(0,2)
        y = random.randint(0,2)
        counter = counter + add(x,y,1) + check(square,1)
    else:
        x = random.randint(0,2)
        y = random.randint(0,2)
        counter = counter + add(x,y,2) + check(square,2)

