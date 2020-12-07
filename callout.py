import os
import re

# change md > into callout objects
# Example input:
# > Egg
# > Egg and bacon
# > Egg and spam
#
# Example output:
# <Callout>
# Egg
# Egg and bacon
# Egg and spam
# </Callout> 

pattern = r'^>.*'
directory_str = input('Choose directory: \n')
directory = os.fsencode(directory_str)

for path, dirname, filenames in os.walk(directory):
    for filename in filenames:
        filename_path = os.path.join(path, filename)
        if (not filename.endswith(b'.md')) and (not filename.endswith(b'.MD')):
            continue
        article = open(filename_path, 'r', encoding='utf-8')
        content = article.read()
        article.close()
        article = open(filename_path, 'r', encoding='utf-8')
        content_lines = article.readlines()
        article.close()
        match_conc = ""
        found_match = 0
        callout = ""

        for line in content_lines:
            match = re.search(pattern, line)
            if match != None:
                match_new = match.string.replace('> ', '')
                callout = f'{callout}{match_new}'
                match_conc = match_conc + match.string
                found_match = 1
            if match == None:
                if found_match == 1:
                    callout = f'<Callout>\n\n{callout}</Callout>\n'
                    print(f'replacing: \n{match_conc}\n with:\n{callout}\n')
                    content = content.replace(match_conc, callout)
                    article = open(filename_path, 'w', encoding='utf-8')
                    article.write(content)
                    article.close()
                    found_match = 0
                    match_conc = ""
                    callout = ""
