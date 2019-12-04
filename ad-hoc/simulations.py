
from random import randrange, random
a = randrange(1,7)
print(a)
a = randrange(1,7)
print(a)
a = randrange(1,7)
print(a)
a = randrange(1,7)
print(a)
a = randrange(1,7)
print(a)
a = randrange(1,7)
print(a)
a = randrange(1,7)
print(a)
a = randrange(1,7)
print(a)
a = randrange(1,7)
print(a)

# Random
a = random()
print(a)
a = random()
print(a)

# Napisati program koji simulira 100 puta eksperiment bacanja kocke
# i prebrojava koliko se kocka zaustavila na odredjenom broju.
# TODO

''' Input:
    The program first prompts for and gets the service probabilities of the
    two players (called "player A" and "player B"). Then the program prompts
    for and gets the number of games to be simulated. 
'''

''' Output:
    The program will provide a series of initial prompts such as the following:
    What is the prob. player A wins a serve?
    What is the prob. player B wins a serve?
    How many games to simulate?
    The program will print out a nicely formatted report showing the number
    of games simulated and the number of wins and winning percentage for
    each player. Here is an example:
    Games Simulated: 500
    Wins for A: 268 (53.6%)
    Wins for B: 232 (46.4%)
'''

from random import random
def main():
    printIntro()
    probA, probB, n = getInputs()
    
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    # Returns the three simulation parameters
    a - float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A" :
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a == 15 or b == 15

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1: 0.1%})".format(winsB, winsB/n))

print(__name__)

if __name__ == '__main__':
    main()