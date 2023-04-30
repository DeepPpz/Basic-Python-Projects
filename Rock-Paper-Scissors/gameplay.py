def play_game(stats):
    import time
    import random
    import custom_functions as func

    while True:
        func.letter_by_letter("Choose: Rock, Paper or Scissors:")
        player_move = input("[r/p/s] ")

        if player_move == "r":
            player_move = "Rock"
        elif player_move == "p":
            player_move = "Paper"
        elif player_move == "s":
            player_move = "Scissors"
        else:
            print("Invalid input. Try again...")
            time.sleep(3)
            continue
        break

    func.letter_by_letter("Now wait for the computer to choose...")
    time.sleep(3)

    computer_move = ""
    computer_random = random.randint(1, 3)
    if computer_random == 1:
        computer_move = "Rock"
    elif computer_random == 2:
        computer_move = "Paper"
    elif computer_random == 3:
        computer_move = "Scissors"

    func.letter_by_letter(f"The computer chose {computer_move}!")

    rock, paper, scissors = "Rock", "Paper", "Scissors"
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        stats["wins"] += 1
        result = player_move + " beats " + computer_move + ": You win!"
    elif player_move == computer_move:
        stats["draws"] += 1
        result = "It's a draw!"
    else:
        stats["loses"] += 1
        result = computer_move + " beats " + player_move + ": You lose!"

    func.letter_by_letter(result)
