import requests
# import argparse
import json
from os import path


changefile = 'lastchanges.json'


def run():
    lastchanges = {'rep': 0}
    if path.isfile(changefile):
        with open(changefile, 'r') as f:
            lastchanges = json.loads(f.read())
    res = requests.get('https://api.stackexchange.com/2.2/users/10278?order=desc&sort=reputation&site=stats')
    if res.status_code != 200:
        raise Exception('non 200 status code', res.status_code)
    c = res.content.decode('utf-8')
    # print('c', c)
    d = json.loads(c)
    # print('d', d)
    d2 = d['items'][0]
    # print('d2', d2)
    newrep = {'rep': d2['reputation']}
    if newrep['rep'] != lastchanges['rep']:
        print('rep: %s -> %s' % (lastchanges['rep'], newrep['rep']))
        with open(changefile, 'w') as f:
            f.write(json.dumps(newrep))

if __name__ == '__main__':
    run()
