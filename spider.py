from urllib2 import urlopen
from link_finder import LinkFinder
from shared import *
import webbrowser
import os
from url import Url
import thread

# Goes to a webpage and parses html code
class Spider:

    # Class variables (shared among all instances)
    project_name = ''
    base_url = '' # homepage url
    domain_name = '' # ensure connected to valid webpage
    queue = list()
    crawled = list()
    
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Shared(project_name, base_url) # create dir + files if not created
        self.boot()
        self.crawl_page('Main Highlights', Spider.base_url)
        
    @staticmethod
    def boot():     
        Spider.queue = Shared.file_to_list(Shared.queue_file)
        Spider.crawled = Shared.file_to_list(Shared.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        # if page_url in Spider.crawled
        print(thread_name + ' now crawling ' + page_url)
        print('Queue ' + str(len(Spider.queue))
              + ' | Crawled ' + str(len(Spider.crawled)))
        Spider.add_links_to_queue(Spider.gather_links(page_url))
        Spider.crawled.append(page_url)
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
            print(e)
            return list()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for link in links:
            print(link)
            for url in Spider.queue:
                if link == url.url:
                    print('continued')
                    continue                   
            if Spider.domain_name not in link: # only crawl specified site  
                continue
            if 'video' in link:
                Spider.queue.append(Url(link))
                print('link added: ' + link)
                
    @staticmethod
    def download_mp4():
        dl = 0
        for url in Spider.queue:
            print(url.status)
            if url.status == 'none':
                dl = 1
                url.youtube_dl()
                Spider.update_files()
                Shared.move_mp4(os.getcwd(), os.getcwd() + '\\timesoccer\\videos\\')
                #thread.start_new_thread(url.youtube_dl, ())
        if dl == 0:
            print("No videos to download")
    
    @staticmethod
    def update_files():
        Shared.list_to_file(Spider.queue, Shared.queue_file)
        Shared.list_to_file(Spider.crawled, Shared.crawled_file)


            




                  
