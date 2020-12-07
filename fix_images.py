import os
import re

# Looks at src path in images and the folder structure
# Then adjusts the src to reflect the folder structure
# example for file  `![alt](foo/bar/spam.png)`
# the output would be `![alt](../../spam.png)`

def generate_path(path):
    path = path.replace(b'\\', b'/')
    print(f"gen: path: {path}\n")
    dirs = re.split('/', str(path))
    print(f"gen: path(str): {path}\ndirs: {dirs}\n")
    path_new = ''
    dirs.pop(0)
    for i in range(len(dirs)):
        dirs[i] = '..'
    print(f"gen: dirs: {dirs}")
    path_new = '/'.join(dirs)
    print(f"gen: path_new: {path_new}")
    path_new = path_new.replace('\'', '')
    return path_new

directory_str = input("Which directory to check? \n")
directory = os.fsencode(directory_str)

for path, dirname, filenames in os.walk(directory):
    for filename in filenames:
        filename_path = os.path.join(path, filename)
        #print(f"filename_path: {filename_path}\npath: {path}\ndirectory: {dirname}\nfilename: {filename}")

        if (not filename.endswith(b".md")) and (not filename.endswith(b".MD")):
            continue

        markdownFile = open(filename_path, 'r', encoding='latin1')
        cont = markdownFile.read()
        markdownFile.close()

        link_pattern = r'\[.*\]\((?P<path>assets.*?)\)'
        links = re.findall(link_pattern, cont)
        for link in links:
            file_path = generate_path(path)
            print(f"link: {link}\n file_path: {file_path}")
            new_path = os.path.join(file_path, link)
            print(f"new path: {new_path}")
        #link_obj = re.search(link_pattern, cont)
        #if link_obj == None:
        #    continue
        #link_path = link_obj.group('path')
        #file_path = generate_path(path)
        #print(file_path)
        #new_path = os.path.join(file_path, link_path)
            cont = cont.replace(link, new_path)
        #print(f'new path {new_path}')
        
        filename = open(filename_path, 'w', encoding='latin1')
        filename.write(cont)
        filename.close()

