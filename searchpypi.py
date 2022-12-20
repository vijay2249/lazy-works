#! python3

import sys
import bs4
import requests
import webbrowser

print('Searching....')
link = f"https://duckduckgo.com/?q='https://pypi.org/search/?q='{''.join(sys.argv[1:])}"
res = requests.get(link)
# webbrowser.open(link)
print(sys.argv[1:], "\n\n")
print(res.text[:100], "\n\n")
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElements = soup.select('a[data-testid="result-title-a"]')
print(linkElements)
# linkElements = soup.select('.package-snippet')
numOpen = min(5, len(linkElements))
for i in range(numOpen):
  urlToOpen = 'https://pypi.org' + linkElements[i].get('href')
  webbrowser.open(urlToOpen)