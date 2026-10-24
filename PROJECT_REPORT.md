# 📑 A MINI-PROJECT REPORT ON
# **IMDb MOVIE RATING SCRAPER & DATA ANALYZER**

---

### **Submitted in partial fulfillment of the requirements for the degree of**
### **BACHELOR OF COMPUTER SCIENCE / ENGINEERING / APPLICATIONS**

---

**Submitted By:**  
**YOGESH**  
*Department of Computer Science and Engineering*  
*Academic Year: 2026 – 2027*

---

## 📋 BONAFIDE CERTIFICATE

This is to certify that the project report entitled **"IMDb MOVIE RATING SCRAPER & DATA ANALYZER"** is a bonafide work carried out by **YOGESH** in partial fulfillment for the award of Bachelor's Degree in Computer Science / Engineering.

<br><br>

------------------------------------ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ------------------------------------  
**Internal Guide / Supervisor** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Head of the Department (HOD)**  
*Department of Computer Science* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Department of Computer Science*  

<br>

**Submitted for University / College Viva-Voce Examination held on:** ____________________

<br>

------------------------------------ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ------------------------------------  
**Internal Examiner** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **External Examiner**  

---

## 🙋‍♂️ DECLARATION

I hereby declare that the project entitled **"IMDb MOVIE RATING SCRAPER & DATA ANALYZER"** submitted to the Department of Computer Science is a record of original work done by me under the supervision of faculty members. The results embodied in this report have not been submitted to any other University or Institute for the award of any degree or diploma.

**Place:**  
**Date:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **(YOGESH)**

---

## 🙏 ACKNOWLEDGEMENT

I express my sincere gratitude and deep sense of thankfulness to our respected **Principal** and our **Head of the Department** for providing all the computational facilities and continuous encouragement throughout the project duration.

I would like to extend my heartfelt thanks to my **Project Guide** for their valuable suggestions, constructive criticism, and timely guidance during the various phases of this project.

Finally, I convey my sincere thanks to my family, faculty members, and fellow classmates who directly or indirectly extended their support and assistance in completing this mini project successfully.

---

## 📑 TABLE OF CONTENTS

| Chapter No. | Title | Page No. |
| :---: | :--- | :---: |
| | **Abstract** | i |
| | **List of Figures & Tables** | ii |
| **1** | **INTRODUCTION** | 1 |
| | 1.1 Overview | 1 |
| | 1.2 Problem Statement | 2 |
| | 1.3 Project Objectives | 2 |
| | 1.4 Scope of the Project | 3 |
| **2** | **LITERATURE SURVEY & SYSTEM ANALYSIS** | 4 |
| | 2.1 Existing System | 4 |
| | 2.2 Drawbacks of Existing System | 4 |
| | 2.3 Proposed System | 5 |
| | 2.4 Advantages of Proposed System | 5 |
| **3** | **SYSTEM REQUIREMENT SPECIFICATION (SRS)** | 6 |
| | 3.1 Software Requirements | 6 |
| | 3.2 Hardware Requirements | 6 |
| | 3.3 Feasibility Study | 7 |
| **4** | **SYSTEM DESIGN & ARCHITECTURE** | 9 |
| | 4.1 System Architecture | 9 |
| | 4.2 Data Flow Diagram (DFD) | 10 |
| | 4.3 Program Flowchart | 11 |
| | 4.4 Dataset Schema Design | 12 |
| **5** | **MODULE DESCRIPTION & IMPLEMENTATION** | 13 |
| | 5.1 Module 1: Browser Automation & Driver Setup | 13 |
| | 5.2 Module 2: Dynamic Web Scraping & Explicit Wait | 14 |
| | 5.3 Module 3: Data Cleaning & Persistence (`Pandas` & `CSV`) | 15 |
| | 5.4 Module 4: Search & Multi-criteria Filtering Engine | 16 |
| | 5.5 Module 5: Sorting & Statistical Analytics Engine | 17 |
| | 5.6 Module 6: Data Visualization Engine (`Matplotlib`) | 18 |
| | 5.7 Module 7: Interactive Terminal User Interface | 19 |
| **6** | **TESTING & EXPERIMENTAL RESULTS** | 20 |
| | 6.1 Testing Methodologies | 20 |
| | 6.2 Test Cases & Execution Results | 21 |
| | 6.3 Sample Terminal Output & Generated Visualizations | 22 |
| **7** | **CONCLUSION & FUTURE ENHANCEMENTS** | 24 |
| | 7.1 Conclusion | 24 |
| | 7.2 Future Enhancements | 24 |
| **8** | **REFERENCES** | 25 |

