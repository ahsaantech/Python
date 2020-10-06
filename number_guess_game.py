number_of_guesses=1
print("Number of guesses is limited to only 9 time:")
while(number_of_guesses<=9):
    guess_of_number=int(input("Guess the number "))
    if guess_of_number<20:
        print("Your enter less number please input greater numbere ")
    elif guess_of_number>20:
        print("You enter greater number please input small number ")
    else:
        print("You win \n")
        print(number_of_guesses,"no of guess he took to finish")
        break
    print(9-number_of_guesses,"no. of guess left\n")
    number_of_guesses=number_of_guesses+1

if number_of_guesses>9:
    print("Game Over")
