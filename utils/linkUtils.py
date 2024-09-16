from urllib.parse import urlparse, urljoin


def get_base_url(url):
    # Parse the URL into components
    parsed_url = urlparse(url)
    
    # Extract the base URL (scheme + netloc)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    
    return base_url

def resolve_relative_urls(base_url, relative_urls):
    absolute_urls = [urljoin(base_url, rel_url) for rel_url in relative_urls]
    return absolute_urls

def clean_and_classify_links(links, base_url):
    absolute_links = set()
    resolved_relative_links = set()
    ignored_links = set()

    for link in links:
        link = link.strip().lower()  # Strip and convert to lowercase
        parsed_link = urlparse(link)

        # Ignore JavaScript links (e.g., "javascript:void(0);") and same-page links (e.g., "#top")
        if link.startswith('javascript') or parsed_link.fragment:
            ignored_links.add(link)
            continue

        # If it's a protocol-relative link (e.g., "//example.com")
        if link.startswith('//'):
            cleaned_link = 'https:' + link.rstrip('/')
            absolute_links.add(cleaned_link)

        # If it's an absolute link (e.g., "https://example.com")
        elif parsed_link.scheme in ['https']:
            cleaned_link = link.rstrip('/')
            absolute_links.add(cleaned_link)

        # If it's a relative link (e.g., "/docs/tutorial")
        elif link.startswith('/'):
            cleaned_link = urljoin(base_url, link).rstrip('/')
            resolved_relative_links.add(cleaned_link)

        # If it's a same-page link (e.g., "#section") or something else
        else:
            ignored_links.add(link)

    # # Remove duplicates by converting to sets and write to files
    # with open(external_file, 'w') as ext_f:
    #     for link in sorted(absolute_links):
    #         ext_f.write(link + '\n')

    # with open(relative_file, 'w') as rel_f:
    #     for link in sorted(resolved_relative_links):
    #         rel_f.write(link + '\n')

    # with open(ignore_file, 'w') as ign_f:
    #     for link in sorted(ignored_links):
    #         ign_f.write(link + '\n')
    return absolute_links, resolved_relative_links, ignored_links