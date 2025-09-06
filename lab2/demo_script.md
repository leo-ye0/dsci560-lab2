# Reddit Data Scraping Demo Script

## Introduction (15 seconds)
"I'll demonstrate a Reddit data scraping script I built for collecting World Cup discussion data for chatbot training."

## The Problem (20 seconds)
"I needed quality conversational data from r/worldcup subreddit. The challenge was filtering out bot comments and getting meaningful discussions with sufficient engagement."

## Key Features (45 seconds)

### Data Collection
```python
subreddit = reddit.subreddit("worldcup")
for post in subreddit.hot(limit=100):
```
"Scrapes top 100 hot posts from r/worldcup"

### Smart Comment Filtering
```python
if hasattr(comment, 'body') and not comment.body.startswith('Hello! Thanks for your submission'):
    comments.append(comment.body)
```
"Filters out bot comments that start with generic greetings"

### Quality Control
```python
if len(comments) >= 2:
    posts_data.append(post_info)
```
"Only keeps posts with at least 2 real human comments for training quality"

## Data Analysis (30 seconds)
```python
def analyze_data_quality(df):
    print(f"Total posts: {len(df)}")
    print(f"Average score: {df['score'].mean():.2f}")
```
"Built-in analysis shows data quality metrics - post count, engagement scores, and sample titles"

## Output (10 seconds)
"Saves clean, structured data to CSV for chatbot training with posts, comments, and engagement metrics."

---
**Result**: High-quality conversational data ready for AI training