from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import html2text


tags_to_remove = [
    'nav', 'script', 'footer', 'header', 'style', 'img', 'svg', 'noscript', 
    'form', 'input', 'button', 'select', 'textarea', 'label', 'iframe', 
    'video', 'audio', 'object', 'embed', 'canvas', 'map', 'area', 'base', 
    'link', 'meta', 'param', 'source', 'track', 'wbr','s','del','option'
]

tags_to_unwrap = [
    'span', 'section', 'article', 'aside', 'main', 'figure', 'figcaption',
    'details', 'summary', 'dialog', 'fieldset', 'legend', 'optgroup', 
    'output', 'progress', 'meter', 'hr', 'b', 'i', 'u',  'strong', 'em','mark', 'small','ins','dfn', 'kbd','data','a'
]

tags_to_keep = [
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p',  
      'sub', 'sup', 'code', 'pre', 'blockquote', 
    'q', 'cite', 'abbr',  'var', 'samp',  'time', 'ol', 
    'ul', 'li', 'table', 'thead', 'tfoot', 'tbody', 'tr', 'th', 'td'
]



def clean_html_for_text(html_content, base_url=None):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove unnecessary tags

    for tag in tags_to_remove:
        for element in soup.find_all(tag):
            element.decompose()

    # Unwrap divs and spans but keep their content
    for tag in tags_to_unwrap:
        for element in soup.find_all(tag):
            element.unwrap()

    # Remove all attributes
    soup = remove_attributes(soup)


    # Optionally, resolve relative URLs in <a> tags if a base URL is provided
    # if base_url:
    #     for a in soup.find_all('a', href=True):
    #         a['href'] = urljoin(base_url, a['href'])

    # Normalize white spaces and clean text
    # cleaned_text = soup.get_text(separator=' ').strip()
    # cleaned_text = ' '.join(cleaned_text.split())  # Collapse multiple spaces

    return str(soup)


def remove_attributes(soup):
    # Iterate over all tags
    for tag in soup.find_all(True):
        # Clear all attributes for each tag
        tag.attrs = {}
    return soup

def extract_content_html2text(html_content):
    h = html2text.HTML2Text()
    h.ignore_links = True
    content = h.handle(html_content)
    return content