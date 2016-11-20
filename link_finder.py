from HTMLParser import HTMLParser
from urllib2 import urlparse

# Crawls webpage found at base_url for href links
class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        HTMLParser.__init__(self)
        self.base_url = base_url
        self.page_url = page_url
        self.links = set() # new empty set to store links of current page_url

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if (attribute == 'href'):
                    # if not full url, convert relative url to full url 
                    url = urlparse.urljoin(self.base_url, value)
                    self.links.add(url)
                    
    def page_links(self):
        return self.links
                
    def error(self, message):
        pass
