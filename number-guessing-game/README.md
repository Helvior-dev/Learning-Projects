# Number Guessing Game

A console-based number guessing game with hints, replay support, and persistent player statistics stored in JSON.

## Features

- Custom guessing range (15–100)
- Proximity hints ("Far", "Not close", "Almost") scaled to the chosen range
- Attempt counter per round
- Replay option without restarting the program
- Player stats (name + total wins) saved to `stats.json` and preserved between sessions
- Menu: view leaderboard or start playing
- Input validation with clear error messages on every prompt

## How to run

```bash
python main.py
```

Requires Python 3.10+ (uses `match`-free code, standard library only — no dependencies).

## How it works

1. On start, choose to **view stats** or **play**.
2. Enter the upper bound of the guessing range (15–100).
3. Enter your name — if you've played before, your existing record is used; otherwise a new one is created.
4. Guess the number. After each wrong guess you get a hint based on how far off you are.
5. On a correct guess, your win is recorded and you can choose to play again or exit.
6. Stats are saved to `stats.json` after every win.

## Example

```
Show stats: 1
Start playing: 2
Choose one of the two: 2
Enter the maximum number (min. 15, max. 100): 50
Enter your name to record the result: Vlad
Enter a number: 25
Not close
Enter a number: 40
Almost
Enter a number: 37
Victory. You guessed it in 3 attempts!
Do you want to start a new game?(Yes/No): no
```

## Data format (`stats.json`)

```json
{
    "Player_Name": {
        "wins": 3
    }
}
```

## Project structure

```
main.py       # game logic, menu, stats functions
stats.json    # auto-generated, stores player stats
```

## What I practiced

- Input validation with `try/except`
- Function decomposition (separating input handling, game loop, and persistence)
- Working with nested dictionaries (`setdefault`)
- Reading/writing JSON files
- Designing a replay loop without recursion