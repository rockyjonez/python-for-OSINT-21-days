# Script to download PDF files from DuckDuckGo search results.
# Can be used to download other kinds of files, as well, with modification.
# Creates a directory in this working directory called 'downloads' to store the downloaded files.
# Provides a count of how many files of that type were downloaded.

import os
import requests
from duckduckgo_search import DDGS

def download_pdf(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            file.write(response.content)
            print(f"Successfully downloaded: {filename}")
            return True
    except requests.RequestException as e:
        print(f"Error downloading {filename}: {e}")
        return False

def sanitize_filename(filename):
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c in (' ', '-', '_')]).rstrip()

# Create a directory to store the downloaded PDFs
download_dir = "C:\\Users\\gener\\Documents\\development\\python-for-OSINT-21-days\\Day_9\\downloads"
os.makedirs(download_dir, exist_ok=True)

keywords = 'osint filetype:pdf'
max_results = 10
results = DDGS().text(keywords, region='us-en', safesearch='off', timelimit='y', max_results=max_results)

downloaded_count = 0
for result in results:
    title = result['title']
    url = result['href']

    # Check if the URL ends with .pdf
    #if url.lower().endswith('.pdf'):
    # Create a sanitized filename from the title
    filename = sanitize_filename(title)
    filename = filename.lower()
    if not filename.endswith('.pdf'):
        filename += '.pdf'

    # Full path for saving the file
    filepath = os.path.join(download_dir, filename)

    # Download and save the PDF
    if download_pdf(url, filepath):
        downloaded_count += 1

    # Break the loop if we've downloaded the maximum number of files
    if downloaded_count >= max_results:
        break

print(f"Total PDFs downloaded: {downloaded_count}")