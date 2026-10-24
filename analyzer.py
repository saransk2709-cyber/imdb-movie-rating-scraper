"""
=============================================================================
Project: IMDb Movie Rating Scraper & Analyzer
File: analyzer.py
Description: Data Analysis, Search, Filter, Sort, and Visualization Module
Author: Yogesh
=============================================================================
"""

import os
import sys
import re
import pandas as pd
import matplotlib.pyplot as plt

# Ensure standard output handles UTF-8 on Windows consoles safely
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# Optional pretty table formatting via tabulate if installed
try:
    from tabulate import tabulate
    HAS_TABULATE = True
except ImportError:
    HAS_TABULATE = False

DEFAULT_CSV_PATH = os.path.join(os.path.dirname(__file__), "data", "imdb_movies.csv")
DEFAULT_SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), "screenshots")


def load_data(csv_path=DEFAULT_CSV_PATH):
    """
    Safely loads the scraped IMDb movies CSV file into a Pandas DataFrame.
    Performs data cleansing, type conversions, and validation.
    
    Args:
        csv_path (str): Filepath to the CSV dataset.
        
    Returns:
        pd.DataFrame or None: Loaded and cleaned DataFrame, or None if error occurs.
    """
    if not os.path.exists(csv_path):
        print(f"\n[!] Error: Dataset not found at '{csv_path}'.")
        print("    Please run Option 1 (Scrape Movies) first to collect live data.\n")
        return None

    if os.path.getsize(csv_path) == 0:
        print(f"\n[!] Error: The file '{csv_path}' is empty.")
        print("    Please run Option 1 (Scrape Movies) to generate movie records.\n")
        return None

    try:
        df = pd.read_csv(csv_path, encoding="utf-8")
        
        # Verify required columns exist
        expected_cols = [
            "Rank", "Movie_Name", "Release_Year", "IMDb_Rating",
            "Votes", "Duration", "Genre", "Movie_URL", "Scraped_DateTime"
        ]
        missing_cols = [col for col in expected_cols if col not in df.columns]
        if missing_cols:
            print(f"[!] Warning: Missing expected columns in CSV: {missing_cols}")

        # Ensure correct numeric types for numerical operations
        if "Rank" in df.columns:
            df["Rank"] = pd.to_numeric(df["Rank"], errors="coerce").fillna(0).astype(int)
        if "Release_Year" in df.columns:
            df["Release_Year"] = pd.to_numeric(df["Release_Year"], errors="coerce").fillna(0).astype(int)
        if "IMDb_Rating" in df.columns:
            df["IMDb_Rating"] = pd.to_numeric(df["IMDb_Rating"], errors="coerce")
        if "Votes" in df.columns:
            # Parse votes string if not purely numeric (e.g., '3.2M', '800K')
            def parse_votes(v):
                if pd.isna(v):
                    return 0
                if isinstance(v, (int, float)):
                    return int(v)
                v_str = str(v).replace(",", "").strip().upper()
                if "M" in v_str:
                    try:
                        return int(float(v_str.replace("M", "")) * 1_000_000)
                    except ValueError:
                        return 0
                elif "K" in v_str:
                    try:
                        return int(float(v_str.replace("K", "")) * 1_000)
                    except ValueError:
                        return 0
                try:
                    return int(float(v_str))
                except ValueError:
                    return 0

            df["Votes"] = df["Votes"].apply(parse_votes)

        return df

    except Exception as e:
        print(f"\n[!] Unexpected error loading dataset: {e}\n")
        return None


def format_table(df_subset, columns=None):
    """
    Formats a Pandas DataFrame for clean tabular terminal display.
    Uses 'tabulate' with grid styling if available; otherwise falls back to Pandas string.
    
    Args:
        df_subset (pd.DataFrame): Dataframe to display.
        columns (list): List of column names to display.
    """
    if df_subset is None or df_subset.empty:
        print("No records found.")
        return

    display_df = df_subset.copy()
    if columns:
        valid_cols = [c for c in columns if c in display_df.columns]
        display_df = display_df[valid_cols]

    # Format votes nicely with commas for display
    if "Votes" in display_df.columns:
        display_df["Votes"] = display_df["Votes"].apply(lambda v: f"{v:,}" if isinstance(v, (int, float)) and v > 0 else "N/A")

    if HAS_TABULATE:
        print(tabulate(display_df, headers="keys", tablefmt="grid", showindex=False))
    else:
        pd.set_option("display.max_columns", None)
        pd.set_option("display.width", 1000)
        print(display_df.to_string(index=False))


