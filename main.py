import os
import requests
from bs4 import BeautifulSoup
import html2text
# from urllib.parse import urlparse, urljoin

from linkUtils import get_base_url, clean_and_classify_links

def write_to_file(file_name, data):
    if not file_name:
        raise ValueError("The file name cannot be an empty string.")
    
    print(f"Attempting to write to: {file_name}")
    
    # Ensure the directory exists
    directory = os.path.dirname(file_name)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)

def extract_content_html2text(html_content):
    h = html2text.HTML2Text()
    h.ignore_links = True
    content = h.handle(html_content)
    return content


def fetch_html(url):
    try:
        base_url = get_base_url(url)
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.text

            # Write HTML content to file
            write_to_file(os.path.join("html", "output.html"), html_content)

            # Extract text content using html2text
            content = extract_content_html2text(html_content)
            write_to_file(os.path.join("content", "content_html2text.txt"), content)

            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract text content
            content = soup.get_text(separator='\n')
            write_to_file(os.path.join("content", "content.txt"), content)

            # Extract links
            links = [a.get("href") for a in soup.find_all("a") if a.get("href")]
            absolute_links, resolved_relative_links, ignored_links = clean_and_classify_links(links, base_url)

            write_to_file(os.path.join("links", "absoluteLinks.txt"), "\n".join(absolute_links))
            write_to_file(os.path.join("links", "resolvedRelativeLinks.txt"), "\n".join(resolved_relative_links))
            write_to_file(os.path.join("links", "ignoredLinks.txt"), "\n".join(ignored_links))

        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    url = "https://python.langchain.com/v0.2/docs/tutorials/llm_chain/"  # Replace with your target URL
    fetch_html(url)
