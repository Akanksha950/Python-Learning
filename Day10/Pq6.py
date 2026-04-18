# 1.Copy notes.txt to notes_backup.txt.
import shutil
shutil.copy("notes.txt","notes_backup.txt")

# 2.Rename notes.txt to final.txt.

import os
os.rename("notes.txt","final.txt")

# 3.Ask user for a filename and copy it to a backup folder.

import shutil
# import os
user=input("enter file name:")

# os.makedirs("backup",exist_ok=True)
shutil.copy(user,"backup")