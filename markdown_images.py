import os


# Markdown images
# Replace HTML <img> tags in .md files with md syntax

directory_str = input("Which directory to check? \n")
directory = os.fsencode(directory_str)

for path, dirname, filenames in os.walk(directory): 
    for filename in filenames:
        filename_path = os.path.join(path, filename)
        #print(f"filename_path: {filename_path}")

        if (not filename.endswith(b".md")) and (not filename.endswith(b".MD")):
            continue

        markdownFile = open(filename_path, 'r', encoding='UTF-8')
        cont = markdownFile.read()
        markdownFile.close()

# <img src="/frontend/wiki/docs/assets/boo_servicePackages-pricebox.png" alt="MMP Light - Price" style="height:20em; width: auto;">
# ![alt](link)
        for iteration in range(cont.count("<img")):

            img_start = cont.find("<img")
            img_path_start=cont.find("src=\"", img_start) + 5
            img_path_end=cont.find("\"", img_path_start)
            img_path=cont[img_path_start:img_path_end]

            img_end=cont.find(">", img_path_start)
            img_html=cont[img_start:img_end+1]
            
            img_alt = ""

            if img_html.find("alt") != -1:
                img_alt_start = cont.find("alt=\"", img_path_end) + 5
                img_alt_end = cont.find("\"", img_alt_start)
                img_alt = cont[img_alt_start:img_alt_end]

            img_md = f"![{img_alt}]({img_path})"

            print(f"Found an image in {filename}. \nPath: {img_path} \nAlt: {img_alt}\nChanging to {img_md}\n\n")

            cont = cont.replace(img_html, img_md, 1)

        filename = open(filename_path, 'w', encoding='UTF-8')
        filename.write(cont)
