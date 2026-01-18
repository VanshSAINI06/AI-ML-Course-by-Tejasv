import random
def play_game():
    random_number=random.randint(1,10)
    no_of_attempts=3
    for i in range(1,no_of_attempts+1):
        input_number=int(input("Guess the number between 1 and 10: "))
        if input_number==random_number:
            print("You guessed the right number!")
            break
        else:
            if(i<no_of_attempts):
                print("Wrong guess. Try again.")
            else:
                print("You lost! Right answer was", random_number)

play_game()