import pandas as pd
df = pd.read_csv('Wikilinks2019-06-11T16-23-19.csv', usecols=['link'])
urls = []
for x in df['link']:
    urls.append('https://en.wikipedia.org/' + x)
print(urls)