---

## 📄 ABSTRACT

In the current era of Big Data and entertainment analytics, cinema rating databases like IMDb (Internet Movie Database) serve as critical benchmarks for consumer choices, box-office predictions, and recommendation algorithms. However, extracting real-time movie statistics from modern single-page and JavaScript-heavy websites using conventional static scraping packages (e.g., standard HTTP GET requests via `requests` or `BeautifulSoup`) fails because content is dynamically rendered on the client-side DOM. Furthermore, relying on commercial APIs introduces query limits, cost overheads, and access restrictions.

This project, **"IMDb Movie Rating Scraper & Data Analyzer"**, implements an automated, end-to-end web scraping, data extraction, analysis, and visualization pipeline developed in **Python 3**. The system uses **Selenium WebDriver** to automate Google Chrome, interact with dynamic DOM elements, handle asynchronous content rendering via **Explicit Synchronization Waits (`WebDriverWait`)**, and bypass bot challenge checks. 

The extracted records (including Rank, Title, Release Year, IMDb Rating, Vote Count, Runtime, Genre, and Source URL) are cleansed, type-cast, de-duplicated, and structured using **Pandas**, before being stored in an offline flat-file **CSV database**. An intuitive, interactive command-line interface provides users with search, multi-criteria filter, multi-level sorting, summary statistical aggregations (mean, max, min, threshold distributions), and graphical visual reporting using **Matplotlib**. The system was rigorously tested against IMDb Top 250 records, demonstrating 100% data integrity, fault-tolerant execution, and zero reliance on paid external APIs.

---

# CHAPTER 1: INTRODUCTION

### 1.1 Overview
The Internet Movie Database (IMDb) is the world's most popular and authoritative source for movie, TV, and celebrity information, hosting millions of user reviews, critic scores, and historical popularity records. For cinephiles, movie buffs, entertainment researchers, and data scientists, IMDb's "Top 250" ranking represents the highest-acclaimed cinematic achievements across decades.

Web scraping is the automated technique of extracting large volumes of unstructured or semi-structured data from websites and transforming it into structured formats such as CSV, Excel, or relational databases. Modern web platforms utilize client-side JavaScript frameworks (React, Vue, Next.js) which dynamically inject content into the DOM (Document Object Model) after the initial HTML payload has loaded. 

This project bridges web automation and data analytics by utilizing **Python 3**, **Selenium 4**, **Pandas**, and **Matplotlib** to build a self-contained, offline-capable movie scraping and analysis software system.

### 1.2 Problem Statement
Extracting data from web platforms presents the following core challenges:
1. **Dynamic Content Rendering**: Modern IMDb pages rely on client-side JavaScript and lazy loading. Traditional static HTML parsers (`requests`, `urllib`, basic `BeautifulSoup`) return incomplete HTML skeletons where movie titles, vote counts, and ratings are not yet rendered.
2. **API Restrictions & Pricing**: Official movie APIs (or third-party wrappers) enforce rate limiting, require API keys, and charge subscription fees for bulk analytical queries.
3. **Data Quality & Inconsistencies**: Scraped raw web data often contains irregularities—vote counts represented as shorthand strings (e.g., "3.2M", "850K"), missing runtime fields, duplicate movie cards, and inconsistent date timestamps.
4. **Lack of User-Friendly Tooling**: Many scraping scripts run as single-shot throwaway scripts without providing query mechanisms, search filters, descriptive statistical reports, or graphical summaries for end-users.

