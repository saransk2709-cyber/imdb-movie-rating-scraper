# 🎬 IMDb Movie Rating Scraper & Analyzer

A complete, beginner-friendly Python mini-project for automated web scraping, data extraction, analysis, and visualization using **Python 3, Selenium WebDriver, Pandas, CSV, and Matplotlib**.

---

## 📌 Table of Contents
1. [Project Overview](#-project-overview)
2. [Project Objective](#-project-objective)
3. [Key Features](#-key-features)
4. [Technologies Used](#-technologies-used)
5. [Project Structure](#-project-structure)
6. [Scraped Dataset & CSV Format](#-scraped-dataset--csv-format)
7. [Installation & Setup Guide](#-installation--setup-guide)
8. [How to Run the Project](#-how-to-run-the-project)
9. [Sample Terminal Output](#-sample-terminal-output)
10. [Academic Lab Documentation](#-academic-lab-documentation)
    - [Aim](#aim)
    - [Objectives](#objectives)
    - [Software Requirements](#software-requirements)
    - [Hardware Requirements](#hardware-requirements)
    - [Algorithm](#algorithm)
    - [System Flowchart](#system-flowchart)
    - [Modular Breakdown](#modular-breakdown)
    - [Advantages & Limitations](#advantages--limitations)
    - [Future Enhancements](#future-enhancements)
    - [Academic Conclusion](#academic-conclusion)
11. [Viva Preparation (20+ Questions & Answers)](#-viva-preparation-20-questions--answers)
12. [Tamil / Tanglish Project Explanation Guide (வைவா விளக்கம்)](#-tamil--tanglish-project-explanation-guide-வைவா-விளக்கம்)

---

## 📖 Project Overview
The **IMDb Movie Rating Scraper** is an end-to-end Python automation and data analytics project. It uses **Selenium WebDriver** to automate Google Chrome, navigate to the publicly accessible **IMDb Top 250 Movies** chart (`https://www.imdb.com/chart/top/`), handle modern dynamic JavaScript rendering with **Explicit Waits**, extract structured movie details, clean and de-duplicate the records using **Pandas**, and store everything in a structured CSV dataset (`data/imdb_movies.csv`).

The project provides an interactive, menu-driven CLI interface that allows users to view, search, filter, sort, and statistically analyze movie ratings, along with generating Matplotlib visualizations saved in `screenshots/`.

---

## 🎯 Project Objective
1. Automate dynamic web data collection from IMDb without relying on third-party paid APIs.
2. Handle client-side JavaScript rendering using **Selenium WebDriver** and **Explicit Waits**.
3. Clean, transform, and de-duplicate web data using **Pandas**.
4. Store persistent records in a standardized **CSV format**.
5. Build an intuitive terminal-based menu for searching, filtering, and statistical analysis.
6. Generate informative graphical charts using **Matplotlib**.

---

## ✨ Key Features
- **Automated Web Scraping**: Automatically opens Chrome in headless mode and parses IMDb Top 250 movies.
- **Dynamic JavaScript Handling**: Employs Selenium `WebDriverWait` and `ExpectedConditions` to wait until elements are rendered.
- **Robust Exception Handling**: Prevents crashes caused by network dropouts, page timeouts, or missing HTML nodes (defaults to `'N/A'`).
- **Data De-duplication**: Automatically detects and drops duplicate movie records before writing to CSV.
- **Interactive Menu-Driven Console**:
  1. *Scrape Movies*: Scrapes live data and updates `data/imdb_movies.csv`.
  2. *View Movies*: Tabular display of movies with custom view limits or full listing.
  3. *Search Movie*: Fast, case-insensitive movie keyword search.
  4. *Filter by Rating*: User-defined rating threshold (e.g., `>= 8.5`).
  5. *Sort by Rating / Votes / Year*: Multi-criteria sorting (highest/lowest rating, popularity, newest).
  6. *Find Highest Rated Movie*: Instantly identifies the #1 top-rated movie with release metadata.
  7. *Analyze Ratings*: Computes aggregate metrics (mean rating, max, min, most voted title, count > 8.0, count > 9.0).
  8. *Visualization*: Generates top 10 rankings and rating distribution charts saved in `screenshots/`.

---

## 🛠️ Technologies Used
| Component | Technology | Purpose |
|---|---|---|
| Programming Language | **Python 3.11+** | Core programming logic and application flow |
| Web Scraping / Automation | **Selenium 4** | Browser automation, dynamic DOM traversal, explicit waits |
| Driver Management | **Selenium Manager / Chrome** | Automatic Chrome driver acquisition |
| Data Processing & Analysis | **Pandas** | DataFrame management, sorting, filtering, aggregation, de-duplication |
| Data Storage | **CSV (Comma-Separated Values)** | Persistent flat-file storage |
| Data Visualization | **Matplotlib** | Visual charting for ratings and distributions |
| Console Formatting | **Tabulate (Optional)** | Terminal grid table rendering |

---

## 📂 Project Structure
```text
imdb_movie_rating_scraper/
│
├── scraper.py             # Main application entry point & Selenium scraping logic
├── analyzer.py            # Data loading, searching, filtering, sorting & analysis logic
├── requirements.txt       # Project Python dependencies
├── README.md              # Complete project documentation & viva guide
├── data/
│   └── imdb_movies.csv    # Scraped movie dataset in CSV format
└── screenshots/
    ├── top_10_movies.png      # Top 10 movies by rating chart
    └── rating_distribution.png # Rating distribution histogram
```

---

## 📊 Scraped Dataset & CSV Format
The scraped dataset is stored inside `data/imdb_movies.csv` with the following columns:

| Column Name | Data Type | Description | Example |
|---|---|---|---|
| `Rank` | Integer | Movie ranking on IMDb chart | `1` |
| `Movie_Name` | String | Title of the film | `The Shawshank Redemption` |
| `Release_Year` | Integer | Year of theatrical release | `1994` |
| `IMDb_Rating` | Float | Public rating (out of 10.0) | `9.3` |
| `Votes` | Integer | Number of user votes / ratings | `3249876` |
| `Duration` | String | Running time of the movie | `2h 22m` |
| `Genre` | String | Movie genre category | `Drama` |
| `Movie_URL` | String | Direct canonical URL on IMDb | `https://www.imdb.com/title/tt0111161/` |
| `Scraped_DateTime`| Datetime | Timestamp of data extraction | `2026-10-09 21:00:58` |

### Sample CSV Row:
```csv
Rank,Movie_Name,Release_Year,IMDb_Rating,Votes,Duration,Genre,Movie_URL,Scraped_DateTime
1,The Shawshank Redemption,1994,9.3,3249876,2h 22m,Drama,https://www.imdb.com/title/tt0111161/,2026-10-09 21:00:58
```

---

## 🚀 Installation & Setup Guide

### Step 1: Install Python
Ensure Python 3.8 or newer is installed on your computer.
- Download from [python.org](https://www.python.org/downloads/)
- **Important**: During installation, check the box **"Add Python to PATH"**.

### Step 2: Open the Project Directory
Open PowerShell, Command Prompt, or VS Code terminal in the project folder:
```powershell
cd "c:\Users\yoges\OneDrive\Desktop\imdb movie rating scraper"
```

### Step 3: Create a Python Virtual Environment
A virtual environment isolates project dependencies:
```powershell
python -m venv venv
```

### Step 4: Activate the Virtual Environment
- **On Windows PowerShell:**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **On Windows Command Prompt (CMD):**
  ```cmd
  venv\Scripts\activate.bat
  ```

> ⚠️ **Fixing PowerShell Script Execution Policy Error:**
> If PowerShell displays the error:
> `File ...\Activate.ps1 cannot be loaded because running scripts is disabled on this system.`
> Run this command once in PowerShell:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Then reactivate: `.\venv\Scripts\Activate.ps1`.

### Step 5: Install Dependencies
Install all required libraries using `pip`:
```powershell
pip install -r requirements.txt
```

---

## 💻 How to Run the Project
To start the interactive program, run:
```powershell
python scraper.py
```

You can also run the analyzer module standalone:
```powershell
python analyzer.py
```

---

## 🖥️ Sample Terminal Output

### Main Menu:
```text
========================================
       IMDb MOVIE RATING SCRAPER        
========================================
1. Scrape Movies
2. View Movies
3. Search Movie
4. Filter by Rating
5. Sort by Rating
6. Find Highest Rated Movie
7. Analyze Ratings
8. Exit
========================================
Enter your choice: 
```

### 1. View Movies (Option 2):
```text
+--------+-----------------------------------------------+----------------+---------------+-----------+------------+---------------------------+
|   Rank | Movie_Name                                    |   Release_Year |   IMDb_Rating |     Votes | Duration   | Genre                     |
+========+===============================================+================+===============+===========+============+===========================+
|      1 | The Shawshank Redemption                      |           1994 |           9.3 | 3,249,876 | 2h 22m     | Drama                     |
|      2 | The Godfather                                 |           1972 |           9.2 | 2,263,116 | 2h 55m     | Crime, Drama              |
|      3 | The Dark Knight                               |           2008 |           9.1 | 3,237,014 | 2h 32m     | Crime, Thriller           |
|      4 | The Godfather Part II                         |           1974 |           9.0 | 1,517,778 | 3h 22m     | Crime, Drama              |
|      5 | The Lord of the Rings: The Return of the King |           2003 |           9.0 | 2,199,299 | 3h 21m     | Adventure, Drama, Fantasy |
+--------+-----------------------------------------------+----------------+---------------+-----------+------------+---------------------------+
```

### 2. Search Movie (Option 3):
```text
Enter movie name: Dark Knight

--- Search Results for 'Dark Knight' (2 matches) ---
+-----------------------+----------------+---------------+-----------+-----------------+
| Movie_Name            |   Release_Year |   IMDb_Rating |     Votes | Genre           |
+=======================+================+===============+===========+=================+
| The Dark Knight       |           2008 |           9.1 | 3,237,014 | Crime, Thriller |
| The Dark Knight Rises |           2012 |           8.4 | 2,032,119 | Crime, Thriller |
+-----------------------+----------------+---------------+-----------+-----------------+
```

### 3. Filter by Rating (Option 4):
```text
Enter minimum IMDb rating: 9.0

--- Movies with IMDb Rating >= 9.0 (7 found) ---
+--------+-----------------------------------------------+----------------+---------------+-----------+---------------------------+
|   Rank | Movie_Name                                    |   Release_Year |   IMDb_Rating |     Votes | Genre                     |
+========+===============================================+================+===============+===========+===========================+
|      1 | The Shawshank Redemption                      |           1994 |           9.3 | 3,249,876 | Drama                     |
|      2 | The Godfather                                 |           1972 |           9.2 | 2,263,116 | Crime, Drama              |
|      3 | The Dark Knight                               |           2008 |           9.1 | 3,237,014 | Crime, Thriller           |
|      4 | The Godfather Part II                         |           1974 |           9.0 | 1,517,778 | Crime, Drama              |
|      5 | The Lord of the Rings: The Return of the King |           2003 |           9.0 | 2,199,299 | Adventure, Drama, Fantasy |
|      6 | 12 Angry Men                                  |           1957 |           9.0 | 1,006,840 | Crime, Drama              |
|      7 | Schindler's List                              |           1993 |           9.0 | 1,607,633 | Biography, Drama, History |
+--------+-----------------------------------------------+----------------+---------------+-----------+---------------------------+
```

### 4. Find Highest Rated Movie (Option 6):
```text
Highest Rated Movie
-------------------
Movie:  The Shawshank Redemption
Rating: 9.3
Year:   1994
Votes:  3,249,876
Genre:  Drama
-------------------
```

### 5. Ratings Analysis (Option 7):
```text
========================================
          IMDb RATINGS ANALYSIS         
========================================
 Total number of movies : 250
 Average IMDb rating    : 8.31 / 10.0
 Highest rating         : 9.3
 Lowest rating          : 8.0
 Most voted movie       : The Shawshank Redemption (3,249,876 votes)
 Movies rated > 8.0     : 248 (99.2%)
 Movies rated > 9.0     : 3 (1.2%)
========================================
```

---

## 🎓 Academic Lab Documentation

### AIM
To design and develop an automated web scraping, data processing, and statistical analytics tool titled **“IMDb Movie Rating Scraper”** using Python, Selenium WebDriver, and Pandas to collect, store, and analyze movie rating metrics from IMDb.

### OBJECTIVES
1. To implement browser automation using Selenium to access client-side rendered dynamic web pages.
2. To utilize Selenium Explicit Waits (`WebDriverWait`, `presence_of_all_elements_located`) for robust element synchronization.
3. To extract multi-attribute movie metadata (Rank, Title, Year, Rating, Votes, Duration, Genre, URL, Scraped Timestamp).
4. To clean, format, and de-duplicate extracted records using Pandas DataFrame manipulation.
5. To persist the structured dataset in a persistent, comma-separated values (CSV) format.
6. To engineer an interactive, menu-driven command-line interface for filtering, searching, and sorting records.
7. To calculate statistical aggregates and render graphical charts using Matplotlib.

### SOFTWARE REQUIREMENTS
- **Operating System**: Windows 10 / 11, macOS, or Linux
- **Language**: Python 3.8+ (Tested on Python 3.11)
- **Web Browser**: Google Chrome (v115+)
- **Python Libraries**:
  - `selenium>=4.15.0`
  - `pandas>=2.0.0`
  - `matplotlib>=3.7.0`
  - `webdriver-manager>=4.0.0`
  - `tabulate>=0.9.0`

### HARDWARE REQUIREMENTS
- **Processor**: Intel Core i3 / AMD Ryzen 3 or higher
- **RAM**: Minimum 4 GB (8 GB recommended)
- **Disk Space**: At least 500 MB free storage
- **Network**: Active broadband/Wi-Fi connection

### ALGORITHM
1. **Start**: Launch the Python application (`scraper.py`).
2. **Initialize WebDriver**: Configure Chrome Options (headless mode, custom user-agent, disable automation flags).
3. **Navigate to URL**: Issue HTTP GET request to `https://www.imdb.com/chart/top/`.
4. **Explicit Wait**: Poll the DOM until the page title contains `"IMDb Top 250"` and movie cards are located.
5. **Data Extraction**:
   - Query movie list elements (`li.ipc-metadata-list-summary-item`).
   - Extract title, rank, year, duration, rating, and vote counts from DOM nodes.
   - Cross-reference embedded JSON-LD script tags for exact genres and precise vote counts.
   - Assign `'N/A'` to any missing or unresolvable attributes.
6. **DataFrame Ingestion**: Convert extracted list of dictionaries into a Pandas DataFrame.
7. **De-duplication**: Apply `df.drop_duplicates(subset=['Movie_Name', 'Release_Year'])`.
8. **Save to CSV**: Export cleaned DataFrame to `data/imdb_movies.csv`.
9. **Interactive Loop**:
   - Present user with menu options (1: Scrape, 2: View, 3: Search, 4: Filter, 5: Sort, 6: Highest, 7: Analyze, 8: Exit).
   - Execute user selection and display formatted outputs.
10. **Termination**: Exit cleanly when user selects option 8.

### SYSTEM FLOWCHART
```text
       ┌──────────────┐
       │    Start     │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │ Launch Chrome│
       │ via Selenium │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │ Load IMDb    │
       │ Top 250 Page │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │Explicit Wait │
       │ (WebDriver)  │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │Extract Movie │
       │Details (DOM) │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │Store in      │
       │Pandas DF     │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │Remove Dups & │
       │Save to CSV   │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │  User Menu   │◄────────┐
       │(Search/Sort/ │         │
       │Filter/Stats) │         │
       └──────┬───────┘         │
              │                 │
              ├─[Continue]──────┘
              │
       [Choice == 8]
              │
              ▼
       ┌──────────────┐
       │     Exit     │
       └──────────────┘
```

### MODULAR BREAKDOWN
1. **Web Scraping Module (`scraper.py`)**: Responsible for browser configuration, navigation, handling dynamic JavaScript challenges, finding DOM elements, parsing movie cards, and writing to CSV.
2. **Data Processing Module (`analyzer.py`)**: Ingests raw CSV data into Pandas DataFrames, performs type conversions, handles missing values, and normalizes string fields.
3. **Search Module (`analyzer.py - search_movie`)**: Implements case-insensitive keyword searching using regular expressions across film titles.
4. **Filtering Module (`analyzer.py - filter_by_rating`)**: Filters movie records based on numerical rating criteria entered by the user.
5. **Sorting Module (`analyzer.py - sort_movies`)**: Sorts DataFrame by IMDb rating (ascending/descending), popularity (votes), or release year.
6. **Analysis Module (`analyzer.py - analyze_ratings & generate_charts`)**: Computes summary statistics (mean, min, max, count thresholds) and renders Matplotlib charts.
7. **Storage Module (`data/imdb_movies.csv`)**: Acts as the persistent storage layer ensuring records survive process termination.

### ADVANTAGES
1. **Full Automation**: Extracts 250 records in seconds without human manual copying.
2. **Handles Dynamic Content**: Unlike standard HTTP request libraries, Selenium executes JavaScript and renders modern Single-Page Applications (SPAs).
3. **Offline Analysis**: Scraped data is cached in CSV, allowing instant queries, searches, and sorting without internet access.
4. **Modular Architecture**: Clean separation between web scraping (`scraper.py`) and analytics (`analyzer.py`).
5. **Fault Tolerant**: Uses explicit try-except blocks and fallback values (`N/A`) preventing unhandled exceptions.

### LIMITATIONS
1. **Dependent on DOM Structure**: If IMDb significantly restructures its CSS class names, scrapers require selector updates.
2. **Higher Resource Usage**: Selenium WebDriver consumes more memory and CPU than lightweight API calls.
3. **Network Latency Dependent**: Slower internet connections will increase page load times.
4. **Rate Limiting / Anti-Bot Challenges**: Aggressive or repeated scraping may trigger CAPTCHA or IP rate limits.

### FUTURE ENHANCEMENTS
1. **Multi-Page Pagination**: Extend scraping to IMDb Top Box Office, Most Popular Movies, and upcoming releases.
2. **Web Dashboard**: Build a modern web interface using Flask or Streamlit for graphical user interaction.
3. **Database Integration**: Migrate from flat CSV files to SQLite or PostgreSQL for relational queries.
4. **Automated Cron Scheduling**: Run the scraper on a daily/weekly schedule to track rating movements over time.
5. **Sentiment Analysis**: Scrape user review comments and apply Natural Language Processing (NLP) to gauge audience sentiment.

### ACADEMIC CONCLUSION
The **IMDb Movie Rating Scraper** demonstrates the practical fusion of web automation, data engineering, and statistical analytics. By utilizing Selenium WebDriver alongside Pandas and Matplotlib, the project overcomes dynamic client-side rendering limitations to yield a structured, queryable, and visualizable movie intelligence dataset.

---

## 💡 Viva Preparation (20+ Questions & Answers)

### Q1. What is Web Scraping?
**Answer:** Web scraping is the automated technique of extracting large amounts of unstructured or semi-structured data from websites and converting it into structured formats such as CSV, JSON, or SQL database tables.

### Q2. Why did you choose Selenium instead of Requests or BeautifulSoup?
**Answer:** Modern websites like IMDb use JavaScript frameworks to load dynamic content asynchronously. Standard libraries like `requests` only download static initial HTML, which often results in empty content or blocked responses. Selenium automates a real browser (Google Chrome), executes JavaScript, and accurately captures dynamic DOM elements.

### Q3. What is IMDb?
**Answer:** IMDb (Internet Movie Database) is the world's most popular online database of movie information, crew details, cast, user reviews, and ratings.

### Q4. Why did you use Pandas in this project?
**Answer:** Pandas provides fast, flexible, and expressive data structures (`DataFrame`) designed to make data cleaning, filtering, sorting, aggregation, and CSV input/output simple and efficient.

### Q5. What is a Pandas DataFrame?
**Answer:** A DataFrame is a two-dimensional, size-mutable, tabular data structure with labeled axes (rows and columns), similar to an Excel spreadsheet or SQL table.

### Q6. What is the difference between XPath and CSS Selector?
**Answer:**
- **CSS Selector**: Matches elements based on CSS classes, IDs, and attributes (e.g., `li.ipc-metadata-list-summary-item`). It is generally faster in modern browsers.
- **XPath (XML Path Language)**: A query language that navigates the XML/HTML document tree bidirectionally (e.g., `//script[@type='application/ld+json']`). It can traverse upwards and match text content.

### Q7. What is Selenium WebDriver?
**Answer:** Selenium WebDriver is a browser automation framework that provides a programming interface to control browsers natively via browser drivers (such as ChromeDriver).

### Q8. What is the difference between Implicit Wait and Explicit Wait?
**Answer:**
- **Implicit Wait**: A global timeout that tells WebDriver to wait a fixed maximum duration when trying to find any element before throwing `NoSuchElementException`.
- **Explicit Wait (`WebDriverWait`)**: Dynamically halts execution until a specific condition (e.g., element visibility, presence, or clickability) is satisfied or a timeout occurs. Explicit wait is preferred because it avoids arbitrary sleeping.

### Q9. Why is CSV chosen as the storage format?
**Answer:** CSV (Comma-Separated Values) is a lightweight, human-readable, plain-text format compatible with virtually all data science libraries (Pandas, NumPy, R), database import tools, and spreadsheet software (Excel).

### Q10. What is Exception Handling, and where is it used here?
**Answer:** Exception handling uses `try-except-finally` blocks to catch runtime anomalies without crashing the program. In this project, it is used during browser initialization, network timeouts (`TimeoutException`), missing HTML nodes, and user input validation (converting strings to floats).

### Q11. Why do we need to remove duplicate movie records?
**Answer:** Duplicates skew statistical analysis (such as average ratings and total counts) and waste storage. We use `df.drop_duplicates(subset=['Movie_Name', 'Release_Year'])` to maintain dataset integrity.

### Q12. How did you extract the IMDb rating for each movie?
**Answer:** Each movie card contains a rating badge with CSS selector `.ipc-rating-star--rating`. We locate this node, extract its text (e.g., `"9.3"`), and convert it into a floating-point number.

### Q13. How does the rating filter feature work?
**Answer:** Using boolean indexing in Pandas: `df[df['IMDb_Rating'] >= min_rating]`. Pandas evaluates each row against the condition and returns a new DataFrame containing only the qualifying rows.

### Q14. How does the sorting feature work in Pandas?
**Answer:** Using the `sort_values()` method. For example:
- Descending rating: `df.sort_values(by="IMDb_Rating", ascending=False)`
- Popularity: `df.sort_values(by="Votes", ascending=False)`

### Q15. What are the main limitations of web scraping?
**Answer:**
1. Vulnerability to website UI/structure updates.
2. Slower execution compared to direct REST APIs.
3. Potential IP rate limiting or anti-scraping blocks.
4. Higher network and memory consumption.

### Q16. What is the difference between Selenium scraping and using an official API?
**Answer:** An API provides direct, structured JSON/XML endpoints with documented authentication and predictable responses. Scraping parses HTML visually rendered for humans, which requires browser overhead and selector maintenance. However, scraping does not require paid API keys or restrictive API quotas.

### Q17. What happens if IMDb changes its website HTML layout?
**Answer:** The scraper may throw `NoSuchElementException` or return `'N/A'` because the old CSS selectors no longer match. To fix it, inspect the updated page in Chrome DevTools and update the CSS selectors in `scraper.py`.

### Q18. What is dynamic content in web pages?
**Answer:** Dynamic content refers to elements loaded or updated on a webpage via client-side JavaScript (AJAX / Fetch API) after the initial HTML page is delivered from the server.

### Q19. What is Headless Mode in Selenium Chrome?
**Answer:** Headless mode (`--headless=new`) runs Google Chrome without opening a visible graphical window on the desktop. This makes automated scripts faster, less distracting, and suitable for headless servers.

### Q20. Explain the complete project workflow from start to finish.
**Answer:**
1. `scraper.py` launches Chrome in headless mode.
2. Navigates to IMDb Top 250 and waits for DOM elements via Explicit Wait.
3. Iterates through 250 movie cards, safely extracting rank, title, year, rating, votes, duration, and genre.
4. Ingests data into a Pandas DataFrame, eliminates duplicates, and saves to `data/imdb_movies.csv`.
5. User enters menu choices in CLI to view, search, filter, sort, or analyze the records.
6. `analyzer.py` calculates statistical aggregates and generates Matplotlib charts in `screenshots/`.

---

## 🇮🇳 Tamil / Tanglish Project Explanation Guide (வைவா விளக்கம்)

கல்லூரி Viva அல்லது Project Presentation-ல் இந்த project-ஐ எளிமையாக விளக்குவதற்கான **Tamil / Tanglish Guide**:

### 1. Project-இன் அடிப்படை நோக்கம் (Concept)
> *"Sir/Madam, இந்த project-ஓட தலைப்பு **IMDb Movie Rating Scraper**. IMDb-ல இருக்கிற Top 250 திரைப்படங்களோட தகவல்களை (Rank, Movie Name, Year, Rating, Votes, Genre, Duration) தானாகவே (Automated-ஆக) திரட்டி, அதை ஒரு **CSV file**-ஆக சேமித்து, பிறகு **Pandas** மூலமாக Search, Filter, Sort, மற்றும் Statistical Analysis செய்யக்கூடிய ஒரு Python Mini Project ஆகும்."*

### 2. ஏன் Selenium பயன்படுத்தினோம்? (Why Selenium?)
> *"பொதுவாக `requests` அல்லது `BeautifulSoup` மூலமாக data எடுக்கும்போது, IMDb போன்ற நவீன தளங்களில் JavaScript மூலமாக dynamic-ஆக data render ஆவதால், static HTML-ல் data கிடைக்காது. அதனால் நாம் **Selenium WebDriver** பயன்படுத்தி ஒரு ரியல் Chrome Browser-ஐ automate பண்ணி, dynamic elements முழுமையாக load ஆகுற வரைக்கும் **Explicit Wait** பண்ணி data-வை extract பண்றோம்."*

### 3. இந்த Project-ல் உள்ள முக்கிய Modules
1. **Scraping Module (`scraper.py`)**:
   - Chrome Browser-ஐ **Headless Mode**-ல் (background-ல்) open செய்கிறது.
   - IMDb Top 250 பக்கத்திற்குச் சென்று, `WebDriverWait` மூலமாக data வரும் வரை காத்திருந்து, DOM elements மற்றும் JSON-LD மூலமாக விவரங்களை எடுக்கிறது.
   - ஏதாவது data இல்லை என்றால் crash ஆகாமல் `'N/A'` என்று சேமிக்கிறது.
   - எடுத்த data-வை `Pandas DataFrame`-ஆக மாற்றி, duplicates-ஐ நீக்கி, `data/imdb_movies.csv`-ல் சேமிக்கிறது.
2. **Analysis Module (`analyzer.py`)**:
   - **View**: படங்களை அட்டவணை வடிவில் பார்க்க உதவுகிறது.
   - **Search**: Case-insensitive substring search (எ.கா: 'Dark Knight' என்று கொடுத்தால் கண்டுபிடிக்கும்).
   - **Filter**: Rating அடிப்படையில் (எ.கா: `>= 8.5`) வடிகட்டுகிறது.
   - **Sort**: அதிக Rating, குறைந்த Rating, அதிக Votes, புதிய படங்கள் என வரிசைப்படுத்துகிறது.
   - **Statistics & Visualization**: சராசரி Rating, அதிகபட்ச Rating, மற்றும் Matplotlib மூலமாக Charts (`screenshots/` folder-ல்) உருவாக்குகிறது.

### 4. Viva-வில் கேட்கக்கூடிய பொதுவான கேள்விகளுக்கு Tamil/Tanglish பதில்கள்:
- **Duplicates எப்படி நீக்கினீர்கள்?**
  > *"Pandas-ல் `df.drop_duplicates(subset=['Movie_Name', 'Release_Year'])` பயன்படுத்தி பெயர் மற்றும் வருடம் ஒன்றாக இருக்கும் duplicate பதிவுகளை நீக்கினோம்."*
- **Explicit Wait எதற்கு?**
  > *"Website load ஆக இணைய வேகம் மாறுபடும். `time.sleep()` போட்டால் தேவையில்லாமல் நேரம் வீணாகும். `WebDriverWait` பயன்படுத்தினால் குறிப்பிட்ட element திரையில் தோன்றிய உடனே அடுத்த step-க்கு சென்றுவிடும்."*
- **Headless Mode என்றால் என்ன?**
  > *"`--headless=new` கொடுக்கும்போது Chrome Browser விண்டோ கண்ணுக்குத் தெரியாமல் background-ல் run ஆகும். இதனால் RAM மற்றும் CPU பயன்பாடு குறையும்."*

---

## 📜 License & Disclaimer
This project is developed for **academic and educational purposes only**. Scraping practices should strictly comply with the target website's Terms of Service and `robots.txt` guidelines.
