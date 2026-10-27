from random import choice as ch

GAME_ITEM = {1: "rock", 2: "scissors", 3: "paper"}
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def rounds():
    while True:
        try:
            rounds = int(input("How many rounds would you like to play?: "))
            if rounds < 1:
                raise ValueError(
                    "The number of rounds cannot be negative and must be an integer."
                )
            return rounds
        except ValueError as error:
            print(f"An error {error} has occurred! Please try again.\n")


def player_variant():
    while True:
        try:
            pl_var = int(
                input(
                    "Choose one of the following options\n1. Rock\n2. Scissors\n3. Paper\nEnter: "
                )
            )
            if pl_var < 0 or pl_var > 3:
                raise ValueError(
                    "The answer must be between 1 and 3, inclusive!"
                )
            return pl_var
        except ValueError as error:
            print(f"An error {error} has occurred! Please try again.\n")


def game(score):
    player = GAME_ITEM[player_variant()]
    computer = ch(list(GAME_ITEM.values()))
    if player == computer:
        return f"{'-' * 15}\nDraw\n{'-' * 15}"
    elif BEATS[player] == computer:
        score["player"] += 1
        return f"{'-' * 15}\nYou win round!\n{'-' * 15}"
    else:
        score["computer"] += 1
        return f"{'-' * 15}\nYou lose round :(\n{'-' * 15}"


def main():
    score = {"player": 0, "computer": 0}
    game_rd = rounds()
    for _ in range(game_rd):
        print(game(score))
    if score["player"] > score["computer"]:
        print("You WIN =)")
    elif score["player"] < score["computer"]:
        print("You lose ;(")
    else:
        print("Draw.")


if __name__ == "__main__":
    main()
