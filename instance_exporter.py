from prometheus_client import start_http_server, Summary, Gauge
import time 
import requests
import os
import json

mastodon_host = os.environ.get('MASTODON_HOST', 'https://diaspodon.fr/')
mastodon_host_url = mastodon_host.rstrip("/")

url = mastodon_host + 'api/v1/instance'
url2 = mastodon_host + 'api/v1/instance/activity'


MASTODON_USERS_COUNT = Gauge('mastodon_user_count', 'Total amount of local users')
MASTODON_STATUS_COUNT = Gauge('mastodon_status_count', 'Total amount of status')
MASTODON_DOMAIN_COUNT = Gauge('rmastodon_domain_count', 'Total amount of known domain')
MASTODON_LOGIN = Gauge('mastodon_weekly_login', 'Weekly amount of logins')
MASTODON_STATUSES = Gauge('mastodon_weekly_statuses', 'Weekly amount of statuses')
MASTODON_REGISTRATIONS = Gauge('mastodon_weekly_registrations', 'Weekly amount of statuses')

def process_instance():

#Instance		
    r = requests.get(url)
    data = json.loads(r.content.decode("utf-8","ignore"))
    MASTODON_USERS_COUNT.set((data["stats"]["user_count"]))
    MASTODON_STATUS_COUNT.set((data["stats"]["status_count"]))
    MASTODON_DOMAIN_COUNT.set((data["stats"]["domain_count"]))
#Activity
    r = requests.get(url2)
    data = json.loads(r.content.decode("utf-8","ignore"))
    MASTODON_LOGIN.set((data[0]["logins"]))
    MASTODON_STATUSES.set((data[0]["statuses"]))
    MASTODON_REGISTRATIONS.set((data[0]["registrations"]))

if __name__ == '__main__':
    start_http_server(9410)
    while True: 
        time.sleep(5)
        process_instance()
