# scrap_multipage_proxy
Web scrapping assignment including proxy server

## Requirements
To install all dependencies, use the requirements.txt
use below cmd to install
```
pip install -r requirements.txt
```

scrap.py named python script in src folder, contains whole code
change the api_key in line 7 to your own key

after running script a JSON file named "records.json" will created
it contains names and links for 10000 google search resuts and youtube channel name
format:
```
{
    "names": [
        "OpeninApp | Homepage",
        "OpeninApp | Youtube",
        .
        .
        .
        .
    ],
    "links": [
        "https://openinapp.com/",
        "https://openinapp.com/youtube",
        .
        .
        .
        .
    ],
    "channel": "https://www.youtube.com/channel/UCIGDcUqL2kKMdJCpIr_dfxg"
}
```
