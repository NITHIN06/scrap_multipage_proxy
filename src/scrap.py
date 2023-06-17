from bs4 import BeautifulSoup
import requests
import pandas as pd

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Accept-Language':'en-US, en;q=0.5'})

def get_content(url):
    print(url)
    site = requests.get(url,  headers=HEADERS)
    soup = BeautifulSoup(site.text, "html.parser")

    links = soup.find_all("a", {"jscontroller":"M9mgyc"}, class_=False)
    names = soup.select('h3.LC20lb')

    next_url = soup.find('a', {"id":"pnnext"})
    return (pd.DataFrame({"names": [name.text for name in names], "links": [link['href'] for link in links]}), next_url)

df = pd.DataFrame(columns=['names', 'links'])

txt = input()
url = 'https://google.com/search?q=' + txt
pre_link = 'https://google.com/'
print(url)

next_url = 'none'
while df.shape[0]<100 or next_url:
    curr_df, next_url = get_content(url)
    df = pd.concat([df, curr_df], axis=0)
    if next_url:
        url = pre_link+next_url['href']
    print(df.shape[0])

print(df.head())