import os
import re

# The script changes relative path to images to root relative
# The script expects that all images are in the same folder
# The folder with images can have subfolders

directory_str = input("Which directory to check? \n")
directory = os.fsencode(directory_str)


for path, dirname, filenames in os.walk(directory):
    for filename in filenames:
        filename_path = os.path.join(path, filename)
        print(f"filename_path: {filename_path}\npath: {path}\ndirectory: {dirname}\nfilename: {filename}")

        if (not filename.endswith(b".md")) and (not filename.endswith(b".MD")):
            continue

        markdownFile = open(filename_path, 'r', encoding='latin1')
        cont = markdownFile.read()
        markdownFile.close()

        link_pattern = r'\[.*\]\((?P<path>assets.*?)\)'
        regex_pattern = r'\[.*\]\((?P<path>\.\.\/.*?)\)'
        links = re.findall(regex_pattern, cont)
        for link in links:
            print(f'link: {link}')
            link_array = link.split('/')
            link_root = ''
            for iteration, item in enumerate(link_array):
                print(f'link array {item}, ')
                if item == '..':
                    continue
                else:
                    link_root = link_root + '/' + item
            link_root = '/consumer-product' + link_root
            print(f'final: {link_root}')
            cont = cont.replace(link, link_root)
        filename = open(filename_path, 'w', encoding='latin1')
        filename.write(cont)
        filename.close()

