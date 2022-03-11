import random, re
# import sys

itemsList =['rock','paper','scissor']

computerScore =0
userScore =0
numberOfdraw =0
numberOfGame =0
while(numberOfGame<5):
    computerChoice = random.choice(itemsList)
    print("Computer selected:",computerChoice)
    # game rules
    # rock beats scissor
    # scissor beats paper
    # paper beats rock

    try:
        userChoice = input("Enter your choice, [Type in lowercase or small letters] ")
        choices = ["rock","paper","scissor"]
        if userChoice.lower() not in choices:
            print("Input Error! Please enter [rock, paper or scissor] to play")
            # sys.exit() # this will terminate the program
        if userChoice == computerChoice:
            print("It's a draw. Play again")
            numberOfdraw=numberOfdraw+1

        if userChoice =='rock' and computerChoice=='scissor':
            print("You Won")
            userScore =userScore+1
        elif userChoice=='rock' and computerChoice=='paper':
            print("Computer Won")
            computerScore=computerScore+1
        if userChoice == 'scissor' and computerChoice =='paper':
            print("You Won")
            userScore =userScore+1
        elif userChoice=='scissor' and computerChoice=='rock':
            print("Computer Won")
            computerScore=computerScore+1

        if userChoice =='paper' and computerChoice =='rock':
            print('you Won')
            userScore =userScore+1
        elif userChoice =="paper" and computerChoice=="scissor":
            print("Computer Won")
            computerScore=computerScore+1

        numberOfGame=numberOfGame+1
    except KeyboardInterrupt:
        print(" KeyboardInterrupt exception is caught, Please enter correctly.")
print('\n')
print("***GAME SUMMARY***")
print("You played",numberOfGame,"times")
print("Your total Score",userScore)
print("Computer's total Score",computerScore)
print("Total draws drawn",numberOfdraw)

if userScore>computerScore:
    print("GAME OVER.You won the overall game")
elif userScore<computerScore:
    print("GAME OVER.Computer won the overall game")
else:
    print("GAME OVER. Its a draw")
