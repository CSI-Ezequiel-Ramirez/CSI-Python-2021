import json, ssl
import urllib.request
from RandomBeer import RandomBeer

ssl._create_default_https_context = ssl._create_unverified_context

BeerURL = "https://random-data-api.com/api/beer/random_beer?size=100"

beers:RandomBeer = []

Req = urllib.request.Request(BeerURL)
RequestData = json.loads(urllib.request.urlopen(Req).read())

for r in RequestData:
    beer:RandomBeer = RandomBeer(**r)
    beers.append(beer)
    print(beer.name)