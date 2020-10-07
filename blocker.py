import time
from datetime import datetime as dt

host="hosts"
"""replace above address by real host file address"""

website_list=["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]
redirect="127.0.0.1"

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours.....")
        with open(host,'r+') as file:
            content=file.read()
            for i in website_list:
                if i in content:
                    pass
                else:
                    file.write(redirect + " " + i + '\n')
    else:
        with open(host,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun time.....")
    time.sleep(5)