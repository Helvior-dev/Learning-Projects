# Number-Guessing-Game

A console game where you guess a randomly chosen number and receive distance-based hints. The game also keeps a win count for each player.

## Features

- Choose an upper bound from 15 to 100; the secret number is selected from 1 to that bound.
- Get a hint after each incorrect guess: `Far away`, `Not very close`, or `Almost`.
- See the number of attempts after a correct guess.
- Play another round without restarting the program.
- View player win totals saved between sessions.

## Requirements

- Python 3.12 or newer
- Standard library only; no third-party packages

## Usage

Run the script and follow the prompts:

```bash
python number-guessing-game.py
```

Choose whether to view saved stats or start playing. During a game, enter guesses from 0 to the selected upper bound. After a win, choose whether to play another round.

## Statistics

Win totals are stored in `stats.json` in the current working directory. The file is created or updated after a win. Records are grouped by player name, for example:

```json
{
  "Player_Name": {
    "wins": 3
  }
}
```

## Project structure

```text
number-guessing-game.py    # Game logic, menu, and stats handling
stats.json                 # Persistent player win totals
```
