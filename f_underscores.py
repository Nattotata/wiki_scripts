import os
import re

# change underscores to hyphen in filenames

directory_str = input('choose directory:\n')
directory = os.fsencode(directory_str)

# change filenames in assets folder
for path, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith(b'.md'):
            continue
        if filename.find(b'_') != -1:
            filename_new = filename.replace(b'_', b'-')
            filename_path_old = os.path.join(path, filename)
            filename_path_new = os.path.join(path, filename_new)
            try:
                os.rename(filename_path_old, filename_path_new)
                print(f"{filename} renamed to {filename_new}\n")
            except:
                print('spam')
    for dirname in dirnames:
        if dirname.find(b'_') != -1:
            dirname_new = dirname.replace(b'_', b'-')
            dirname_path_old = os.path.join(path, dirname)
            dirname_path_new = os.path.join(path, dirname_new)
            print(f'renaming {dirname_path_old} to {dirname_path_new}')
            os.rename(dirname_path_old, dirname_path_new)