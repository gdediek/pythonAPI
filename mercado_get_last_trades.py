import json
import urllib2

url = "https://www.mercadobitcoin.net/api/BTC/ticker"
data = json.load(urllib2.urlopen(url))

print(data)
