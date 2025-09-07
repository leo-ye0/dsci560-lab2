# Reddit Data Scraper for Chatbot Training

A Python script to collect high-quality conversational data from Reddit's r/worldcup subreddit for AI chatbot training.

## Features

- Scrapes hot posts from r/worldcup
- Filters out bot comments automatically
- Quality control: only keeps posts with 2+ real comments
- Built-in data analysis and metrics
- Exports clean CSV data

## Setup

1. Install dependencies:
```bash
pip install praw pandas
```

2. Get Reddit API credentials at https://www.reddit.com/prefs/apps/

3. Update credentials in `scripts/data_exploration.py`:
```python
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET", 
    user_agent="your_username"
)
```

## Usage

```bash
python scripts/data_exploration.py
```

Output: `data/worldcup_data.csv` with structured conversation data

## Data Structure

- `title`: Post title
- `text`: Post content
- `score`: Upvotes
- `num_comments`: Comment count
- `top_comments`: Array of filtered comments

## Requirements

- Python 3.6+
- praw
- pandas

# CONCACAF PDF Converter for Chatbot Training

A Python script to convert PDF files of matchups into CSV files used for chatbot training. The example used for this instance will be the CONCACAF Qualification Series.

## Features
- Loads in PDF file
- Filters out PDF and convert them to text to find matchups between countries
- Converts matchups into a data frame
- Export clean CSV data

## Setup 

1. Install dependencies:
```bash
pip install pdfplumber pandas
```

2. Download PDF file

## Usage

```bash
python scripts/pdf_conversion.py
```

Output (for this example): `data/concacaf_matchups.csv` with structured conversation data

## Data Structure

- `home`: Home team
- `away`: Away team

## Requirements

- Python 3.6+
- pdfplumber
- pandas

# Kaggle FIFA World Cup Historical Data (CSV) for Chatbot Training

A Python script to download CSV files from Kaggle for training our AI chatbot.

## Features

- Reads and preprocesses all 3 official Kaggle datasets
- Cleans numerical columns
- Performs type coercion and fills in missing data
- Merges relevant information into a unified structure by year

## Setup

Install dependencies:
```bash
pip install kagglehub pandas
```
## Usage

```bash
python scripts/data_exploration_kaggle.py
```

Output: `data/WorldCups.csv`, `data/WolrdCupMatches.csv`, and `data/WolrdCupPlayers.csv` with tournament, match, and player-level data.
Also logs summary stats (e.g., top scorers, match cities) to console.

## Data Structure

1. WorldCups.csv

-`Year`: The year the tournament was held

-`Country`: Host country

-`Winner`, `Runners-Up`, `Third`, `Fourth`: Final rankings

-`GoalsScored`, `MatchesPlayed`, `Attendance`: Overall statistics

2. WorldCupMatches.csv

-`Year`, `Datetime`, `City`, `Stadium`: Match metadata

-`Home Team Name`, `Away Team Name`, `Home Team Goals`, `Away Team Goals`: Team data

-`MatchID`: Unique identifier used to link with player data

3. WorldCupPlayers.csv

-`MatchID`: Foreign key to WorldCupMatches.csv

-`Team Initials`, `Coach Name`, `Player Name`, `Position`, `Line-up`, `Shirt Number`: Basic player data

## Requirements

- Python 3.6+
- kagglehub
- pandas
