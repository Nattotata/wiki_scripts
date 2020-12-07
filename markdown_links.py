import os


#Linquisition
#Replace HTML links in .md files in a directory with md links
directory_str = input("Which directory to check? \n")
directory = os.fsencode(directory_str)

for path, dirname, filenames in os.walk(directory):
    for filename in filenames:
        filename_path = os.path.join(path, filename)
        #print(f"filename_path: {filename_path}")

        if (not filename.endswith(b".md")) and (not filename.endswith(b".MD")):
            continue

        markdownFile = open(filename_path, 'r')
        cont = markdownFile.read()
        markdownFile.close()

        for iteration in range(cont.count("<a href")):
            link_start=cont.find("<a href=")
            link_end=cont.find("</a>")+4
            link=cont[link_start:link_end]

            link_url_start=cont.find("\"", link_start)
            link_url_end=cont.find("\"", link_url_start + 1)
            link_url = cont[link_url_start:link_url_end]
            link_url = link_url.replace("\"", "")

            link_alt_start = cont.find(">", link_url_end) + 1
            link_alt_end = cont.find("</a", link_alt_start)
            link_alt = cont[link_alt_start:link_alt_end]

            link_md = f"[{link_alt}]({link_url})"
            print(f"Found link in {filename}. \nLink: {link}\nExtracted into url: {link_url} \nand alt: {link_alt}.\nChanging to {link_md}\n\n")

            link.replace("\n", "")
            link_md.replace("\n", "")
            cont = cont.replace(link, link_md, 1)

        filename = open(filename_path, 'w')
        filename.write(cont)
