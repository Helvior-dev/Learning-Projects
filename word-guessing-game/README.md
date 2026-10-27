# Word Guessing Game

A console-based word guessing game (Hangman-style) with category selection and a points-based attempt limit.

## Features

- Choose a category: Animals, Countries, Things, or Plants
- A random word is picked from the chosen category
- Guess the word letter by letter, with progress shown as underscores (`_ _ a _ _`)
- Already-guessed letters are rejected without costing a point
- Wrong letters cost one point; the game ends when points run out
- Special "Flawless victory" message if you win without losing a single point
- Full input validation with retry on invalid input

## How to run

```bash
python main.py
```

Requires Python 3.10+, standard library only — no dependencies.

## How it works

1. Choose a category.
2. A word from that category is picked at random and hidden behind underscores.
3. Guess one letter at a time.
4. Correct letters reveal every matching position in the word.
5. Wrong letters cost one of your 10 points.
6. Win by revealing the whole word before running out of points.

## Example

```
Select the category you want to use to guess the word. Available categories: Animals, Countries, Things, Plants: countries
Enter a letter: a
_ a _ a _ a
Enter a letter: c
c a _ a _ a
...
You WIN!
```

## Project structure

```
main.py    # categories, word logic, letter-guessing loop
```

## What I practiced

- Using `enumerate()` to find and update multiple matching positions in a word
- Representing mutable progress as a list of characters instead of a string
- Passing and reassigning multiple mutable/immutable values between functions (`word, cnt = letter(...)`)
- Avoiding magic numbers by extracting a named constant (`MAX_ATTEMPTS`)
- Organizing word data by category in a dictionary of tuples