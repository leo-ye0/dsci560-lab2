import praw
import pandas as pd
from datetime import datetime
import kagglehub
import os

# Reddit API setup (Register at https://www.reddit.com/prefs/apps/)
# Replace with your credentials
reddit = praw.Reddit(
    client_id="NJrUxQuuK72o-2DUgH8mMQ",
    client_secret="Pl0M8u1XEoGfPPYmtGHJfvBeojoqpw", 
    user_agent="Educational-Score979 "
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
        post.comments.replace_more(limit=0) #do not click "load more comments"
        comments = []
        for comment in post.comments[:15]:  # Check more to filter out bots
            if hasattr(comment, 'body') and not comment.body.startswith('Hello! Thanks for your submission'):
                comments.append(comment.body)
                if len(comments) >= 5:  # Stop at 5 real comments
                    break
        
        post_info['top_comments'] = comments
        
        # Only keep posts with at least 2 real comments
        if len(comments) >= 2:
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

    # download csv dataset
def download_worldcup_csv():
    world_cup_csv_path = kagglehub.dataset_download("abecklas/fifa-world-cup")

    world_cup_csv_df = {}
    # file names
    csv_files = [
        "WorldCups.csv",
        "WorldCupMatches.csv",
        "WorldCupPlayers.csv"
    ]

    output_dir = os.path.join(os.path.dirname(__file__), "../data")
    os.makedirs(output_dir, exist_ok=True)

    # save csv files
    for filename in csv_files:
        csv_path = os.path.join(world_cup_csv_path, filename)
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            if filename == "WorldCups.csv":
                df["Year"] = pd.to_numeric(df["Year"], errors="coerce").fillna(0).astype(int)
                df["GoalsScored"] = pd.to_numeric(df["GoalsScored"], errors="coerce").fillna(0).astype(int)

            elif filename == "WorldCupMatches.csv":
                df["Year"] = pd.to_numeric(df["Year"], errors="coerce").fillna(0).astype(int)
                df["Home Team Goals"] = pd.to_numeric(df["Home Team Goals"], errors="coerce").fillna(0).astype(int)
                df["Away Team Goals"] = pd.to_numeric(df["Away Team Goals"], errors="coerce").fillna(0).astype(int)
            output_path = os.path.join(output_dir, filename)
            df.to_csv(output_path, index=False)
            print(f"saved {filename} to {output_path}")
            world_cup_csv_df[filename] = df 
        else:
            print(f"error: file {filename} not found")
    return world_cup_csv_df

# analyze csv data
def analyze_worldcup_data(dataframes):

    if "WorldCups.csv" in dataframes:
        df = dataframes["WorldCups.csv"]
        print("\nWorld Cups Summary")
        print(f"Tournaments: {len(df)}")
        print(f"Years: {df['Year'].min()} - {df['Year'].max()}")
        print(f"Most Wins:\n{df['Winner'].value_counts().head(3).to_string()}")


    if "WorldCupMatches.csv" in dataframes:
        df = dataframes["WorldCupMatches.csv"]
        df["TotalGoals"] = df["Home Team Goals"] + df["Away Team Goals"]
        print("\nMatch Stats")
        print(f"Total Matches: {len(df)}")
        print(f"Average Goals/Match: {df['TotalGoals'].mean():.2f}")
        print("Top Scoring Matches:")
        print(df.sort_values("TotalGoals", ascending=False)[[
            "Year", "Home Team Name", "Away Team Name", "TotalGoals"
        ]].head(3))
        print(f"Top Match Cities:\n{df['City'].value_counts().head(3).to_string()}")

    if "WorldCupPlayers.csv" in dataframes:
        df = dataframes["WorldCupPlayers.csv"]
        print("\nPlayer Stats")
        print(f"Total Appearances: {len(df)}")
        print(f"Unique Players: {df['Player Name'].nunique()}")
        print("Most Frequent Players:")
        print(df['Player Name'].value_counts().head(3).to_string())



if __name__ == "__main__":
    # Scrape data
    df = scrape_worldcup_data(100)
    
    # Analyze
    analyze_data_quality(df)
    
    # Save for further processing
    df.to_csv('data/worldcup_data.csv', index=False)
    print("\nData saved to data/worldcup_data.csv")

    # get csv data
    world_cup_csv = download_worldcup_csv()
    # analyze csv data
    analyze_worldcup_data(world_cup_csv)
