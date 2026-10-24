
import os
import sys
import re
import json
import time
from datetime import datetime

# Ensure standard output handles UTF-8 on Windows consoles safely
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Data handling
import pandas as pd

# Selenium components
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

# Import modular analysis functions from analyzer.py
import analyzer

# Project directories & paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_PATH = os.path.join(DATA_DIR, "imdb_movies.csv")
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")


def init_driver(headless=True):
    """
    Initializes and configures Google Chrome WebDriver with optimal options.
    Uses Selenium Manager (built into Selenium 4) for automatic driver management.
    
    Args:
        headless (bool): If True, runs Chrome in headless mode without a GUI window.
        
    Returns:
        webdriver.Chrome: Configured Chrome WebDriver instance.
    """
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--lang=en-US")
    
    # Modern realistic user-agent to comply with standard browser headers
    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    try:
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except WebDriverException as e:
        print(f"\n[!] Error initializing Chrome WebDriver: {e}")
        print("    Ensure Google Chrome is installed on your computer.\n")
        return None


def scrape_imdb_movies(limit=250, save_to_csv=True, headless=True):
    """
    Scrapes Top Movies from IMDb using Selenium WebDriver.
    
    Extracts:
    - Rank
    - Movie Name
    - Release Year
    - IMDb Rating
    - Number of Votes
    - Duration
    - Genre
    - Movie URL
    - Scraped Date/Time
    
    Args:
        limit (int): Maximum number of movies to scrape (default: 250).
        save_to_csv (bool): Whether to persist data to data/imdb_movies.csv.
        headless (bool): If True, runs browser silently; if False, opens visible Chrome window.
        
    Returns:
        pd.DataFrame or None: Scraped movies DataFrame or None on failure.
    """
    target_url = "https://www.imdb.com/chart/top/"
    print("\n" + "=" * 50)
    print("           STARTING IMDb MOVIE SCRAPER")
    print("=" * 50)
    print(f"[*] Target URL  : {target_url}")
    print(f"[*] Browser Mode: {'Visible Chrome Window (Live GUI)' if not headless else 'Headless (Silent background)'}")
    print("[*] Launching Selenium Chrome WebDriver...")

    driver = init_driver(headless=headless)
    if not driver:
        return None

    movies_data = []

    try:
        print("[*] Navigating to IMDb Top Rated Movies page...")
        driver.get(target_url)

        # Explicit Wait: Wait for page title and main container to load
        print("[*] Waiting for dynamic web elements to load (Selenium Explicit Wait)...")
        wait = WebDriverWait(driver, 25)
        
        # IMDb may trigger a brief security verification; wait for the real page title
        wait.until(lambda d: "IMDb" in d.title and "Top 250" in d.title)
        
        # Wait until movie card list items are loaded in the DOM
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")))

        # ---------------------------------------------------------------------
        # Step 1: Extract JSON-LD metadata for rich fields (Genre, Exact Votes)
        # ---------------------------------------------------------------------
        ld_map = {}
        try:
            ld_scripts = driver.find_elements(By.XPATH, "//script[@type='application/ld+json']")
            for s in ld_scripts:
                content = s.get_attribute("innerHTML")
                if content:
                    data = json.loads(content)
                    if isinstance(data, dict) and data.get("@type") == "ItemList":
                        for item_wrapper in data.get("itemListElement", []):
                            item = item_wrapper.get("item", {})
                            m_url = item.get("url", "").split("?")[0].rstrip("/")
                            if m_url:
                                ld_map[m_url] = item
                            name = item.get("name")
                            if name:
                                ld_map[name.strip().lower()] = item
        except Exception as e:
            print(f"[!] Note: Secondary metadata extraction info: {e}")

        # ---------------------------------------------------------------------
        # Step 2: Extract visual movie cards from DOM
        # ---------------------------------------------------------------------
        cards = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
        total_found = len(cards)
        print(f"[✓] Successfully located {total_found} movie elements in DOM.")

        actual_limit = min(limit, total_found) if limit else total_found
        print(f"[*] Extracting details for {actual_limit} movies...\n")

        scraped_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for idx in range(actual_limit):
            card = cards[idx]

            # 1. Rank
            rank = idx + 1
            try:
                rank_els = card.find_elements(By.CSS_SELECTOR, "[data-testid='title-list-item-ranking'], .ipc-signpost__text")
                if rank_els:
                    clean_r = rank_els[0].text.replace("#", "").strip()
                    if clean_r.isdigit():
                        rank = int(clean_r)
            except Exception:
                rank = idx + 1

            # 2. Movie Name & URL
            movie_name = "N/A"
            movie_url = "N/A"
            try:
                title_els = card.find_elements(By.CSS_SELECTOR, ".ipc-title__text, [class*='ipc-title__text']")
                if title_els:
                    raw_title = title_els[0].text.strip()
                    # Remove any numeric prefixes like "1. " or "2. "
                    movie_name = re.sub(r"^\d+\.\s*", "", raw_title)

                link_els = card.find_elements(By.CSS_SELECTOR, "a.ipc-title-link-wrapper, a.ipc-lockup-overlay")
                if link_els:
                    raw_href = link_els[0].get_attribute("href") or ""
                    movie_url = raw_href.split("?")[0]
            except Exception:
                pass

            # 3. Release Year & Duration
            release_year = "N/A"
            duration = "N/A"
            try:
                meta_spans = card.find_elements(By.CSS_SELECTOR, ".cli-title-metadata li, .cli-title-metadata span")
                for span in meta_spans:
                    txt = span.text.strip()
                    if re.match(r"^(19|20)\d{2}$", txt):
                        release_year = int(txt)
                    elif "h" in txt or "m" in txt:
                        duration = txt
            except Exception:
                pass

            # 4. IMDb Rating & Votes
            imdb_rating = "N/A"
            votes = "N/A"
            try:
                r_els = card.find_elements(By.CSS_SELECTOR, ".ipc-rating-star--rating")
                if r_els:
                    imdb_rating = float(r_els[0].text.strip())

                v_els = card.find_elements(By.CSS_SELECTOR, ".ipc-rating-star--voteCount")
                if v_els:
                    v_raw = v_els[0].text.strip().replace("(", "").replace(")", "").replace("\xa0", "").strip()
                    votes = v_raw
            except Exception:
                pass

            # 5. Enrich with Genre and exact vote counts from JSON-LD
            clean_url = movie_url.rstrip("/")
            ld_item = ld_map.get(clean_url) or ld_map.get(movie_name.lower())
            genre = "N/A"

            if ld_item:
                g = ld_item.get("genre")
                if isinstance(g, list):
                    genre = ", ".join(g)
                elif isinstance(g, str):
                    genre = g

                # If JSON-LD has exact integer ratingCount, use it for precision
                if ld_item.get("aggregateRating", {}).get("ratingCount"):
                    votes = int(ld_item["aggregateRating"]["ratingCount"])

                # Fill duration if missing in DOM
                if duration == "N/A" and ld_item.get("duration"):
                    d_match = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?", ld_item.get("duration", ""))
                    if d_match:
                        h, m = d_match.groups()
                        h_txt = f"{h}h " if h else ""
                        m_txt = f"{m}m" if m else ""
                        duration = (h_txt + m_txt).strip()

            # Parse string votes (e.g. '3.2M', '850K') into integer if needed
            if isinstance(votes, str) and votes != "N/A":
                v_clean = votes.upper()
                if "M" in v_clean:
                    try:
                        votes = int(float(v_clean.replace("M", "")) * 1_000_000)
                    except ValueError:
                        pass
                elif "K" in v_clean:
                    try:
                        votes = int(float(v_clean.replace("K", "")) * 1_000)
                    except ValueError:
                        pass
                elif v_clean.isdigit():
                    votes = int(v_clean)

            movie_record = {
                "Rank": rank,
                "Movie_Name": movie_name,
                "Release_Year": release_year,
                "IMDb_Rating": imdb_rating,
                "Votes": votes,
                "Duration": duration,
                "Genre": genre,
                "Movie_URL": movie_url,
                "Scraped_DateTime": scraped_timestamp
            }

            movies_data.append(movie_record)

            # Progress indicator in terminal
            if (idx + 1) % 50 == 0 or (idx + 1) == actual_limit:
                print(f"[*] Scraped {idx + 1}/{actual_limit} movies...")

    except TimeoutException:
        print("\n[!] Timeout Error: The IMDb page took too long to load.")
        print("    Please verify your internet connection and try again.")
        return None
    except WebDriverException as e:
        print(f"\n[!] Selenium WebDriver Error: {e}")
        return None
    except Exception as e:
        print(f"\n[!] Unexpected Scraping Error: {e}")
        return None
    finally:
        print("[*] Closing Selenium WebDriver session...")
        driver.quit()

    if not movies_data:
        print("[!] No movie records could be extracted.")
        return None

    # Step 7: Store in Pandas DataFrame
    df = pd.DataFrame(movies_data)

    # Step 8: Remove duplicate movies safely
    initial_count = len(df)
    df.drop_duplicates(subset=["Movie_Name", "Release_Year"], inplace=True)
    duplicates_removed = initial_count - len(df)
    if duplicates_removed > 0:
        print(f"[✓] Cleaned dataset: Removed {duplicates_removed} duplicate movie records.")

    # Step 9: Save result to CSV
    if save_to_csv:
        os.makedirs(DATA_DIR, exist_ok=True)
        df.to_csv(CSV_PATH, index=False, encoding="utf-8")
        print(f"\n[✓] Successfully saved {len(df)} movies to: {CSV_PATH}")

    # Step 10: Display scraped movies in a clean table in terminal
    print("\n--- Scraped Movies Preview ---")
    analyzer.view_movies(df, limit=10)

    return df


