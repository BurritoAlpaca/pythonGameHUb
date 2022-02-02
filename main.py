#random thing game

class Player():
    def __init__(self):
        self.name = input('What is your name? ')
        self.points = 100


player1 = Player()

gameList = ['Dice']

#file1 = open('GameRules.txt', 'r')

#print(file1[0])

def startGame():
    print('Welcome {0}\nWhat game would you like to play?'.format(player1.name))
    for i in range(0, len(gameList)):
        print('\n{0}: {1}'.format(i + 1, gameList[i]))

def gameSelect(gameNum):
    if gameNum = 0:
        dice()

def dice():
    print('Welcome to dice, the rules of the game are simple')
    print('\n')
startGame()