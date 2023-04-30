import time
import custom_functions as func
import game_types as game

func.letter_by_letter(f"Hello, fella! Want to play a game {chr(127918)} ?")

while True:
    yes_no = input("[y/n] ")

    if yes_no == "n":
        func.letter_by_letter(f"Ooh, no. {chr(129402)} Till next time!")
        exit(0)
    elif yes_no == "y":
        func.letter_by_letter(f"Alright, let's go! {chr(128512)}")
        time.sleep(1)
        func.loading()
        time.sleep(3)
        break
    else:
        func.letter_by_letter("Woah, I didn't quite catch that.")
        func.letter_by_letter(f"Want to play a game {chr(127918)} ?")

func.letter_by_letter("Do you wanna play single game or tournament?")
game_type = input("[s/t] ")
while game_type not in ["s", "t"]:
    func.letter_by_letter("No such game!\nChoose again: single game or tournament?")
    game_type = input("[s/t] ")

if game_type == "s":
    game.single_games()
elif game_type == "t":
    game.tournament()