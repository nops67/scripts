# Solution for Project: Math and BODMAS
# From ebook "Learn Python in One Day and Learn It Well" by Jamie Chan

from random import randint
from os import remove, rename

def getUserScore(userName):
    try:
        scores = open('userScores.txt', 'r')
        for line in scores:
            content = line.split(',')
            if content[0] == userName:
                scores.close()
                return content[1]
        scores.close()
        return "-1"
    except IOError:
        print("\nFile userScores.txt not found. A new file will be created")
        scores = open('userScores.txt', 'w')
        scores.close()
        return "-1"

def updateUserPoints(newUser, userName, score):
    if newUser:
        scores = open('userScores.txt', 'a')
        scores.write(userName + ', ' + score + '\n')
        scores.close()
    else:
        scores = open('userScores.txt', 'r')
        temp = open('userScores.tmp', 'w')
    for line in scores:
        content = line.split(',')
        if content[0] == userName:
            content[1] = score
            line = content[0] + ', ' + content[1] + '\n'
        temp.write(line)
    scores.close()
    temp.close()
    remove('userScores.txt')
    rename('userScores.tmp', 'userScores.txt')

def generateQuestion():
    operandList = [0, 0, 0, 0]
    operatorList = ['', '', '']
    operatorDict = {1:'+', 2:'-', 3:'*'}
    
    for i in range(4):
        operandList[i] = randint(1, 9)
        
    for i in range(3):
        operatorList[i] = operatorDict[randint(1, 3)]
            
    questionString = str(operandList[0])

    for i in range(1, 4):
        questionString = questionString + operatorList[i-1] + str(operandList[i])

    result = eval(questionString)
        
    print("\nHow much is " + questionString + " ?")
    userInput = input("Answer: ")

    while True:
        try:
            if int(userInput) == result:
                print("\nCorrect!")
                return 1
            else:
                print("\nIncorrect!\nThe correct answer is", result)
                return -1
        except Exception as e:
                print("You did not enter a number. Please try again.")
                userInput = input("Answer: ")

try:
    userName = input("Username: ")
    userScore = int(getUserScore(userName))
    
    if userScore == -1:
        newUser = True
        userScore = 0
        print("\nWelcome to the game,", userName)
    else:
        newUser = False
        print("\nCurrent Score =", userScore)

    userChoice = 0 

    while userChoice != 'q':
        userScore += generateQuestion()
        print("\nCurrent Score =", userScore)
        userChoice = input("Press any key to continue or q to quit: ")

    updateUserPoints(newUser, userName, str(userScore))

except Exception as e:
    print("An error as occured and the program will exit.")
