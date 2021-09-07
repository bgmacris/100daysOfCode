import os
# import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# https://www2.animeflv.to/ver/boku-no-hero-academia-2016-4
url = "https://www2.animeflv.to/ver/boku-no-hero-academia-2016-4"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
html = web_byte.decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
find_iframes = soup.find_all("div", {"class": "Wrapper"})
find_iframes = soup.find_all("div", {"class": "Body"})
find_iframes = soup.find_all("div", {"class": "Container"})
find_iframes = soup.find_all("div", {"class": "CpCn ClFx"})
find_iframes = soup.find_all("div", {"class": "CpCnA"})
find_iframes = soup.find_all("div", {"class": "CapiTcn tab-content"})
find_iframes = soup.find_all("div", {"class": "tab-pane active"})
find_iframes = soup.find_all("div", {"class": "load-video"})

for iframes in find_iframes:
    for iframe in iframes:
        video = f"http:{iframe.attrs['src']}"
        
req = Request(video, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
html = web_byte.decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
find_video = soup.find_all("div", {"class": "wrapper"})
find_video = soup.find_all(class_="videocontent")
# find_video = soup.find_all(class_="jw-video jw-reset")

print(find_video)
