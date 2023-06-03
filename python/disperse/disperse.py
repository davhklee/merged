import shutil
import os
import subprocess

count = 0
for r, subfolder, files in os.walk("merged"):
    if "git" not in r:
        for f in files:
            count += 1
            src = "/".join([r, f])
            dst = src.replace("merged", "trunk")
            #print(src, dst)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy(src, dst)
            os.system("cd trunk;git add --all")
            os.system("cd trunk;git commit -m 'new commit " + str(count) + "'")



