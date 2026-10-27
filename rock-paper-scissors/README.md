# Rock Paper Scissors

A console-based Rock Paper Scissors game against the computer, with configurable round count and score tracking.

## Features

- Choose how many rounds to play
- Random computer opponent
- Round-by-round results (win / lose / draw)
- Final match result based on total score
- Full input validation with retry on invalid input

## How to run

```bash
python main.py
```

Requires Python 3.10+, standard library only — no dependencies.

## How it works

1. Enter the number of rounds you want to play.
2. Each round, pick Rock, Scissors, or Paper.
3. The computer picks randomly.
4. The round result is shown immediately (win / lose / draw).
5. After all rounds, the overall winner is announced based on total score.

## Example

```
How many rounds would you like to play?: 3
Choose one of the following options
1. Rock
2. Scissors
3. Paper
Enter: 1
---------------
You win round!
---------------
...
You WIN =)
```

## Project structure

```
main.py    # game rules, input handling, round loop
```

## What I practiced

- Representing game rules as a dictionary (`BEATS`) instead of chained if/elif
- Passing mutable state (`score`) explicitly into functions instead of relying on globals
- Separating constants (fixed game data) from state (data that changes during runtime)
- Input validation loops