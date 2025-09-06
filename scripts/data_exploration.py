import kagglehub
import pandas as pd
import os

def download_worldcup_csv():
    # download dataset
    path = kagglehub.dataset_download("abecklas/fifa-world-cup")
    print("Dataset downloaded to:", path)

    df_names = {}
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
        csv_path = os.path.join(path, filename)
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
            df_names[filename] = df 
        else:
            print(f"error: file {filename} not found")
    return df_names

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
    df = download_worldcup_csv()
    analyze_worldcup_data(df)
