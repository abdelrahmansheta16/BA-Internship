import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_urls_recursively(url, visited_urls=set()):
    if url in visited_urls:
        return []

    visited_urls.add(url)

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        urls = set()

        for link in soup.find_all('a', href=True):
            href = link.get('href')
            absolute_url = urljoin(url, href)
            urls.add(absolute_url)

        sub_urls = []
        for sub_url in urls:
            sub_urls.extend(extract_urls_recursively(sub_url, visited_urls))

        return list(urls) + sub_urls

    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch {url} - {e}")
        return []

if __name__ == "__main__":
    # Replace with your desired website URL
    url = 'https://www.curlie.org/'

    urls = extract_urls_recursively(url)
    print('Extracted URLs:')
    for url in urls:
        print(url)
