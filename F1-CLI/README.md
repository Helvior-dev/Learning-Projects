# F1-CLI

An interactive command-line tool for exploring statistics about Formula 1 drivers from the 2025 season.

## Features

- List all drivers.
- Filter drivers by team or country.
- List drivers born in or after 2000.
- Show the top 0 to 20 drivers by career points.

## Data source

At startup, the program downloads the 2025 driver data from the [formula1-datasets repository](https://github.com/toUpperCase78/formula1-datasets). An internet connection is required.

## Requirements

- Python 3.12 or newer
- The `requests` package

Install the dependency with:

```bash
python -m pip install requests
```

## Usage

Run the script and follow the Russian-language menu:

```bash
python f1.py
```

Menu options let you list drivers, filter by team or country, show drivers born in or after 2000, or display the top N by career points.
