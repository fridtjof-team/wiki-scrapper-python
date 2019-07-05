# wiki-scrapper-python
This scraper scraps wikipedia data and saves the response in json.
## Getting started
You can clone or download the project on your machine.
using git:
```
git clone https://github.com/fridtjof-team/wiki-scrapper-python.git
```
### Prerequisties
You will need a local development environment for [Python 3](https://www.python.org/download/releases/3.0/) and [scrapy](http://doc.scrapy.org/en/1.1/intro/overview.html) installed.

### How to run the spiders
Thier are two spiders in the project, [First spider](https://github.com/fridtjof-team/wiki-scrapper-python/blob/master/spiders/wikipedia_visa.py) will give you a csv file containing all the country name and link.
And the [second spider](https://github.com/fridtjof-team/wiki-scrapper-python/blob/master/spiders/wikipedia_country.py) will use that csv file and crawl all the links.
Here how you run the spiders
```
$ scrapy crawl wikipedia_visa
```
this will generate a csv, copy the name and modify it in the second spider.
```
df = pd.read_csv('paste the name here', usecols=['link'])
```
Now run the second spider
```
$ scrapy crawl wikipedia_country
```
this will generate a json file in the current directory.

## Built with
[Python 3](https://www.python.org/) - Programming language.
[Scrapy](https://scrapy.org/) - Framework for extracting the data and saving it.
[Pandas](https://pandas.pydata.org/) - Parsing the CSV

## Authors
* **Ayush Gupta** - *Initial work* [MrAyush](https://github.com/MrAyush)
See also the list of [contributors](https://github.com/fridtjof-team/wiki-scrapper-python/graphs/contributors)
