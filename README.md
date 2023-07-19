# BA-Internship
This prototype is a basic Python tool for extracting URLs recursively from a website, starting with the given URL. It uses the `requests` library to fetch the HTML content of web pages and the `BeautifulSoup` library to parse the HTML and find all anchor tags with `href` attributes, representing the URLs. 

The function `extract_urls_recursively` takes the initial URL and a set of visited URLs (to avoid revisiting the same URLs) as input. It makes HTTP requests, processes the HTML content, and extracts the URLs from the anchor tags. It then recursively calls itself for each extracted URL to crawl through sub-pages and continue extracting URLs.

This prototype provides a starting point for building a more comprehensive web crawler or URL extraction tool, and it can be further enhanced to handle different link formats, avoid crawling external websites, or perform additional data processing on the extracted URLs.
