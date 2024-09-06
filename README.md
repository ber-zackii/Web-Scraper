# Web Scraper for News Articles

This is a Python-based web scraper that extracts the title, byline, updated date, and content of a news article given a URL. It uses `Requests` to fetch the webpage and `BeautifulSoup` to parse the HTML content.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Example](#example)

## Features
- Scrapes and returns the following details from a news article:
  - Title
  - Byline (if available)
  - Updated date (if available)
  - Article content
- Handles common web scraping errors like missing elements or network issues.

## Requirements
Make sure you have the following Python libraries installed:

- [Requests](https://docs.python-requests.org/en/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

You can install these dependencies using pip:
```bash
pip install requests beautifulsoup4
```

## Setup

1. Clone the repository or download the script.
2. Make sure you have Python installed (preferably Python 3.7+).
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

To run the scraper, open a terminal and navigate to the folder containing `scrapArticle.py`.

Run the script and provide a URL for the news article when prompted:

```bash
python scrapArticle.py
```

## Example Output

If you provide the following URL:


```bash
https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html
```
The output will be something like this:

```bash
. Title: The Remote Learning Chronicles
. Byline: By John Doe
. Updated Date: September 2, 2020
. Content: As the world grapples with the pandemic, remote learning has taken the spotlight. ...
```