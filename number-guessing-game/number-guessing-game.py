from random import randint as rn
import json


def enter_number():
    while True:
        try:
            user_var = int(input("Enter a number between 15 and 100 (minimum 15, maximum 100): "))
            if user_var < 15 or user_var > 100:
                raise ValueError(
                    "The level must be an integer between 15 and 100."
                )
            return user_var
        except ValueError as error:
            print(f"An error occurred: {error}. Please try again.\n")


def con_game():
    while True:
        try:
            con_game = input("Would you like to start the game over? (Yes/No): ").strip().lower()
            if not isinstance(con_game, str) or con_game not in (
                "yes",
                "no",
            ):
                raise TypeError("The answer must be text.")
            return True if con_game == "yes" else False
        except TypeError as error:
            print(f"An error occurred: {error}. Please try again.\n")


def show_stats(data):
    for key, value in data.items():
        print(f"Player: {key} Wins: {value["wins"]}")
        print()


def variant():
    print("View stats: 1\nStart playing: 2")
    while True:
        try:
            variant = int(input("Choose one of the two: "))
            if not isinstance(variant, int) or variant not in (1, 2):
                raise ValueError("The number must be 1 or 2")
            return variant
        except ValueError as error:
            print(f"An error occurred: {error}. Please try again.\n")


def main():
    data = load_stats()
    while True:
        choice = variant()
        if choice == 1:
            show_stats(data)
        elif choice == 2:
            break
    user_num = enter_number()
    game_num = rn(1, user_num)
    attempt = 0
    name = input("Enter your name to record the result: ")
    data.setdefault(name, {"wins": 0})
    while True:
        try:
            vod = int(input("Enter a number: "))
            if vod > user_num or vod < 0:
                raise ValueError(
                    f"The number must be at least 0 and no greater than the number you selected, {user_num}"
                )
            attempt += 1
            if game_num == vod:
                print(f"Victory. You made it in {attempt} tries!")
                data[name]["wins"] += 1
                save_stats(data)
                if con_game():
                    user_num = enter_number()
                    game_num = rn(1, user_num)
                    attempt = 0
                else:
                    return
            elif abs(game_num - vod) > user_num * 0.5:
                print("Far away")
            elif abs(game_num - vod) > user_num * 0.2:
                print("Not very close")
            elif abs(game_num - vod) <= user_num * 0.2:
                print("Almost")
        except ValueError as error:
            print(f"An error occurred: {error}. Please try again.\n")


def load_stats():
    try:
        with open("stats.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save_stats(data):
    with open("stats.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    main()
