from datetime import datetime
from time import sleep
import requests
import schedule
import pytz

TZ = 'US/Central'
print('Script is up')
print("Example : " + datetime.now(pytz.timezone(TZ)).strftime('%c'))

def get_active_count():
    headers = {
        'User-Agent': 'script:f1_active_user_count_puller:v1.2 (by u/itsrekttime)'}
    sub_count = requests.get(
        'https://www.reddit.com/r/formula1/about.json', headers=headers)
    data = sub_count.json()
    timestamp = datetime.now(pytz.timezone(TZ))
    try:
        return data['data']['active_user_count'], timestamp
    except:
        return 'Status 429'

def main(file_name):
    count, timestamp = get_active_count()
    with open(file_name, 'a') as f:
        f.write(timestamp.strftime('%c') + f',{count}\n')

schedule.every(15).seconds.do(main, 'raw_data.txt')


while True:

    schedule.run_pending()
    sleep(1)
