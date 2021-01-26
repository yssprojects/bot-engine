import schedule
import requests

def job():
    r = requests.get('http://tgfile.stream.seshu.co/').content
    print(r)
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