def display_menu():
    """
    Displays the interactive main menu interface.
    """
    print("\n" + "=" * 40)
    print("       IMDb MOVIE RATING SCRAPER        ")
    print("=" * 40)
    print("1. Scrape Movies")
    print("2. View Movies")
    print("3. Search Movie")
    print("4. Filter by Rating")
    print("5. Sort by Rating")
    print("6. Find Highest Rated Movie")
    print("7. Analyze Ratings")
    print("8. Exit")
    print("=" * 40)


def main():
    """
    Main interactive application loop.
    Continues running until the user selects Exit (Option 8).
    """
    print("\nWelcome to the IMDb Movie Rating Scraper & Analyzer!")
    print("A Python mini-project built with Selenium, Pandas, and Matplotlib.")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # 1. Scrape Movies
            print("\nOption 1: Scrape Movies selected.")
            view_browser = input("Do you want to see the Chrome browser open live on screen? (y/n, default: y): ").strip().lower()
            show_window = False if view_browser in ["n", "no"] else True
            scrape_imdb_movies(limit=250, save_to_csv=True, headless=not show_window)

        elif choice == "2":
            # 2. View Movies
            df = analyzer.load_data(CSV_PATH)
            if df is not None:
                sub_choice = input("\nEnter number of movies to view (press Enter for top 20, or 'all'): ").strip().lower()
                if sub_choice == "all":
                    analyzer.view_movies(df, limit=0)
                elif sub_choice.isdigit() and int(sub_choice) > 0:
                    analyzer.view_movies(df, limit=int(sub_choice))
                else:
                    analyzer.view_movies(df, limit=20)

        elif choice == "3":
            # 3. Search Movie
            df = analyzer.load_data(CSV_PATH)
            if df is not None:
                search_term = input("\nEnter movie name: ").strip()
                if search_term:
                    analyzer.search_movie(df, search_term)
                else:
                    print("Movie name cannot be empty.")

        elif choice == "4":
            # 4. Filter by Rating
            df = analyzer.load_data(CSV_PATH)
            if df is not None:
                raw_min = input("\nEnter minimum IMDb rating: ").strip()
                try:
                    min_rating = float(raw_min)
                    if 0.0 <= min_rating <= 10.0:
                        analyzer.filter_by_rating(df, min_rating)
                    else:
                        print("Rating must be between 0.0 and 10.0.")
                except ValueError:
                    print("Invalid input! Please enter a valid decimal number (e.g., 8.5).")

        elif choice == "5":
            # 5. Sort by Rating
            df = analyzer.load_data(CSV_PATH)
            if df is not None:
                print("\nSorting Options:")
                print("1. Highest to Lowest Rating")
                print("2. Lowest to Highest Rating")
                print("3. Most Votes")
                print("4. Newest Movies")
                sort_choice = input("Choose a sorting option (1-4): ").strip()
                if sort_choice in ["1", "2", "3", "4"]:
                    analyzer.sort_movies(df, int(sort_choice))
                else:
                    print("Invalid option! Please enter a number between 1 and 4.")

        elif choice == "6":
            # 6. Find Highest Rated Movie
            df = analyzer.load_data(CSV_PATH)
            if df is not None:
                analyzer.find_highest_rated_movie(df)

        elif choice == "7":
            # 7. Analyze Ratings
            df = analyzer.load_data(CSV_PATH)
            if df is not None:
                analyzer.analyze_ratings(df)
                plot_choice = input("Would you like to generate visualization charts in screenshots/? (y/n): ").strip().lower()
                if plot_choice in ["y", "yes"]:
                    analyzer.generate_charts(df, SCREENSHOTS_DIR)

        elif choice == "8":
            # 8. Exit
            print("\nThank you for using IMDb Movie Rating Scraper!")
            print("Project successfully terminated. Goodbye!\n")
            break

        else:
            print(f"\n[!] Invalid choice '{choice}'. Please select a valid option (1-8).")


if __name__ == "__main__":
    main()
