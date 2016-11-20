import os

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
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isfile(watched):
        write_file(watched, '')

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
        










