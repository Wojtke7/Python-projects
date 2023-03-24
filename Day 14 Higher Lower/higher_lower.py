import os 
import random
from game_data import data
from art import logo,vs


data1 = data

def showScore(score):
    if score == 0:
        return
    else:
        print("Your right! Current score:" , score)


def printObject(string, object1):
    print("Compare", string, ": ", end='') 
    print(object1['name'], object1['description'], object1['country'], sep=', ')


def drawA(data1):
    A = random.choice(data1)
    return A

def drawEnemy(data1):
    enemy = random.choice(data1)    
    return enemy

def game():
    CORRECT = True
    A = drawA(data1)
    enemy = drawEnemy(data1)
    score = 0
    while CORRECT:
        print(logo)
        showScore(score)
        printObject('A',A)
        print(vs)
        printObject('B', enemy)

        choose = input("Who has more followers? Type 'A' or 'B': ")

        while True:    
            if choose == 'A':
                if A['follower_count'] > enemy['follower_count']:
                    score += 1
                    enemy = drawEnemy(data1)
                    break
                else:
                    os.system('cls')
                    CORRECT = False
                    print(logo)
                    print("Sorry that's wrong Final score: ", score)
                    input("Press enter to close")
                    break
            elif choose == 'B':
                if enemy['follower_count'] > A['follower_count']:
                    score += 1
                    A = enemy
                    enemy = drawEnemy(data1)
                    break
                else:
                    os.system('cls')
                    print(logo)
                    print("Sorry that's wrong Final score: ", score)
                    input("Press enter to close")
                    CORRECT = False
                    break
            else:
                choose = input("You type something wrong, try again: ")
        os.system('cls')         

                    
game()









    



