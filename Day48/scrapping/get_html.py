import requests
from bs4 import BeautifulSoup

#url = 'https://getbootstrap.com/docs/4.0/examples/sign-in/'
url = 'https://www.facebook.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
with open('page/index.html', 'w') as file:
	file.write(str(soup))
print(soup)