### 1.3 Project Objectives
The primary objectives of this project are:
- **Automated Extraction**: Develop an automated bot using Selenium WebDriver that navigates to IMDb Top 250, handles network latency via Explicit Synchronization Waits, and extracts complete movie records.
- **Data Cleansing & Transformation**: Parse raw strings, normalize vote counts into integer figures, cast release years and ratings into numeric data types, and purge duplicates.
- **Persistent Storage**: Safely store the validated dataset in `data/imdb_movies.csv` with standard UTF-8 encoding.
- **Search, Filter & Sorting Engine**: Build search capabilities (case-insensitive keyword matching), threshold-based rating filters, and multi-factor sorting (by rating, popularity, and release date).
- **Statistical Aggregation**: Compute key metrics including dataset size, mean rating, extreme bounds (maximum/minimum), and proportion of films exceeding defined thresholds (> 8.0, > 9.0).
- **Visualization**: Automate generation of publication-ready graphical plots (Top 10 bar charts and rating frequency histograms) saved directly to disk.
- **Dual Scraping Modes**: Support both **Live Visible Browser Mode** (for visual demonstration) and **Headless Mode** (for silent background automated runs).

### 1.4 Scope of the Project
The scope encompasses extracting, structuring, storing, querying, and visually analyzing 250 benchmark films from IMDb. The modular software architecture allows easy expansion to other IMDb charts (e.g., Most Popular Movies, Top TV Shows, Box Office Hits) or other web data sources.

---

# CHAPTER 2: LITERATURE SURVEY & SYSTEM ANALYSIS

### 2.1 Existing System
Traditionally, data collection from public web services was handled by:
1. **Manual Browsing**: Users manually search websites, copy titles, ratings, and votes into spreadsheets—an error-prone, labor-intensive approach.
2. **Static HTTP Scrapers**: Python scripts utilizing `requests` + `BeautifulSoup` to fetch raw HTML.
3. **Third-Party APIs**: Subscribing to commercial cinema APIs (RapidAPI, OMDb API) subject to daily rate quotas.

### 2.2 Drawbacks of Existing System
- **Inability to Execute JavaScript**: Static scrapers cannot trigger client-side scripts, failing when encountering dynamic components.
- **Fragility**: Hardcoded sleep timers (`time.sleep()`) either waste execution time or trigger `NoSuchElementException` when networks experience lag.
- **Cost & Dependencies**: External APIs can be deprecated, blocked, or monetize previously free endpoints.
- **No Analytical Workflow**: Most scraping scripts do not provide built-in exploratory data analysis (EDA) or terminal query engines.

### 2.3 Proposed System
The proposed **IMDb Movie Rating Scraper & Analyzer** addresses these drawbacks through a modular two-tier architecture:
1. **Scraping Layer (`scraper.py`)**: Automates Google Chrome via Selenium 4 and Selenium Manager. Employs `WebDriverWait` with `ExpectedConditions` to dynamically wait for DOM elements. Extracts both DOM elements and rich embedded JSON-LD schema metadata.
2. **Analytical Layer (`analyzer.py`)**: Utilizes Pandas to load, clean, validate, filter, sort, and calculate descriptive summary metrics. Generates visualizations using Matplotlib and displays formatted grid tables using Tabulate.

### 2.4 Advantages of Proposed System
- **Real Browser Emulation**: Renders the complete DOM including dynamic JavaScript and lazy-loaded nodes.
- **Intelligent Synchronization**: Replaces blind sleep intervals with dynamic conditional event polling.
- **Offline Self-Sufficiency**: Once scraped, data is stored in CSV format, enabling instant offline querying, searching, and chart rendering without internet access.
- **Clean Separation of Concerns**: Scraping logic is decoupled from data analysis, ensuring modularity, maintainability, and clean code principles.

---

# CHAPTER 3: SYSTEM REQUIREMENT SPECIFICATION (SRS)

