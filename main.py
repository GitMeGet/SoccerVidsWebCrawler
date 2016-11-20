import threading
from Queue import Queue
from spider import Spider
from domain import *
from general import *
import webbrowser

PROJECT_NAME = 'timesoccer'
HOME_PAGE = 'http://www.timesoccer.com/football-highlights'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8 # depends on OS 

# Thread queue
queue = Queue()

Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)

if len(Spider.queue) > 0:
    current_video = Spider.queue.pop()
    webbrowser.open_new(current_video)
    Spider.watched.add(current_video)
    Spider.update_files()
