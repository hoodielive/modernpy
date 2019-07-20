my_object = dict()

my_object['key01'] = 'syntax'

print(my_object.__getitem__('key01'))

import urllib
import json
import sys

class Wikipedia():
    def __getitem__(self, key):
        data = urllib.urlopen(
        'http://en.wikipedia.org/w/api.php?action=query'
        '&prop=revisions&titles=%s&rvprop=content&redirects'
        '&format=json' %(urllib2.quote(key))).read()

        return json.loads(data)['query']['pages'].values()[0] \
            ['revisions'][0]['*'].encode('ascii', 'replace')

wikipedia = Wikipedia()
print(wikipedia['hacker'])