import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
data = {
    'cate': 'realtimehot'
}

try:
    r = requests.get('http://s.weibo.com/top/summary?', params=data, headers=headers)
    print(r.url)
    if r.status_code == 200:
        html = r.text
    else:
        html = ""
except():
    html = ""

soup = BeautifulSoup(html, 'lxml')

sc = soup.find_all('tr', attrs={'class': ''})

for main_data in sc:
    q = str(main_data).split("td")[5]
    q = q.split(">")[2].split("<")[0]
    print(q)
