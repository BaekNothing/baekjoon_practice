import urllib.request  
from bs4 import BeautifulSoup  
  
url = 'https://neolook.com/archives/19920505a'
  
conn = urllib.request.urlopen(url)
soup = BeautifulSoup(conn, "html.parser")  
arta = soup.find_all('div', class_='archives-description')

filteredText = url + '\n'
for art in arta:
    filteredText += art.text.strip()
filteredText = filteredText.replace(',', '')
filteredText = filteredText.replace('\n\n\n', ',    ')

with open('output.txt', 'wt', encoding='utf8') as f:
    f.write(str(filteredText))
#출처: https://crazyj.tistory.com/190 [크레이지J의 탐구생활:티스토리]