from bs4 import BeautifulSoup
import requests

# txt = input()
txt = 'openinapp.co'
url = 'https://google.com/search?q=' + txt
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Accept-Language':'en-US, en;q=0.5'})

site = requests.get(url,  headers=HEADERS)
print("Get...")

soup = BeautifulSoup(site.text, "html.parser")
print("Parse...")

links = soup.find_all("a", {"jscontroller":"M9mgyc"}, class_=False)
# names = soup.find_all('h3', class_="LC201b")
names = soup.select('h3.LC20lb')


# for i in links:
#     print(i['href'])
# # print(names)
# for i in names:
#     print(i)

# print(len(links), len(names))
pre_link = 'https://google.com/'
link = soup.find('a', {"id":"pnnext"})['href']
link = pre_link+link

site = requests.get(url,  headers=HEADERS)
soup = BeautifulSoup(site.text, "html.parser")

links = soup.find_all("a", {"jscontroller":"M9mgyc"}, class_=False)
names = soup.select('h3.LC20lb')

for i in links:
    print(i['href'])
# print(names)
for i in names:
    print(i)