import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
import os

# Function to fetch and parse HTML content
def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    return None

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
        if soup is None:
            print(f"Failed to scrape: {url}")
            return

        page_content = soup.get_text(separator=' ', strip=True)
        scraped_data[url] = page_content

        child_links = get_child_links(base_url, soup)
        for link in child_links:
            scrape_page(link)

    scrape_page(base_url)
    return scraped_data

def write_to_markdown(scraped_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for url, content in scraped_data.items():
            f.write(f"# {url}\n\n")
            f.write(f"{content[:200]}...\n\n")  # Write first 200 chars of content for brevity
            f.write("---\n\n")  # Add a horizontal rule between entries
    print(f"Markdown file created: {output_file}")

# Main script
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scrape.py <base_url> <output_file>")
        sys.exit(1)

    base_url = sys.argv[1]
    output_file = sys.argv[2]

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    scraped_data = scrape_website(base_url)
    write_to_markdown(scraped_data, output_file)
