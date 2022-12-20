import requests
import os
import bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    print(f"Downloading the page: {url}")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElement = soup.select('#comic img')
    if comicElement == []:
        print("No images found")
    else:
        comicUrl = f"https://{comicElement[0].get('src')}"
        print(f"Downloading image: {comicUrl}")
        res = requests.get(comicUrl)
        res.raise_for_status()
    
    imgFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imgFile.write(chunk)
    imgFile.close()
    
    prevLink = soup.select('a[rel="prev"]')[0]
    url = f"https://xkcd.com{prevLink.get('href')}"
    

print('Done...')