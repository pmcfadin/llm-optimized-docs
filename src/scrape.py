import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
import os
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

# Function to fetch and parse HTML content
def fetch_page(url):
    print(f"Fetching: {url}")
    
    try:
        response = requests.get(url, headers=headers)
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

# Function to clean and structure content
def clean_content(soup):
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Extract main content
    main_content = soup.find('main')
    if not main_content:
        main_content = soup

    # Extract headers and their content
    content = []
    for header in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        header_text = header.get_text(strip=True)
        content.append(f"{'#' * int(header.name[1:])} {header_text}")
        
        next_element = header.find_next_sibling()
        while next_element and next_element.name not in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            if next_element.name in ['p', 'ul', 'ol']:
                content.append(next_element.get_text(separator='\n', strip=True))
            next_element = next_element.find_next_sibling()

    # Join content with double newlines for readability
    text = '\n\n'.join(content)

    # Remove redundant newlines
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text

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

        page_content = clean_content(soup)
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
            f.write(content)
            f.write("\n\n---\n\n")  # Add a horizontal rule between entries
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
