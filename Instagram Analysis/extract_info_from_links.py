from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas as pd, numpy as np
from bs4 import BeautifulSoup as bs

with open("epam.txt", 'r') as f:
    links = f.readlines()

result = pd.DataFrame()
for i in range(len(links)):
    try:
        page = urlopen(links[i]).read()
        data = bs(page, 'html.parser')
        body = data.find('body')
        script = body.find('script')
        raw = script.text.strip().replace('window._sharedData =', '').replace(';', '')
        json_data = json.loads(raw)
        posts = json_data['entry_data']['PostPage'][0]['graphql']
        posts = json.dumps(posts)
        posts = json.loads(posts)
        x = pd.DataFrame.from_dict(json_normalize(posts), orient='columns')
        x.columns = x.columns.str.replace("shortcode_media.", "")
        result = result.append(x)

    except:
        np.nan

result = result.drop_duplicates(subset='shortcode')
result.index = range(len(result.index))