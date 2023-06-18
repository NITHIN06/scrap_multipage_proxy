from bs4 import BeautifulSoup
import requests
import pandas as pd
import json


api_key = "4H7QVNWEUEZ6441Q9WNG4E0NM7SVQNVNO0FUXE4W0YTYP4CTYLZGYK6IU11MKNDMZKSJ8RGVVLDNY0K4"
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Accept-Language':'en-US, en;q=0.5', 
            "Authorization": f"Bearer {api_key}"
            })
channel = ''

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
    if df['channel']=='':
        for i in links:
            if 'channel' in i or f"youtube.com/{txt.split()[-1]}" in i:
                df['channel'] = i
    # print(link)

    next_url = soup.find('a', {"id":"pnnext"})
    return ({"names": [name.text for name in names], "links": links}, next_url)

df = {"names": [], "links": [], "channel": ''}

# txt = "youtube.com openinapp.co"
txt = "youtube.com openinapp"
url = 'https://google.com/search?q=' + txt
pre_link = 'https://google.com/'

# print(url)

next_url = 'none'
link = ''
while len(df['links'])<10000 or next_url:
    curr_df, next_url = get_content(url)
    df['links'].extend(curr_df['links'])
    df['names'].extend(curr_df['names'])
    if next_url:
        url = pre_link+next_url['href']
    else:
        break
    # break
    
    # print(df.shape[0])

# print(df)
df['links'] = df['links'][:10000]
df['names'] = df['names'][:10000]
json_object = json.dumps(df, indent=4)
 
# Writing to sample.json
with open("../records.json", "w") as outfile:
    outfile.write(json_object)

print(len(df['links']))