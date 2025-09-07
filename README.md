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