def view_movies(df, limit=20):
    """
    Displays the top movies in a clean tabular view.
    
    Args:
        df (pd.DataFrame): The movies dataframe.
        limit (int): Number of records to preview (0 to view all).
    """
    if df is None or df.empty:
        print("No movies available to display.")
        return

    cols = ["Rank", "Movie_Name", "Release_Year", "IMDb_Rating", "Votes", "Duration", "Genre"]
    
    if limit and limit > 0 and limit < len(df):
        print(f"\n--- Previewing Top {limit} Movies (Total: {len(df)}) ---")
        subset = df.head(limit)
    else:
        print(f"\n--- Displaying All {len(df)} Movies ---")
        subset = df

    format_table(subset, columns=cols)


def search_movie(df, movie_name):
    """
    Performs case-insensitive search by movie name.
    
    Args:
        df (pd.DataFrame): The movies dataframe.
        movie_name (str): The search query.
    """
    if df is None or df.empty:
        print("No movie dataset loaded.")
        return

    query = movie_name.strip()
    if not query:
        print("Search query cannot be empty.")
        return

    # Case-insensitive substring match
    matches = df[df["Movie_Name"].str.contains(re.escape(query), case=False, na=False)]

    print(f"\n--- Search Results for '{query}' ({len(matches)} match{'es' if len(matches) != 1 else ''}) ---")
    if matches.empty:
        print(f"No movies found matching '{query}'. Try another keyword.")
        return

    cols = ["Movie_Name", "Release_Year", "IMDb_Rating", "Votes", "Genre"]
    format_table(matches, columns=cols)


def filter_by_rating(df, min_rating):
    """
    Filters movies whose IMDb rating is greater than or equal to min_rating.
    
    Args:
        df (pd.DataFrame): The movies dataframe.
        min_rating (float): Minimum rating threshold.
    """
    if df is None or df.empty:
        print("No movie dataset loaded.")
        return

    filtered = df[df["IMDb_Rating"] >= min_rating]
    print(f"\n--- Movies with IMDb Rating >= {min_rating:.1f} ({len(filtered)} found) ---")

    if filtered.empty:
        print(f"No movies found with rating >= {min_rating:.1f}.")
        return

    cols = ["Rank", "Movie_Name", "Release_Year", "IMDb_Rating", "Votes", "Genre"]
    format_table(filtered, columns=cols)


def sort_movies(df, option):
    """
    Sorts movies according to the chosen criteria:
    1: Highest to Lowest Rating
    2: Lowest to Highest Rating
    3: Most Votes
    4: Newest Movies
    
    Args:
        df (pd.DataFrame): The movies dataframe.
        option (int): Chosen sorting option.
    """
    if df is None or df.empty:
        print("No movie dataset loaded.")
        return

    cols = ["Rank", "Movie_Name", "Release_Year", "IMDb_Rating", "Votes", "Genre"]

    if option == 1:
        print("\n--- Sorted by Rating (Highest to Lowest) ---")
        sorted_df = df.sort_values(by="IMDb_Rating", ascending=False)
    elif option == 2:
        print("\n--- Sorted by Rating (Lowest to Highest) ---")
        sorted_df = df.sort_values(by="IMDb_Rating", ascending=True)
    elif option == 3:
        print("\n--- Sorted by Votes (Most Popular) ---")
        sorted_df = df.sort_values(by="Votes", ascending=False)
    elif option == 4:
        print("\n--- Sorted by Release Year (Newest to Oldest) ---")
        sorted_df = df.sort_values(by="Release_Year", ascending=False)
    else:
        print("Invalid sorting option.")
        return

    # Preview top 20 of sorted result
    format_table(sorted_df.head(20), columns=cols)
    if len(sorted_df) > 20:
        print(f"(Showing top 20 out of {len(sorted_df)} movies)")


def find_highest_rated_movie(df):
    """
    Finds and displays the movie with the highest IMDb rating.
    
    Args:
        df (pd.DataFrame): The movies dataframe.
    """
    if df is None or df.empty:
        print("No movie dataset loaded.")
        return

    valid_ratings = df.dropna(subset=["IMDb_Rating"])
    if valid_ratings.empty:
        print("No valid rating information available.")
        return

    max_rating = valid_ratings["IMDb_Rating"].max()
    top_movies = valid_ratings[valid_ratings["IMDb_Rating"] == max_rating]

    print("\nHighest Rated Movie")
    print("-------------------")
    for _, movie in top_movies.iterrows():
        print(f"Movie:  {movie['Movie_Name']}")
        print(f"Rating: {movie['IMDb_Rating']}")
        print(f"Year:   {movie['Release_Year']}")
        print(f"Votes:  {movie['Votes']:,}")
        print(f"Genre:  {movie['Genre']}")
        print("-------------------")


