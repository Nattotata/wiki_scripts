import os

## Replace <br> with two spaces (or </br>)

directory_str = input("Which directory to check? \n")
directory = os.fsencode(directory_str)

for path, dirname, filenames in os.walk(directory):
    for filename in filenames:
        filename_path = os.path.join(path, filename)

        if (not filename.endswith(b".md")) and (not filename.endswith(b".MD")):
            continue

        article = open(filename_path, "r", encoding="utf8")
        content = article.read()
        content = content.replace("<br>", "  ")
        article.close()
        article = open(filename_path, "w", encoding="utf8")
        article.write(content)
