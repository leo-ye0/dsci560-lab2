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