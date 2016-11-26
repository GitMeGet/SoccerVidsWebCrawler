from __future__ import unicode_literals
import os
import requests
from youtube_dl import YoutubeDL
import glob, os, shutil
import re

# Each website crawled is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project: " + directory)
        os.makedirs(directory)

# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    watched = project_name + '/watched.txt'
    videos = project_name + '/videos'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isfile(watched):
        write_file(watched, '')
    if not os.path.exists(videos):
        os.makedirs(videos)

# Create a new file
def write_file(path, data):
    # creates file handle to 'path' in write mode 
    f = open(path, 'w')
    f.write(data)
    f.close()

# Append to existing file 
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        
# Delete contents of a file
def delete_file_contents(path):
    # overwrites file at path w/ new empty file 
    with open(path, 'w'):
        pass # do nothing

# set: no duplicates ; list: can have duplicates

# Read a file and convert each line into set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', '')) # remove newline char
    return results

# Convert items in a set to save in a file
# Iterate thru' set. Each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
        
def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

def youtube_dl(url):
    ydl_opts = {
        'output': 'C:/Users/Yu Peng/Desktop/LearnPythonTheHardWay'
    }
    with YoutubeDL(ydl_opts) as ydl:
        print('Downloading: ' + url)
        ydl.download([url])

def move_mp4(source_dir, dest_dir):
    files = glob.iglob(os.path.join(source_dir, "*.mp4"))
    for file in files:
        if os.path.isfile(file):
            shutil.move(file, dest_dir)
        
def parse_html(url):
    m = re.search(r'(\w+)-vs-(\w+)',url)
    
    return (m.group(2) + ' vs ' + m.group(1)).lower()







