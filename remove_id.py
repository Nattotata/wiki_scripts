import os

# Removes id from the frontmatter of a markdown article
# input:
# ---
# title: Spam
# id: spam
# ---
# output:
# ---
# title: Spam
# ---

directory_str = input("Which directory to check? \n")
directory = os.fsencode(directory_str)

for path, dirname, filenames in os.walk(directory):
    for filename in filenames:
        filename_path = os.path.join(path, filename)

        if (not filename.endswith(b".md")) and (not filename.endswith(b".MD")):
            continue

        with open(filename_path,"r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if "id: " not in line[0:10]:
                    f.write(line)
            f.truncate()
            