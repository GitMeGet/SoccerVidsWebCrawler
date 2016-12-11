from youtube_dl import YoutubeDL
import re

class Url:

    common_video_path = 'C:/Users/Yu Peng/Desktop/LearnPythonTheHardWay/timesoccer/videos/'

    def __init__(self, url):
        self.status = 'none'
        self.url = url
        self.video_path = ''

    def youtube_dl(self):
        ydl_opts = {
            'outtmpl': Url.common_video_path + '%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
            info_dict = ydl.extract_info(self.url, download=False)
            video_title = info_dict.get('title', None)
            video_extension = info_dict.get('ext', None)
            self.video_path = Url.common_video_path + video_title + '.' + video_extension
        status = 'downloaded'
        
    def parse_html(self):
        m = re.search(r'(\w+)-vs-(\w+)',self.url)
        
        return (m.group(2) + ' vs ' + m.group(1)).lower()
        
