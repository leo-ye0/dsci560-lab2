import praw
import pandas as pd
from datetime import datetime

# Reddit API setup (Register at https://www.reddit.com/prefs/apps/)
# Replace with your credentials
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET", 
    user_agent="reddit_username"
)

def scrape_worldcup_data(limit=100):
    """Scrape posts and comments from r/worldcup for chatbot training data"""
    
    subreddit = reddit.subreddit("worldcup")
    posts_data = []
    
    # Get hot posts
    for post in subreddit.hot(limit=limit):
        post_info = {
            'title': post.title,
            'text': post.selftext,
            'score': post.score,
            'num_comments': post.num_comments
        }
        
        # Get top comments for context
        post.comments.replace_more(limit=0)
        comments = []
        for comment in post.comments[:15]:  # Check more to filter out bots
            if hasattr(comment, 'body') and not comment.body.startswith('Hello! Thanks for your submission'):
                comments.append(comment.body)
                if len(comments) >= 5:  # Stop at 5 real comments
                    break
        
        post_info['top_comments'] = comments
        posts_data.append(post_info)
    
    return pd.DataFrame(posts_data)

def analyze_data_quality(df):
    """Analyze scraped data for chatbot training suitability"""
    
    print(f"Total posts: {len(df)}")
    print(f"Posts with text: {len(df[df['text'].str.len() > 0])}")
    print(f"Average score: {df['score'].mean():.2f}")
    print(f"Average comments: {df['num_comments'].mean():.2f}")
    
    # Show sample data
    print("\nSample post titles:")
    for title in df['title'].head(5):
        print(f"- {title}")

if __name__ == "__main__":
    # Scrape data
    df = scrape_worldcup_data(100)
    
    # Analyze
    analyze_data_quality(df)
    
    # Save for further processing
    df.to_csv('data/worldcup_data.csv', index=False)
    print("\nData saved to data/worldcup_data.csv")