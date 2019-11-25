from pprint import pprint
import requests 

r = requests.get('https://api.spotify.com/v1/search?type=artist&q=snoop')
pprint(r.json())

