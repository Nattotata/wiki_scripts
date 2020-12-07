import os
import re

# Regex pattern and flag
# test in https://regexr.com/
directory_str = input("Which directory to check? \n")
directory = os.fsencode(directory_str)

# centered text pattern
# pattern = r'(?P<start><div class ?= ?"centeredText" ?>)(:?.+?)(?P<end><\/div>)'

# warning callout pattern
# pattern = r'(?P<first><div class ?= ?"warning" ?>)(:?.+?)(?P<second><\/div>)'
# replacement_first = '<Callout icon type="warning" title="This is a warning callout.">\n'
# replacement_second = '</Callout>'

# replacing <strong> with **
# pattern = r'(?P<first><strong>)(:?.+?)(?P<second><\/strong>)'
# replacement_first = '**'
# replacement_second = '**'

# replacing tip with default callout
# pattern = r'(?P<first><div class ?= ?"tip" ?>)(:?.+?)(?P<second><\/div>)'
# replacement_first = '<Callout icon>\n'
# replacement_second = '</Callout>'

# replace <em> with *
# pattern = r'(?P<first><em>)(:?.+?)(?P<second><\/em>)'
# replacement_first = '*'
# replacement_second = '*'

# replace underscores in links with hyphens
# pattern = r'!\[.+\)'

pattern = r'<div.+<\/div>'
pattern_src = r'src=".+?"'
pattern_id = r'id=".+?"'
pattern_img = r'!\[.*\]\((?P<path>.+\))'

def write_to_file(path, content):
    article = open(path, "w", encoding="utf8")
    article.write(content)
    article.close()
            
def read_from_file(path):
        article = open(path, "r", encoding='utf-8')
        content = article.read()
        article.close()
        return content

for path, dirname, filenames in os.walk(directory):
    for filename in filenames:
        filename_path = os.path.join(path, filename)
        if (not filename.endswith(b".md")) and (not filename.endswith(b".MD")):
            continue
        content = read_from_file(filename_path)
        # check flag
        # flags=re.DOTALL
        found_array = re.finditer(pattern_img, content)
        for found_item in found_array:
            # this part varies
            found_str = found_item.group('path')
            if (found_str.find('_') != -1):
                new_str = found_str.replace('_', '-')
                print(f'replacing: {found_str} with {new_str}\n')
                content = content.replace(found_str, new_str)
                write_to_file(filename_path, content)
            #if found_str.find('lucidchart') != -1:
            #    lucid_src = re.search(pattern_src, found_str)
            #    lucid_id = re.search(pattern_id, found_str)
            #    lucid_output = f'<Lucidchart {lucid_id.group(0)} {lucid_src.group(0)} />'
            #    print(f"replacing: {found_str}\n with: {lucid_output}\n")
            #    content = content.replace(found_str, lucid_output)
            #content = content.replace(str(found_item.group('first')), replacement_first)
            #content = content.replace(str(found_item.group('second')), replacement_second)
        #write_to_file(filename_path, content)
