import requests
import bs4

res = requests.get('http://www.example.com')

type(res)

print(res.text)

soup = bs4.BeautifulSoup(res.text, 'lxml')

title_tag_list = soup.select('title')