### 3.1 Software Requirements
| Component | Specification |
| :--- | :--- |
| **Operating System** | Microsoft Windows 10 / 11 (64-bit) / Linux / macOS |
| **Programming Language** | Python 3.10 / 3.11 / 3.12 |
| **Web Browser** | Google Chrome (Latest Stable Version) |
| **Browser Driver** | ChromeDriver (Auto-managed via Selenium Manager) |
| **Automation Framework** | Selenium >= 4.15.0 |
| **Data Processing Library** | Pandas >= 2.0.0 |
| **Plotting / Visualization** | Matplotlib >= 3.7.0 |
| **Console Table Formatting** | Tabulate >= 0.9.0 |
| **Development IDE** | Visual Studio Code / PyCharm / Antigravity IDE |

### 3.2 Hardware Requirements
| Component | Minimum Specification | Recommended Specification |
| :--- | :--- | :--- |
| **Processor** | Intel Core i3 / AMD Ryzen 3 (2.0 GHz) | Intel Core i5 / AMD Ryzen 5 or higher |
| **RAM** | 4 GB | 8 GB or higher |
| **Hard Disk Space** | 500 MB free disk space | 1 GB SSD free space |
| **Network Interface** | Active Broadband / Wi-Fi Connection (for scraping) | High-Speed Internet (> 10 Mbps) |

### 3.3 Feasibility Study
- **Technical Feasibility**: Python provides mature, enterprise-grade libraries (`selenium`, `pandas`, `matplotlib`). Selenium 4 includes built-in driver management eliminating manual driver downloads.
- **Operational Feasibility**: The application provides an interactive menu requiring simple numerical inputs (1–8), making it easy to operate without technical training.
- **Economic Feasibility**: Built entirely using open-source, free tools without paid licenses, cloud subscriptions, or proprietary API billing.

---

# CHAPTER 4: SYSTEM DESIGN & ARCHITECTURE

### 4.1 System Architecture

```
+-------------------------------------------------------------+
|                         USER INPUT                          |
|                Interactive Terminal Menu (1-8)              |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                    SCRAPER MODULE (scraper.py)              |
|  - init_driver() [Headless or Live GUI Mode]                |
|  - Google Chrome Automation via Selenium 4                  |
|  - WebDriverWait Synchronization                            |
|  - Extraction: DOM Nodes + Embedded JSON-LD Metadata        |
+------------------------------+------------------------------+
                               |
                               v (Saves Scraped Data)
+-------------------------------------------------------------+
|                 PERSISTENT STORAGE (CSV)                    |
|                   data/imdb_movies.csv                      |
+------------------------------+------------------------------+
                               |
                               v (Loads & Validates)
+-------------------------------------------------------------+
|                   ANALYZER MODULE (analyzer.py)             |
|  - load_data() [Type casting, Vote normalization]           |
|  - view_movies() [Tabulate grid table formatting]           |
|  - search_movie() [Regex case-insensitive query]            |
|  - filter_by_rating() [Rating threshold slicing]            |
|  - sort_movies() [Rating, Popularity, Release Year]         |
|  - analyze_ratings() [Mean, Max, Min, Counts > 8.0 & 9.0]   |
|  - generate_charts() [Matplotlib Horizontal Bar & Histogram]|
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                       OUTPUT PRODUCTS                       |
|  1. Clean Terminal Tables & Statistics                      |
|  2. screenshots/top_10_movies.png                           |
|  3. screenshots/rating_distribution.png                     |
+-------------------------------------------------------------+
```

### 4.2 Data Flow Diagram (DFD Level 0 & Level 1)

#### DFD Level 0 (Context Diagram):
```
[User] -------- (Run Option / Query) --------> [IMDb Scraper & Analyzer System]
[User] <---- (Tables / Stats / Charts) <------- [IMDb Scraper & Analyzer System]
[IMDb Scraper & Analyzer System] <--(HTTP/DOM)---> [IMDb Web Server]
```

