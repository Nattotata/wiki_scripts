# input: <div class="lucidchart"><iframe allowfullscreen frameborder="0" style="width:100%; height:720px" src="https://www.lucidchart.com/documents/embeddedchart/9d139e7f-df8a-47d7-9cea-df594dd8ec0e" id="83esIy9NlTrX"></iframe><a href="https://www.lucidchart.com/documents/view/9d139e7f-df8a-47d7-9cea-df594dd8ec0e" target="_blank"><center>diagram source</center></div>
# output: <Lucidchart id="25sBc7EM0uN8" src="https://www.lucidchart.com/documents/embeddedchart/2b68c544-af0b-4a7b-a42f-9f4032e89520" />

import os
import re


directory_str = input("Which directory to check? \n")
directory = os.fsencode(directory_str)

for path, dirname, filenames in os.walk(directory):
    for filename in filenames:
        filename_path = os.path.join(path, filename)
        if (not filename.endswith(b".md")) and (not filename.endswith(b".MD")):
            continue

        article = open(filename_path, "r", encoding='utf-8')
        content = article.read()
        article.close()

        # content_one_line = content.replace("\n", "")
        pattern_div = r'<div class ?= ?"lucidchart".*?<\/div>'
        pattern_url = r'(?:src ?= ?")(?P<url>\S+)(")'
        pattern_id = r'(?:id ?= ?")(?P<id>\S+)(")'

        lucid_divs = re.findall(pattern_div, content, flags=re.DOTALL)
        for lucid_div in lucid_divs:        
            lucid_url = re.search(pattern_url, lucid_div)
            lucid_id = re.search(pattern_id, lucid_div)

            if not lucid_id or not lucid_url:
                continue
            lucid_url = lucid_url.group('url')
            lucid_id = lucid_id.group('id')
            print(f"lucid_url: {lucid_url}\nlucid_id: {lucid_id}")
            lucid_url = lucid_url.replace("\"", "")
            lucid_id = lucid_id.replace("\"", "")
            lucid_output = f'<Lucidchart id="{lucid_id}" src="{lucid_url}" />'
            print(f"replacing: {lucid_div}\n with: {lucid_output}\n")
            content = content.replace(lucid_div, lucid_output)

            article = open(filename_path, "w", encoding="utf8")
            article.write(content)
            article.close()
            