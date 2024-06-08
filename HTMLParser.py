from urllib.request import urlopen
from html.parser import HTMLParser
from urllib.parse import urljoin

#url = 'http://facweb.cdm.depaul.edu/asettle/web/test.html'
#html = urlopen(url).read().decode()

class MyHtmlParser(HTMLParser):
    '''basic html parser'''

    def handle_starttag(self, tag, attrs):
        '''prints tags'''
        print(f"Encountered starting {tag} tag, with {len(attrs)} attributes")

    def handle_endtag(self, tag):
        '''prints end tag'''
        print(f"Encountered ending {tag} tag")

class ParserPracticeBase(HTMLParser):
    '''adds url handling capability to HTMLParser'''

    def parse(self, url):
        '''open URL and feed contents to HTMLParser'''
        html = urlopen(url).read().decode()
        self.feed(html)  

class AttributesParser(ParserPracticeBase):
    '''parses attributes into key-value pairs'''   

    def handle_starttag(self, tag, attrs):
        '''print attributes for <a> tags'''
        if tag == 'a':  # if the tag is an anchor tag
            print(attrs)  # print the attributes       

class LinksParser(ParserPracticeBase):
    '''prints links to screen'''

    def handle_starttag(self, tag, attrs):
        '''prints href values to screen'''
        if tag == 'a':  # if the tag is an anchor tag
            for name, link in attrs:  # for each attribute in the tag
                if name == 'href':  # if the attribute is 'href'
                    print(link)  # print the link

class PrettyParser(ParserPracticeBase):
    '''pretty prints html'''

    def __init__(self):
        '''constructor'''
        super().__init__()
        self.indent = 0

    def handle_starttag(self, tag, attrs):
        '''prints start tag at correct indent level'''
        if tag not in ('img', 'br', 'hr'):  # if the tag is not an image, line break, or horizontal rule
            print(' ' * self.indent + f'<{tag}>')  # print the tag with the correct indent level
            self.indent += 4  # increase the indent level by 4

    def handle_endtag(self, tag):
        '''prints end tag at correct indent level'''
        self.indent -= 4  # decrease the indent level by 4
        print(' ' * self.indent + f'</{tag}>')  # print the tag with the correct indent level

    def handle_data(self, data):
        '''prints data at correct indent level'''
        print(' ' * self.indent + data)  # print the data with the correct indent level

class DataCollector(ParserPracticeBase):
    '''create string of inner data'''

    def __init__(self):
        '''constructor'''
        super().__init__()
        self.data = ''

    def handle_data(self, data):
        '''collects data into string'''
        self.data += data

    def get_data(self):
        '''return data collected from html'''
        return self.data   

class HeaderParser(ParserPracticeBase):
    '''prints header tags to screen'''

    def handle_starttag(self, tag, attrs):
        '''prints header tags to screen'''
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):  # if the tag is a header tag
            print(tag)  # print the tag

    def handle_data(self, data):
        '''prints header data to screen'''
        print(data)  # print the data   

    def get_list(self):
        '''return list of header data'''
        return self.headerlist

class ListParser(ParserPracticeBase):
    '''create a list of list items'''
    
    def __init__(self):
        '''constructor'''
        super().__init__()
        self.flag = False
        self.li_list = []

    def handle_starttag(self, tag, attrs):
        '''set flag when li tag is encountered'''
        if tag == 'li':
            self.flag = True

    def handle_endtag(self, tag):
        '''unsets flag when li end tag encountered'''
        if tag == 'li':
            self.flag = False

    def handle_data(self, data):
        '''add data for li tags to list'''
        if self.flag == True:
            self.li_list.append(data)

    def set_list(self, lst):
        '''sets self.list'''
        self.li_list = lst

    def get_list(self):
        '''returns self.list'''
        return self.li_list
    
class Collector(HTMLParser):
    '''collect HTTP links'''

    def __init__(self):
        '''constructor'''
        super().__init__()
        self.linklist = []
        self.url = ''

    def parse(self, url):
        '''run the parser'''
        self.url = url
        html = urlopen(url).read().decode()
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        '''adds absolute URLs to linklist'''
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    absolute = urljoin(self.url, value)
                    if absolute[:4] == 'http':
                        self.linklist.append(absolute)

    def get_links(self):
        '''returns links'''
        return self.linklist    