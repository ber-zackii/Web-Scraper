import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the title of the article
        title = soup.find('h1').get_text() if soup.find('h1') else "No title found"

        # Find the article content (may vary based on site structure)
        paragraphs = soup.find_all('p')
        content = '\n'.join([para.get_text() for para in paragraphs])

        # Optional: Find the byline and updated date if available
        byline = soup.find(class_='byline').get_text() if soup.find(class_='byline') else "No byline found"
        updated_date = soup.find(class_='updated').get_text() if soup.find(class_='updated') else "No updated date found"

        # Display the result
        return {
            'Title': title,
            'Byline': byline,
            'Updated Date': updated_date,
            'Content': content
        }

    except requests.exceptions.RequestException as e:
        return f"Error fetching the page: {e}"

# Example usage:
if __name__ == "__main__":
    news_url = input("Enter the news article URL: ")
    result = scrape_article(news_url)
    
    # Print the scraped information
    print("Title:", result)
    
