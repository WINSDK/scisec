from bs4 import BeautifulSoup
import sys

# Read HTML data from stdin.
html_content = sys.stdin.read()

soup = BeautifulSoup(html_content, 'html.parser')
g_content_divs = soup.find_all(class_='g-content')

for div in g_content_divs:
    paragraphs = div.find_all('p')
    for p in paragraphs:
        print(p.get_text())
