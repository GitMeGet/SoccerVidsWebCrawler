from __future__ import unicode_literals
from url import Url
import os

url = Url('http://www.timesoccer.com/video/burnley-vs-bournemouth-live-streaming-highlights.html')

url.youtube_dl()

os.startfile(url.video_path) 