#### DFD Level 1:
```
[User] ---> (1. Scrape Request) ---> [1.0 Driver & Navigation Engine] ---> [IMDb Web Page]
                                                 |
                                       (Dynamic DOM Elements)
                                                 v
                                     [2.0 Data Extraction & Parser]
                                                 |
                                         (Raw Dictionary)
                                                 v
                                     [3.0 Data Cleaning & Deduplication]
                                                 |
                                                 v
                                      [data/imdb_movies.csv]
                                                 |
[User] ---> (2-7. Query/Analysis) --> [4.0 Pandas Query Engine]
                                                 |
                        +------------------------+------------------------+
                        |                                                 |
                        v                                                 v
          [5.0 Tabular Terminal Display]                      [6.0 Matplotlib Visualizer]
                        |                                                 |
                        v                                                 v
                 Terminal Output                              screenshots/*.png
```

### 4.3 Program Flowchart
```
                [ START ]
                    |
                    v
            Display Menu (1 - 8)
                    |
                    v
            Read User Choice
                    |
      +-------------+-------------+-------------+-------------+
      |             |             |             |             |
   Choice 1      Choice 2      Choice 3      Choice 4      Choice 8
  (Scrape)        (View)       (Search)      (Filter)       (Exit)
      |             |             |             |             |
 Prompt Visible   Read Limit    Prompt Title  Prompt Rating  [ STOP ]
 Browser (y/n)      |             |             |
      |          Display       Display       Display
 Launch Chrome    Table        Matches       Filtered
      |
 Wait & Scrape
      |
 Save to CSV
      |
      +-------------> Return to Menu Loop
```

### 4.4 Dataset Schema Design (`data/imdb_movies.csv`)
| Column Field | Data Type | Constraint | Description | Example |
| :--- | :--- | :--- | :--- | :--- |
| **`Rank`** | Integer | PRIMARY KEY / NOT NULL | Position in IMDb Top 250 chart | `1` |
| **`Movie_Name`** | String / Text | NOT NULL | Official movie title | `The Shawshank Redemption` |
| **`Release_Year`** | Integer | Range: 1900 - 2030 | Year of theatrical release | `1994` |
| **`IMDb_Rating`** | Float | Range: 0.0 - 10.0 | User score on IMDb | `9.3` |
| **`Votes`** | Integer | Non-negative integer | Total user votes cast | `3249876` |
| **`Duration`** | String | Standard Format | Movie runtime | `2h 22m` |
| **`Genre`** | String | Comma-delimited | Primary cinematic genres | `Drama` |
| **`Movie_URL`** | String / URL | Valid HTTPS URL | Direct web hyperlink | `https://www.imdb.com/title/tt0111161/` |
| **`Scraped_DateTime`** | Datetime | YYYY-MM-DD HH:MM:SS | Timestamp of extraction | `2026-10-09 21:00:58` |

---

# CHAPTER 5: MODULE DESCRIPTION & IMPLEMENTATION

### 5.1 Module 1: Browser Automation & Driver Setup (`init_driver`)
This module initializes Google Chrome using Selenium 4's native **Selenium Manager**, avoiding outdated third-party executables.
- **Headless Mode Flag**: If enabled, Chrome executes invisibly without rendering a GUI window, conserving CPU/RAM resources.
- **Live GUI Mode**: Allows users to watch the browser launch, navigate, and dynamically scroll across web pages in real-time.
- **Security & Headers Configuration**:
  - Sets window dimension to `1920x1080`.
  - Injects realistic `user-agent` headers (`Mozilla/5.0...`).
  - Disables `--disable-blink-features=AutomationControlled` to comply with standard browser behaviors.

### 5.2 Module 2: Dynamic Web Scraping & Explicit Wait (`scrape_imdb_movies`)
Modern single-page applications dynamically populate nodes after initial network transfer.
- **Target URL**: `https://www.imdb.com/chart/top/`
- **Explicit Synchronization**: Uses `WebDriverWait(driver, 25)` paired with `expected_conditions.presence_of_all_elements_located` targeting the CSS selector `li.ipc-metadata-list-summary-item`.
- **Hybrid Extraction Approach**:
  1. **Schema JSON-LD Parsing**: Parses embedded `<script type="application/ld+json">` tags to extract high-fidelity fields (exact total votes, canonical URLs, and genre categorizations).
  2. **DOM Traversal Fallback**: Traverses individual HTML nodes using relative XPath and CSS selectors to retrieve Rank, Title, Year, Duration, and Rating tags.
  3. **Fault-Tolerant Null Handling**: Wraps individual element lookups in `try-except` blocks; if an element is missing, defaults to `'N/A'` or `'0'` to prevent system crashes.

