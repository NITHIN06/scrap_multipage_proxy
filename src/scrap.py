from bs4 import BeautifulSoup
import requests
import pandas as pd
import json


api_key = "API_KEY"
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Accept-Language':'en-US, en;q=0.5', 
            "Authorization": f"Bearer {api_key}"
            })


# HEADERS = {"Authorization": f"Bearer {api_key}"}


def get_content(url):
    print(url)
    site = requests.get(url, headers=HEADERS)
    # site = client.get(url)
    soup = BeautifulSoup(site.content, "html.parser")

    links = soup.find_all("a", {"jscontroller":"M9mgyc"}, class_=False)
    names = soup.select('h3.LC20lb')
    # print(soup)

    links = [link['href'] for link in links]
    link = ''
    if link=='':
        for i in links:
            if 'channel' in i or f"youtube.com/{txt.split()[-1]}" in i:
                link = i
    print(link)

    next_url = soup.find('a', {"id":"pnnext"})
    return ({"names": [name.text for name in names], "links": links}, next_url, link)

df = {"names": [], "links": [], "channel": ''}

# txt = "youtube.com openinapp.co"
txt = "youtube openinapp"
url = 'https://google.com/search?q=' + txt
pre_link = 'https://google.com/'
print(url)

next_url = 'none'
link = ''
while len(df['links'])<10000 or next_url:
    curr_df, next_url, link = get_content(url)
    df['links'].extend(curr_df['links'])
    df['names'].extend(curr_df['names'])
    if next_url:
        url = pre_link+next_url['href']
    # print(df.shape[0])

df['channel'] = link
print(df)
df['links'] = df['links'][:10000]
df['names'] = df['names'][:10000]
json_object = json.dumps(df, indent=4)
 
# Writing to sample.json
with open("../records.json", "w") as outfile:
    outfile.write(json_object)