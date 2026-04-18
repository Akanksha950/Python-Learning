import datetime

with open("mylog.txt","a")as f:
    f.write(f"Akanksha logged in at {datetime.datetime.now()}\n")