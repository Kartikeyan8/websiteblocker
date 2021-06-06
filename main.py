import time
from datetime import datetime as t
hosts_path=r"C:/Windows/System32/Drivers/etc/hosts"
hosts_path1=r"C:\Users\Kart B\PycharmProjects\websiteblocker\hosts"
websitelist=["www.instagram.com","instagram.com"]
redirect="127.0.0.1"
while True:
    if t(t.now().year,t.now().month,t.now().day,23)< t.now() <t(t.now().year,t.now().month,t.now().day,24):
        print("padhai padhai")
        with open(hosts_path1,"r+") as file:
            content=file.read()
            for website in websitelist:
                if website in content:
                    pass
                else:
                    file.write(redirect+' '+ website +'\n')

    else:
        with open(hosts_path1,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websitelist):
                    file.write(line)
                    file.truncate()


        print("padhai padhai")
    time.sleep(5)



