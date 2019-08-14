import random    
square = [['.','.','.'],['.','.','.'],['.','.','.']]

def printSquare(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print(str(a[i][j]), end=' ')
        print()
        
def add(x,y,z):
    if square[x][y] == '.':
        square[x][y] = z
        printSquare(square)
        print()
        return 1
    else:
        return 0
       
def check(z):
    if square[0][0] == z and square[1][1] == z and square[2][2] == z:
            return 9
    elif square[0][0] == z and square[0][1] == z and square[0][2] == z:
            return 9
    elif square[0][0] == z and square[1][0] == z and square[2][0] == z:
            return 9
    elif square[1][1] == z and square[0][1] == z and square[2][1] == z:
            return 9
    elif square[1][1] == z and square[1][0] == z and square[1][2] == z:
            return 9
    elif square[1][1] == z and square[0][2] == z and square[2][0] == z:
            return 9
    elif square[2][2] == z and square[2][0] == z and square[2][1] == z:
            return 9
    elif square[2][2] == z and square[0][2] == z and square[1][2] == z:
            return 9
    else:
        return 0

def start(player1, player2):
    counter = 0
    while counter < 9:
        if counter % 2 == 0:
            x = random.randint(0,2)
            y = random.randint(0,2)
            counter = counter + add(x,y,player1) + check(player1)
            if check(player1) == 9:
                print('Player ' + player1 + ' won.')
                print()
        else:
            x = random.randint(0,2)
            y = random.randint(0,2)
            counter = counter + add(x,y,player2) + check(player2)
            if check(player2) == 9:
                print('Player ' + player2 + ' won.')
                print()
    if counter == 9:
        print('It is a tie.')
        print()

player1 = 'X'
player2 = 'O'
tries = 10
games = 0
playerX = 0
playerO = 0
while games < tries:
    print('Game: ' + str(games + 1) + '.')
    start(player1, player2)
    if check(player1) == 9:
        playerX += 1
    if check(player2) == 9:
        playerO += 1
    games += 1
    square = [['.','.','.'],['.','.','.'],['.','.','.']]
tie = tries - playerX - playerO

print()
print('Player ' + player1 + ' won ' + str(playerX) + ' times.')
print('Player ' + player2 + ' won ' + str(playerO) + ' times.')
print('There were ' + str(tie) + ' ties.')

