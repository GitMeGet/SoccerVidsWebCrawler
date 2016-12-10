from youtube_dl import YoutubeDL
import re

class Url:

    status = ''
    url = ''

    def __init__(self, url):
        self.status = 'none'
        self.url = url

    def youtube_dl(self):
        ydl_opts = {
            'output': 'C:/Users/Yu Peng/Desktop/LearnPythonTheHardWay'
        }
        with YoutubeDL(ydl_opts) as ydl:
            print('Downloading: ' + self.url)
            ydl.download([self.url])
        status = 'downloaded'
        print("Download done: " + self.url)

    def parse_html(self):
        m = re.search(r'(\w+)-vs-(\w+)',self.url)
        
        return (m.group(2) + ' vs ' + m.group(1)).lower()
        