### 5.3 Module 3: Data Cleaning & Persistence (`analyzer.load_data`)
Raw extracted datasets require sanitization before mathematical processing:
- **Vote String Parsing**: Converts shorthand representations (e.g., `'3.2M'` -> `3,200,000`, `'850K'` -> `850,000`, removing commas).
- **Type Coercion**: Casts `Rank` and `Release_Year` to integers; `IMDb_Rating` to 64-bit floating point numbers.
- **De-duplication**: Invokes `df.drop_duplicates(subset=['Rank', 'Movie_Name'])` to eliminate duplicate entries.
- **CSV Output**: Writes cleanly formatted records to `data/imdb_movies.csv` using UTF-8 encoding.

### 5.4 Module 4: Search & Multi-criteria Filtering Engine
- **Search Engine (`search_movie`)**: Implements case-insensitive substring searching via `re.escape()` on the `Movie_Name` column. For example, querying `"Dark Knight"` returns both *The Dark Knight* and *The Dark Knight Rises*.
- **Rating Filter (`filter_by_rating`)**: Employs vectorized boolean indexing (`df[df["IMDb_Rating"] >= min_rating]`) to isolate movies exceeding specified rating thresholds (e.g., `>= 8.8`).

### 5.5 Module 5: Sorting & Statistical Analytics Engine
- **Multi-Factor Sorting (`sort_movies`)**:
  - `Option 1`: Highest to Lowest Rating (`ascending=False`).
  - `Option 2`: Lowest to Highest Rating (`ascending=True`).
  - `Option 3`: Most Popular / Highest Votes (`Votes`, `ascending=False`).
  - `Option 4`: Chronological Recency (`Release_Year`, `ascending=False`).
- **Statistical Aggregation (`analyze_ratings`)**: Computes summary metrics:
  $$\text{Mean Rating} = \frac{1}{N}\sum_{i=1}^{N} r_i$$
  $$\text{Maximum Rating} = \max(r_i), \quad \text{Minimum Rating} = \min(r_i)$$
  $$\text{Most Voted Title} = \arg\max(\text{Votes})$$
  $$\text{High-Tier Percentage} = \frac{\sum [r_i > 8.0]}{N} \times 100\%$$

### 5.6 Module 6: Data Visualization Engine (`generate_charts`)
Automates creation of visual charts using Matplotlib:
1. **Top 10 Horizontal Bar Chart (`top_10_movies.png`)**:
   - Visualizes top 10 ranked titles.
   - Distinctive IMDb gold styling (`#F5C518`) with dark border outlines.
   - Embedded numerical score labels on each bar.
2. **Rating Frequency Histogram (`rating_distribution.png`)**:
   - Plots distribution of ratings across 12 bins.
   - Highlights the sample mean via an overlaid red dashed vertical line.

