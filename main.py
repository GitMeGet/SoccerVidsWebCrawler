import threading
from Queue import Queue
from spider import Spider
from domain import *
from general import *
import webbrowser
import os 

PROJECT_NAME = 'timesoccer'
HOME_PAGE = 'http://www.timesoccer.com/'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8 # depends on OS 

Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)

if len(Spider.queue) > 0:
    current_video = Spider.queue.pop()
    video_files = os.listdir(Spider.videos_folder)
    parsed = parse_html(current_video)
    found = 0
    for video in video_files:      
        if (parsed in video.lower()):          
            print("Enjoy the video")
            os.startfile(os.getcwd() + '\\timesoccer\\videos\\' + video)        
            Spider.watched.add(current_video)
            found = 1
            break          
    if (found == 0):
        Spider.queue.add(current_video)
        print("Sorry, video hasn't been downloaded")   
else:
    print("Sorry no more videos")

Spider.update_files()

# Spider.download_mp4()
