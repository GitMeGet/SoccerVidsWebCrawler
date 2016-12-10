import threading
from domain import *
from shared import *
from spider import *
import webbrowser
import os
import random
from url import Url

PROJECT_NAME = 'timesoccer'
HOME_PAGE = 'http://www.timesoccer.com/'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8 # depends on OS 

Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)

if len(Spider.queue) > 0:
    #current_video = Spider.queue[random.randint(0,len(Spider.queue) - 1)]
    current_video = Spider.queue.pop(0)
    Spider.queue.append(current_video)
    video_files = os.listdir(Shared.videos_folder)
    parsed = current_video.parse_html()
    for video in video_files:      
        if (parsed in video.lower()):          
            print("Enjoy the video")
            os.startfile(os.getcwd() + '\\timesoccer\\videos\\' + video)        
            current_video.status = 'watched'
            break          
    if (current_video.status != 'watched'):
        print("Sorry, video hasn't been downloaded")  
else:
    print("Sorry no more videos")

Spider.update_files()
Spider.download_mp4()
