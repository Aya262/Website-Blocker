import time
import argparse
from datetime import datetime as dt


parser=argparse.ArgumentParser(description="Program to block a distracted website for more productivity")
parser.add_argument("--StartHour",help="The begining hour for working hour ",type=int,default=8)
parser.add_argument("--EndHour",help="The end hour for working day ",type=int,default=20)
args=parser.parse_args()
redirect="127.0.0.1"
host_path=r"/etc/hosts"

year=dt.now().year
month=dt.now().month
day=dt.now().day
blocked_website=['www.facebook.com','www.twitter.com','www.youtube.com']
#shour=8
#ehour=21

start_hour=dt(year,month,day,args.StartHour)
end_hour=dt(year,month,day,args.EndHour)
while True:
    if start_hour<dt.now()<end_hour:
        with open(host_path,'r+') as file:
            content=file.read()
            for website in blocked_website:
                if website not in content:
                    content.write(redirect+" "+website+"\n")

    else :
        with open(host_path,'r+') as file:
            lines=file.readlines()
            file.seek(0)
            for line in lines :
                if any (website in line for website in blocked_website):
                    pass
                else :
                    file.write(line)

            file.truncate()

    time.sleep(5)


