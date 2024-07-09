import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to fetch and parse HTML content
def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return BeautifulSoup(response.text, 'html.parser')

# Function to extract all child links from a page
def get_child_links(base_url, soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        full_link = urljoin(base_url, link)
        if full_link.startswith(base_url):  # Keep only internal links
            links.append(full_link)
    return links

# Function to scrape a page and its child pages
def scrape_website(base_url):
    scraped_data = {}
    visited = set()

    def scrape_page(url):
        if url in visited:
            return
        visited.add(url)
        print(f"Scraping: {url}")

        soup = fetch_page(url)
        page_content = soup.get_text(separator=' ', strip=True)
        scraped_data[url] = page_content

        child_links = get_child_links(base_url, soup)
        for link in child_links:
            scrape_page(link)

    scrape_page(base_url)
    return scraped_data

# Main script
if __name__ == "__main__":
    website_url = 'http://example.com'  # Replace with your target website URL
    scraped_data = scrape_website(website_url)
    
    # Print scraped data (or process it as needed)
    for url, content in scraped_data.items():
        print(f"URL: {url}\nContent: {content[:200]}...\n")  # Print first 200 chars of content for brevity
