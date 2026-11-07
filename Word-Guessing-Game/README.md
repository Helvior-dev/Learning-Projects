# Word-Guessing-Game

A console-based, Hangman-style word guessing game with category selection and a ten-point mistake limit.

## Features

- Choose from Animals, Countries, Things, or Plants.
- A random word is selected from the chosen category.
- Correct guesses reveal every matching position in the word.
- Each incorrect guess costs one point. The game ends after ten incorrect guesses.
- A special message is shown for a win with no incorrect guesses.

## Requirements

- Python 3.6 or newer
- Standard library only; no third-party packages

## Usage

Run the script and follow the English-language prompts:

```bash
python word-guessing-game.py
```

Enter lowercase letters. Guesses are compared as entered, so uppercase letters are not converted automatically. Previously revealed letters do not cost a point, but incorrect guesses are not remembered and can cost a point again if repeated.

## Project structure

```text
word-guessing-game.py    # Categories, game logic, and command-line loop
```

## What I practiced

- Using `enumerate()` to reveal multiple matching positions.
- Tracking game progress with a mutable list of characters.
- Passing updated state between functions.
- Defining a named constant for the maximum number of attempts.
- Organizing word lists by category in a dictionary of tuples.
