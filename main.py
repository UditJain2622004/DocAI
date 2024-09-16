import os
import requests
from bs4 import BeautifulSoup
# from urllib.parse import urlparse, urljoin

from utils.linkUtils import get_base_url, clean_and_classify_links
from utils.contentUtils import clean_html_for_text, extract_content_html2text
from utils.utils import write_to_file



def fetch_html(url):
    try:
        base_url = get_base_url(url)
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            # ==================== LINK CLEANING AND CLASSIFICATION ====================
            # Extract links
            links = [a.get("href") for a in soup.find_all("a") if a.get("href")]
            absolute_links, resolved_relative_links, ignored_links = clean_and_classify_links(links, base_url)

            write_to_file(os.path.join("links", "absoluteLinks.txt"), "\n".join(absolute_links))
            write_to_file(os.path.join("links", "resolvedRelativeLinks.txt"), "\n".join(resolved_relative_links))
            write_to_file(os.path.join("links", "ignoredLinks.txt"), "\n".join(ignored_links))


            # ==================== CONTENT EXTRACTION ====================
            cleaned_html_content = clean_html_for_text(html_content, base_url)

            # Write HTML content to file
            write_to_file(os.path.join("html", "output.html"), cleaned_html_content)

            # Extract text content using html2text
            content = extract_content_html2text(cleaned_html_content)
            write_to_file(os.path.join("content", "content_html2text.txt"), content)

            # Extract text content
            # soup = BeautifulSoup(cleaned_html_content, 'html.parser')
            # content = soup.get_text(separator='\n')
            # write_to_file(os.path.join("content", "content.txt"), content)
            
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")




# Example usage
if __name__ == "__main__":
    url = "https://python.langchain.com/docs/tutorials/llm_chain/#using-language-models"  # Replace with your target URL
    fetch_html(url)
