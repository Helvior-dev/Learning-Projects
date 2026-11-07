from random import choice as ch

MAX_ATTEMPTS = 10


CATEGORIES = {
    "animals": (
        "elephant",
        "giraffe",
        "dolphin",
        "penguin",
        "kangaroo",
        "octopus",
        "crocodile",
        "hedgehog",
    ),
    "countries": (
        "ukraine",
        "germany",
        "brazil",
        "canada",
        "japan",
        "portugal",
        "argentina",
        "norway",
    ),
    "things": (
        "keyboard",
        "umbrella",
        "backpack",
        "telescope",
        "notebook",
        "bicycle",
        "microwave",
        "flashlight",
    ),
    "plants": (
        "sunflower",
        "cactus",
        "bamboo",
        "lavender",
        "mushroom",
        "tulip",
        "fern",
        "willow",
    ),
}


def user_category() -> str:
    while True:
        try:
            variant = (
                input(
                    "Select the category you want to use to guess the word. Available categories: Animals, Countries, Things, Plants: "
                )
                .lower()
                .strip()
            )
            if variant not in CATEGORIES:
                raise ValueError(
                    "The option must be a string and must be selectable (Animals, Countries, Things, Plants)"
                )
            return variant
        except ValueError as error:
            print(f"An error occurred {error}, please try again")


def check_letter() -> str:
    while True:
        try:
            let = input("Enter a letter: ")
            if not isinstance(let, str) or len(let) > 1:
                raise ValueError("Enter one letter")
            return let
        except ValueError as error:
            print(f"An error occurred {error}, please try again")


def letter(word: str, secret_word: str, cnt: int) -> str:
    while True:
        let = check_letter()
        if let in word:
            print("This letter has already been guessed. Please select another one.")
        elif let in secret_word:
            for i, char in enumerate(secret_word):
                if char == let:
                    word[i] = let
            print("You guessed the letter!")
            return word, cnt
        else:
            cnt -= 1
            print(
                f"That letter isn't in the word. You've lost one point, so you have {cnt} points left!"
            )
            return word, cnt


def main():
    cnt = MAX_ATTEMPTS
    secret_word = ch(CATEGORIES[user_category()])
    word = ["_"] * len(secret_word)
    while cnt != 0:
        word, cnt = letter(word, secret_word, cnt)
        print(*word)
        if "_" not in word and cnt == MAX_ATTEMPTS:
            print("Flawless victory. You didn't spend a single point!")
            return
        elif "_" not in word:
            print("You WIN!")
            return
    print(
        f'You ran out of points — you lost.\nThe hidden word was: "{secret_word.title()}".\nBetter luck next time!'
    )


if __name__ == "__main__":
    main()