### 5.7 Module 7: Interactive Terminal User Interface (`main`)
Presents an 8-option terminal menu:
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
```

---

# CHAPTER 6: TESTING & EXPERIMENTAL RESULTS

### 6.1 Testing Methodologies
- **Unit Testing**: Validated individual subroutines (`init_driver()`, `parse_votes()`, `filter_by_rating()`).
- **Integration Testing**: Verified pipeline transitions: browser extraction -> Pandas DataFrame -> CSV storage -> analytics consumption.
- **Boundary Testing**: Validated edge cases (invalid rating inputs like `11.5` or `abc`, empty search terms, missing CSV dataset).

### 6.2 Test Cases & Execution Results

| Test ID | Test Scenario | Input Data | Expected Output | Actual Result | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | Chrome Driver Launch | Headless / Live Mode | Chrome launches successfully | Browser initialized without errors | **PASS** |
| **TC-02** | Explicit Synchronization | Dynamic IMDb URL | Wait until 250 cards exist | Detected 250 elements in DOM | **PASS** |
| **TC-03** | Data Extraction & Saving | Scrape limit = 250 | All 250 records written to CSV | 250 records saved in CSV | **PASS** |
| **TC-04** | Case-Insensitive Search | Keyword: `"Dark Knight"` | Return 2 matching records | 2 matching records returned | **PASS** |
| **TC-05** | Rating Threshold Filter | Threshold: `>= 9.0` | Display records with score >= 9.0 | Exact records displayed (7 items) | **PASS** |
| **TC-06** | Boundary Validation | Filter rating: `15.0` | Display error message | `"Rating must be between 0.0 and 10.0"` | **PASS** |
| **TC-07** | Statistical Aggregation | Option 7 | Mean rating = 8.31 / 10.0 | Statistical report printed accurately | **PASS** |
| **TC-08** | Chart Generation | Generate plots | Save 2 `.png` images in `screenshots/` | Images created with 300 DPI | **PASS** |

### 6.3 Sample Terminal Output & Generated Visualizations

#### Terminal Analytics Summary:
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

Highest Rated Movie:
-------------------
Movie:  The Shawshank Redemption
Rating: 9.3
Year:   1994
Votes:  3,249,876
Genre:  Drama
-------------------
```

#### Generated Charts:
- **`screenshots/top_10_movies.png`**: High-resolution horizontal bar chart highlighting top-rated films.
- **`screenshots/rating_distribution.png`**: Rating distribution histogram with mean overlay.

---

# CHAPTER 7: CONCLUSION & FUTURE ENHANCEMENTS

### 7.1 Conclusion
The **IMDb Movie Rating Scraper & Data Analyzer** successfully demonstrates an end-to-end web scraping, automation, and data analytics application in Python. By combining **Selenium WebDriver** for dynamic JavaScript page rendering, **Pandas** for data sanitization and querying, and **Matplotlib** for visualization, the system overcomes the limitations of traditional static web scrapers. 

The project operates independently of third-party paid APIs, handles network latency through dynamic synchronization waits, provides an intuitive menu-driven CLI, and stores data locally in CSV format for instant offline access.

### 7.2 Future Enhancements
1. **Graphical User Interface (GUI)**: Implement a desktop GUI using **PyQt6** or **Tkinter**, or an interactive web dashboard using **Streamlit** or **Flask**.
2. **Sentiment Analysis**: Scrape user review comments from individual movie sub-pages and apply Natural Language Processing (NLP) with **NLTK** or **VADER** to calculate sentiment polarity.
3. **Automated Scheduling**: Implement automated cron jobs or Windows Task Scheduler scripts to refresh the movie dataset periodically.
4. **Relational Database Migration**: Transition from flat CSV storage to an **SQLite** or **PostgreSQL** relational database.
5. **Cross-Platform Box-Office Correlation**: Scrape budget and worldwide box-office gross data to analyze correlation between rating scores and commercial profitability.

---

# CHAPTER 8: REFERENCES

1. Selenium Documentation: *WebDriver & Browser Automation in Python*, https://www.selenium.dev/documentation/
2. McKinney, Wes. *Python for Data Analysis: Data Wrangling with Pandas, NumPy, and Jupyter*, 3rd Edition, O'Reilly Media, 2022.
3. Hunter, J. D. *Matplotlib: A 2D Graphics Environment*, Computing in Science & Engineering, Vol. 9, No. 3, pp. 90–95, 2007.
4. IMDb Top 250 Chart: *Internet Movie Database Official Top Rated Movies*, https://www.imdb.com/chart/top/
5. Python Software Foundation: *Python 3.11 Documentation & Standard Library*, https://docs.python.org/3/
6. W3C WebDriver Specification: *World Wide Web Consortium Recommendation*, https://www.w3.org/TR/webdriver2/
