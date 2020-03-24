import scrapy
from ..items import CrawlerItem
from bs4 import BeautifulSoup

class QuoteSpider(scrapy.Spider):
    name = 'corona'
    start_urls = [
        'https://www.theguardian.com/au'
    ]
    def parse(self, response):
        items = CrawlerItem()
        links = response.css("a.js-headline-text::attr(href)").extract()
        for link in links:
            yield response.follow(link, callback=lambda r: self.parse_beyond(r, items))

    def parse_beyond(self, response, items):
        label = response.css("span.label__link-wrapper")[0].extract()
        headline = response.css("h1.content__headline::text")[0].extract()
        if headline is None:
            headline = response.css("h1.content__headline--no-margin-bottom::text")[0].extract()
        if (label.find('Coronavirus') or label.find('coronavirus') or headline.find('Corona') or headline.find('corona') or headline.find('COVID'))  is not None:
            tree = BeautifulSoup(label, "lxml")
            label = tree.get_text()
            # print(label)
            items['label'] = label
            items['link'] = response.url
            items['headline'] = headline
            time = response.css("time.content__dateline-wpd")[0].extract()
            if time is not None:
                tree = BeautifulSoup(time, "lxml")
                time = tree.get_text()
                # print(time)
                items['time'] = time
            byline = response.css("p.byline")[0].extract()
            if byline is None :
                byline = response.css("span.content__headline--byline")[0].extract()
                if byline is not None :
                    tree = BeautifulSoup(byline, "lxml")
                    byline = tree.get_text()
                    # print(byline)
                    items['byline'] = byline
            else :
                tree = BeautifulSoup(byline, "lxml")
                byline = tree.get_text()
                # print(byline)
                items['byline'] = byline
            # print(items)
            yield items







# All done just host the csv file up and be done with it