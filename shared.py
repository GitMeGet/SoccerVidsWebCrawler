import os
import requests
import glob, os, shutil
import pickle

class Shared:

    queue_file = '' 
    crawled_file = ''
    video_folder = ''

    def __init__(self, project_name, base_url):
        Shared.queue_file = project_name + '/queue.txt'
        Shared.crawled_file = project_name + '/crawled.txt'
        Shared.videos_folder = project_name + '/videos'
        self.create_project_dir(project_name)
        self.create_data_files(project_name, base_url)
     
    # Each website crawled is a separate project (folder)
    @staticmethod  
    def create_project_dir(directory):
        if not os.path.exists(directory):
            print("Creating project: " + directory)
            os.makedirs(directory)
     
    # Create queue and crawled files (if not created)
    @staticmethod
    def create_data_files(project_name, base_url):      
        if not os.path.isfile(Shared.queue_file):
            Shared.write_file(Shared.queue_file, '')
        if not os.path.isfile(Shared.crawled_file):
            Shared.write_file(Shared.crawled_file, '')
        if not os.path.exists(Shared.videos_folder):
            os.makedirs(Shared.videos_folder)

    # Create a new file
    @staticmethod
    def write_file(path, data):
        # creates file handle to 'path' in write mode 
        f = open(path, 'w')
        f.write(data)
        f.close()

    # set: no duplicates ; list: can have duplicates

    # Read a file and convert each line into list items
    @staticmethod
    def file_to_list(file_name):
        with open(file_name,'rb') as rfp:
            try:
                data = pickle.load(rfp)
                return data
            except EOFError :
                return list()
            except KeyError :
                return list()

    # Convert items in a list to save in a file
    @staticmethod
    def list_to_file(links, file):
        with open(file,'wb') as wfp:
            pickle.dump(links, wfp)        

    @staticmethod        
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

    @staticmethod
    def move_mp4(source_dir, dest_dir):
        files = glob.iglob(os.path.join(source_dir, "*.mp4"))
        for file in files:
            if os.path.isfile(file):
                if file not in dest_dir:
                    shutil.move(file, dest_dir)

    





