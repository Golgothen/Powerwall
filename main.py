from urllib.request import urlopen, Request #, localhost
from urllib.error import HTTPError

import ssl, json
context = ssl._create_unverified_context()
 
host = '192.168.1.112'
browser_id = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
f = urlopen('https://{}/api/meters/aggregates'.format(host), context=context)
response = json.loads(f.read().decode('utf-8', errors='ignore'))
