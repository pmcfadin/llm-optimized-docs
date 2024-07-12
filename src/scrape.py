import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
import os
import openai

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

# Function to fetch and parse HTML content
def fetch_page(url):
    print(f"Fetching: {url}")
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as err:
        print(f"An error occurred while fetching the page: {err}")
    return None

# Function to extract all child links from a page
def get_child_links(base_url, html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        full_link = urljoin(base_url, link)
        if full_link.startswith(base_url):  # Keep only internal links
            links.append(full_link)
    return links

# Function to convert HTML to Markdown using LLM
def html_to_markdown(html):
    prompt = """
    You are an expert HTML to Markdown converter. Your task is to convert the given HTML content into well-formatted Markdown, following these guidelines:

    1. Preserve the hierarchical structure of headings (h1, h2, h3, etc.).
    2. Convert HTML lists (ul, ol) to proper Markdown lists.
    3. Preserve code blocks and their language specifications if available.
    4. Convert links to Markdown format, preserving both the link text and URL.
    5. Convert tables to Markdown table format.
    6. Preserve emphasis (bold, italic) using Markdown syntax.
    7. Include any important images, converting them to Markdown image syntax and preserving alt text.
    8. Omit any navigation elements, headers, footers, or sidebars that are not part of the main content.
    9. Preserve any important notes, warnings, or callouts, formatting them distinctly in Markdown.
    10. Ensure that the resulting Markdown is clean, readable, and properly spaced.

    Here's the HTML content to convert:

    {html}

    Please provide the converted Markdown content.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that converts HTML to Markdown."},
            {"role": "user", "content": prompt.format(html=html)}
        ]
    )

    return response.choices[0].message['content']

# Function to scrape a page and its child pages
def scrape_website(base_url):
    scraped_data = {}
    visited = set()

    def scrape_page(url):
        if url in visited:
            return
        visited.add(url)
        print(f"Scraping: {url}")

        html = fetch_page(url)
        if html is None:
            print(f"Failed to scrape: {url}")
            return

        markdown_content = html_to_markdown(html)
        scraped_data[url] = markdown_content

        child_links = get_child_links(base_url, html)
        for link in child_links:
            scrape_page(link)

    scrape_page(base_url)
    return scraped_data

def write_to_markdown(scraped_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for url, content in scraped_data.items():
            f.write(f"Source: {url}\n\n")
            f.write(content)
            f.write("\n\n---\n\n")
    print("Markdown file created: {}".format(output_file))

# Function to remove duplicate content
def remove_duplicates(scraped_data):
    seen_content = set()
    unique_data = {}
    for url, content in scraped_data.items():
        if content not in seen_content:
            seen_content.add(content)
            unique_data[url] = content
    return unique_data

# Main script
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scrape.py <base_url> <output_file>")
        sys.exit(1)

    base_url = sys.argv[1]
    output_file = sys.argv[2]

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Set up OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    scraped_data = scrape_website(base_url)
    unique_data = remove_duplicates(scraped_data)
    write_to_markdown(unique_data, output_file)
