# Creating Rock, Paper, and Scissors
import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Enter you choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    #get the users input

    choice=int(input("Enter your choice :"))
    

    while choice > 3 or choice <1:
        choice=int(input('Enter a valid choice please'))

    #connecting the value with the choice
    if choice == 1:
        choice_name= 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('User choice is \n',choice_name)
    print('Now its Computers Turn. . . .')

    #Computer is going to choose a random number from 1-3
    comp_choice = random.randint(1,3)

    # looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    #initialize value of comp_choice_name
    # making corresponding variable with the choice value
    if comp_choice == 1:
        comp_choice_name = 'rocK'
    elif comp_choice == 2:
        comp_choice_name = 'papeR'
    else:
        comp_choice_name = 'scissoR'
    print("Computer choice is \n", comp_choice_name)
    print(choice_name,'Vs',comp_choice_name)
    # Check for a draw
    if choice == comp_choice:
        print('Its a Draw', end="")
        result="Draw"
    # condition for winning
    if (choice==1 and comp_choice==2):
        print('paper wins =>',end="")
        result='papeR'
    elif (choice==2 and comp_choice==1):
        print('paper wins =>',end="")
        result='Paper'

    if (choice==1 and comp_choice==3):
        print('Rock wins =>\n',end= "")
        result='Rock'
    elif (choice==3 and comp_choice==1):
        print('Rock Wins =>\n',end= "")
        result="rocK"
    
    if (choice==2 and comp_choice==3):
        print('Scissors wins =>',end="")
        result='scissoR'
    elif (choice==3 and comp_choice==2):
        print('Scissors wins =>',end="")
        result='Rock'
     # Printing either user or computer wins or draw
    if result == "Draw":
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again (Y/N)")
    # if the user n or N then condition is True
    ans = input().lower
    if ans =='n':
        break

print("Thank you for playing!")