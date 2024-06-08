from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

from solutions import Collector

class Crawler(object):
        
    def crawl(self, url):
        '''recursive web crawler that calls analyze() on each web page'''
        links = self.analyze(url)
        for link in links:
            try:
                self.crawl(link)
            except:
                pass

    def analyze(self, url):
        '''returns the list of URLs found in the page url'''
        print("Visiting", url)
        collector = Collector()
        collector.parse(url)
        urls = collector.get_links()
        return urls
