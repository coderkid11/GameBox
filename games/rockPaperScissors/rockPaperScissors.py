def rockPaperScissors():
    import os
    import random
    import array
    import time
    from asciiArt.asciiLogo import asciiLogo
    from asciiArt.asciiLogo import slowAsciiLogo
    from asciiArt.rockPaperScissors import rockAsciiArt, paperAsciiArt, scissorsAsciiArt
    os.system('clear')

    score = array.array('u', ['0', '-', '0'])
    userScore = 0
    computerScore = 0

    def gameStart():
        nonlocal userScore
        nonlocal computerScore
        nonlocal compChoice
        nonlocal userChoice
        if userChoice == 1 and compChoice == 1:
            print('Computer chose ' + compChoiceName + '!')
            rockAsciiArt()
            print('Vs')
            rockAsciiArt()
            print("Draw")
        elif userChoice == 2 and compChoice == 1:
            print('Computer chose ' + compChoiceName + '!')
            paperAsciiArt()
            print('Vs')
            rockAsciiArt()
            print("You win!")
            userScore = userScore + 1
            score[0] = str(userScore)
        elif userChoice == 3 and compChoice == 1:
            print('Computer chose ' + compChoiceName + '!')
            scissorsAsciiArt()
            print('Vs')
            rockAsciiArt()
            print("GameBox wins!")
            computerScore = computerScore + 1
            score[2] = str(computerScore)
        elif userChoice == 1 and compChoice == 2:
            print('Computer chose ' + compChoiceName + '!')
            rockAsciiArt()
            print('Vs')
            paperAsciiArt()
            print("GameBox wins!")
            computerScore = computerScore + 1
            score[2] = str(computerScore)
        elif userChoice == 2 and compChoice == 2:
            print('Computer chose ' + compChoiceName + '!')
            paperAsciiArt()
            print('Vs')
            paperAsciiArt()
            print("Draw")
        elif userChoice == 3 and compChoice == 2:
            print('Computer chose ' + compChoiceName + '!')
            scissorsAsciiArt()
            print('Vs')
            paperAsciiArt()
            print("You Win!")
            userScore = userScore + 1
            score[0] = str(userScore)
        elif userChoice == 1 and compChoice == 3:
            print('Computer chose ' + compChoiceName + '!')
            rockAsciiArt()
            print('Vs')
            scissorsAsciiArt()
            print("You Win!")
            userScore = userScore + 1
            score[0] = str(userScore)
        elif userChoice == 2 and compChoice == 3:
            print('Computer chose ' + compChoiceName + '!')
            paperAsciiArt()
            print('Vs')
            scissorsAsciiArt()
            print("GameBox Wins!")
            computerScore = computerScore + 1
            score[2] = str(computerScore)
        elif userChoice == 3 and compChoice == 3:
            print('Computer chose ' + compChoiceName + '!')
            scissorsAsciiArt()
            print('Vs')
            scissorsAsciiArt()
            print("Draw")
        else:
            print("Error, ask admin for help.")

    slowAsciiLogo()
    print("Welcome to Rock Paper Scissors!")
    print(" ")
    print(
        "This is a completly normal game of Rock Paper Scissors, no surprises. Just enter rock, paper or scissors to get started."
    )
    print(" ")
    print("Press ENTER to continue")
    enterToContinue = input("")
    os.system('clear')

    while True:

        os.system('clear')
        asciiLogo()
        print("The score is", score[0], score[1], score[2])
        print("")
        userChoice = int(input("1.Rock 2.Paper 3.Scissors? "))

        compChoice = random.randint(1, 3)
        if compChoice == 1:
            compChoiceName = 'Rock'
        elif compChoice == 2:
            compChoiceName = 'Paper'
        elif compChoice == 3:
            compChoiceName = 'Scissors'

        gameStart()

        if input('Play again (y/n)? ') not in ('Y', 'y'):
            os.system('clear')
            asciiLogo()
            print("The final score was", score[0], score[1], score[2])
            enterToContinue = input("Press ENTER to continue")
            break
