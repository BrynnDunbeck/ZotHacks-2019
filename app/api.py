import requests
import json
import random

def get_data(location, term=None):
    api_key = '6MqGGOGfbw44AovX18OKlkUjdb1UBAxui9s03uPsZ4HLaJ7Ubru5ov9IUR8xJBYCVohnazSYRM_PUJtq-4a4hvSFbPMpXL9DQpuoBL4b4o9vedDZzJYMd4x4K0TIXXYx'
    headers = {'Authorization': 'Bearer %s' % api_key}

    url = 'https://api.yelp.com/v3/businesses/search'
    if term!='':
        params = {'term': term, 'location': location}
    else:
        params = {'location': location}

    req = requests.get(url, params = params, headers = headers)
    parsed = json.loads(req.text)
    businesses = parsed['businesses']
    i = random.randint(0, len(businesses) - 1)
    return businesses[i]
