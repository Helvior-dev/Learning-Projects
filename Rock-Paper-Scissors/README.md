# Rock-Paper-Scissors

A command-line game of Rock, Paper, Scissors against the computer.

## Features

- Choose how many rounds to play.
- Select rock, scissors, or paper in each round.
- The computer makes a random choice.
- See each round's result and the final match result.

## Rules

- Rock beats scissors.
- Scissors beats paper.
- Paper beats rock.
- A draw does not award a point to either side.

## Requirements

- Python 3.6 or newer
- Standard library only; no third-party packages

## Usage

Run the script, enter a round count of at least 1, then choose an option each round:

```bash
python rock-paper-scissors.py
```

Options are `1` for rock, `2` for scissors, and `3` for paper. The final result is based on the number of rounds won by the player and the computer.

## Project structure

```text
rock-paper-scissors.py    # Game rules, input handling, and round loop
```
