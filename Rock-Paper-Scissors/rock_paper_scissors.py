import random
import time
import pers_func

pers_func.letter_by_letter("Hello, fella! Want to play a game? [y/n]")

while True:
    yes_no = input()

    if yes_no == "n":
        pers_func.letter_by_letter("Ooh, no :(. Till next time!")
        exit(0)
    elif yes_no == "y":
        pers_func.letter_by_letter("Alright, let's go! ^_^ ")
        time.sleep(1)
        pers_func.loading()
        break
    else:
        pers_func.letter_by_letter("Woah, I didn't quite catch that.")
        pers_func.letter_by_letter("Want to play a game? [y/n]")

rock, paper, scissors = "Rock", "Paper", "Scissors"

time.sleep(3)
pers_func.letter_by_letter("Choose [r]ock, [p]aper or [s]cissors:")
player_move = input()

if player_move == "r":
    player_move = "Rock"
elif player_move == "p":
    player_move = "Paper"
elif player_move == "s":
    player_move = "Scissors"
else:
    raise SystemExit("Invalid input. Try again...")

pers_func.letter_by_letter("Now wait for the computer to choose...")
pers_func.loading()
pers_func.loading()
time.sleep(3)
pers_func.letter_by_letter("I'm sorry, but he's a bit slow in choosing...")
pers_func.loading()
time.sleep(3)

computer_random = random.randint(1, 3)

computer_move = ""

if computer_random == 1:
    computer_move = "Rock"
elif computer_random == 2:
    computer_move = "Paper"
elif computer_random == 3:
    computer_move = "Scissors"

pers_func.letter_by_letter(f"The computer chose {computer_move}!")

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    result = "You win!"
elif player_move == computer_move:
    result = "It's a draw!"
else:
    result = "You lose!"

pers_func.letter_by_letter(result)

