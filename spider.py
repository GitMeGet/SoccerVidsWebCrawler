from urllib2 import urlopen
from link_finder import LinkFinder
from general import *
import webbrowser

# Goes to a webpage and parses html code
class Spider:

    # Class variables (shared among all instances)
    project_name = ''
    base_url = '' # homepage url
    domain_name = '' # ensure connected to valid webpage
    queue_file = '' 
    crawled_file = ''
    watched_file = ''
    queue = set()
    crawled = set()
    watched = set()
    
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.watched_file = Spider.project_name + '/watched.txt'
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)
        

    # First Spider creates project dir and data files (Q & crawled.txt)
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
        Spider.watched = file_to_set(Spider.watched_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue))
                  + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.info().gettype() == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except IOError, e:
            print('Error: cannot crawl page')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if url in Spider.watched:
                continue
            if Spider.domain_name not in url: # only crawl specified site  
                continue
            if 'video' in url:
                Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
        set_to_file(Spider.watched, Spider.watched_file)







            




                  