def analyze_ratings(df):
    """
    Calculates and displays summary statistics using Pandas:
    - Total number of movies
    - Average IMDb rating
    - Highest rating
    - Lowest rating
    - Movie with highest votes
    - Number of movies above 8.0
    - Number of movies above 9.0
    
    Args:
        df (pd.DataFrame): The movies dataframe.
    """
    if df is None or df.empty:
        print("No movie dataset loaded.")
        return

    total_movies = len(df)
    avg_rating = df["IMDb_Rating"].mean()
    highest_rating = df["IMDb_Rating"].max()
    lowest_rating = df["IMDb_Rating"].min()
    
    # Movie with highest votes
    max_votes_idx = df["Votes"].idxmax()
    most_voted_movie = df.loc[max_votes_idx]

    movies_above_8 = (df["IMDb_Rating"] > 8.0).sum()
    movies_above_9 = (df["IMDb_Rating"] > 9.0).sum()

    print("\n========================================")
    print("          IMDb RATINGS ANALYSIS         ")
    print("========================================")
    print(f" Total number of movies : {total_movies}")
    print(f" Average IMDb rating    : {avg_rating:.2f} / 10.0")
    print(f" Highest rating         : {highest_rating:.1f}")
    print(f" Lowest rating          : {lowest_rating:.1f}")
    print(f" Most voted movie       : {most_voted_movie['Movie_Name']} ({most_voted_movie['Votes']:,} votes)")
    print(f" Movies rated > 8.0     : {movies_above_8} ({(movies_above_8/total_movies)*100:.1f}%)")
    print(f" Movies rated > 9.0     : {movies_above_9} ({(movies_above_9/total_movies)*100:.1f}%)")
    print("========================================\n")


def generate_charts(df, output_dir=DEFAULT_SCREENSHOTS_DIR):
    """
    Generates and saves Matplotlib visualizations:
    1. Top 10 movies by IMDb rating
    2. Rating distribution histogram
    
    Args:
        df (pd.DataFrame): The movies dataframe.
        output_dir (str): Folder to save chart images.
    """
    if df is None or df.empty:
        print("No data available to plot.")
        return

    os.makedirs(output_dir, exist_ok=True)

    # Set aesthetic plot style
    plt.style.use("seaborn-v0_8-darkgrid" if "seaborn-v0_8-darkgrid" in plt.style.available else "default")

    # ---------------- Chart 1: Top 10 Movies by Rating ----------------
    chart1_path = os.path.join(output_dir, "top_10_movies.png")
    top_10 = df.sort_values(by=["IMDb_Rating", "Votes"], ascending=[False, False]).head(10)
    top_10 = top_10.iloc[::-1]  # reverse for horizontal bar chart (highest on top)

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(top_10["Movie_Name"], top_10["IMDb_Rating"], color="#F5C518", edgecolor="#333333", height=0.6)
    
    ax.set_xlim(8.0, 10.0)
    ax.set_xlabel("IMDb Rating", fontsize=12, fontweight="bold")
    ax.set_title("Top 10 Movies by IMDb Rating", fontsize=14, fontweight="bold", pad=15)
    
    # Add data labels on bars
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.03, bar.get_y() + bar.get_height() / 2, f"{width:.1f}",
                va="center", ha="left", fontsize=10, fontweight="bold", color="#111111")

    plt.tight_layout()
    plt.savefig(chart1_path, dpi=300)
    plt.close()
    print(f"[OK] Saved chart: {chart1_path}")

    # ---------------- Chart 2: Rating Distribution ----------------
    chart2_path = os.path.join(output_dir, "rating_distribution.png")
    fig, ax = plt.subplots(figsize=(9, 5))
    
    ratings = df["IMDb_Rating"].dropna()
    n, bins, patches = ax.hist(ratings, bins=12, color="#1f77b4", edgecolor="#ffffff", alpha=0.85)

    ax.set_xlabel("IMDb Rating", fontsize=12, fontweight="bold")
    ax.set_ylabel("Number of Movies", fontsize=12, fontweight="bold")
    ax.set_title("Distribution of IMDb Movie Ratings", fontsize=14, fontweight="bold", pad=15)
    
    # Highlight mean rating line
    mean_val = ratings.mean()
    ax.axvline(mean_val, color="#d9534f", linestyle="--", linewidth=2, label=f"Mean: {mean_val:.2f}")
    ax.legend(fontsize=11)

    plt.tight_layout()
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    print(f"[OK] Saved chart: {chart2_path}")


if __name__ == "__main__":
    # Standalone execution test for analyzer
    print("Testing IMDb Analyzer...")
    dataset = load_data()
    if dataset is not None:
        view_movies(dataset, limit=5)
        analyze_ratings(dataset)
        find_highest_rated_movie(dataset)
        generate_charts(dataset)
