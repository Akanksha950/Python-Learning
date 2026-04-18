# Word counter-Count how many words are present in the file notes.txt.

with open("notes_backup.txt","r")as f:
    data=f.read()
    words=data.split()
    print("Number of words:",len(words))


# Log Appender-Append the current date and time to a file logs.txt whenever the program runs.

import datetime
with open("logs.txt","a")as f:
    f.write(f"Hello It's me here {datetime.datetime.now()}\n")