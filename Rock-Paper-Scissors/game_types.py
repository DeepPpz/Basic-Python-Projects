import gameplay as gp
import custom_functions as func


def single_games():
    stats = {"wins": 0, "draws": 0, "loses": 0}
    count_games = 0

    while True:
        count_games += 1
        gp.play_game(stats)

        func.letter_by_letter("Do you wanna play another game?")
        yes_no = input("[y/n] ")

        if yes_no == "y":
            continue
        else:
            break

    func.letter_by_letter("Stats from all games:")
    for key, value in stats.items():
        func.letter_by_letter(f"* {key} - {value}")


def tournament():
    func.letter_by_letter(f"OK! Now the computer is pumped up! {chr(128170)}")
    func.letter_by_letter("How many games do you want to play?")
    while True:
        try:
            games = int(input())
            break
        except ValueError:
            func.letter_by_letter("You have to give me a number! Let's try again!")

    stats = {"wins": 0, "draws": 0, "loses": 0}

    for i in range(games):
        gp.play_game(stats)

    func.letter_by_letter("The tournament is over! \nHere are the stats:")
    for key, value in stats.items():
        func.letter_by_letter(f"* {key} - {value}")

    if stats["draws"] > (games / 2):
        result = "Too many draws!\nThe tournament is a tie! " + chr(129309)
    elif stats["wins"] > stats["loses"]:
        result = "You win the tournament! " + chr(127942)
    elif stats["loses"] > stats["wins"]:
        result = "You lost the tournament! " + chr(128555)
    else:
        result = "The tournament is a tie! " + chr(129309)

    func.letter_by_letter(result)
