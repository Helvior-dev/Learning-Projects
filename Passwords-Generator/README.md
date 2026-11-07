# Password Generator

An interactive Python CLI that generates passwords from selected character types.

## Features

- Choose digits, uppercase letters, lowercase letters, and punctuation.
- Include at least one character from every selected type in each password.
- Generate multiple passwords and print them to the terminal or save them to a file.
- Uses Python's `secrets.choice` to select password characters.

## Requirements

- Python 3.6 or newer
- No third-party packages

## Usage

Run the script and follow the prompts. The prompts are in Russian.

```bash
python password_generator.py
```

The script asks how many passwords to generate, their length, which character types to include, and whether to print or save the results. A password must be at least as long as the number of selected character types.

When saving to a file, output is written to `passwords.txt` in the current working directory. Choose `new` to overwrite the file or `old` to append to it.

## Security note

Characters are selected with `secrets.choice`, but their final order is shuffled with `random.shuffle`. Because of this, the generator should not be treated as fully cryptographically secure.
