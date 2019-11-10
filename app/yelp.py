'''
import requests
import json
import random
'''
from app import app
'''
api_key = '6MqGGOGfbw44AovX18OKlkUjdb1UBAxui9s03uPsZ4HLaJ7Ubru5ov9IUR8xJBYCVohnaz\
SYRM_PUJtq-4a4hvSFbPMpXL9DQpuoBL4b4o9vedDZzJYMd4x4K0TIXXYx'
headers = {'Authorization': 'Bearer %s' % api_key}

url = 'https://api.yelp.com/v3/businesses/search'
params = {'term': lkjflskjfsl, 'location': akdflskjfs}

req = requests.get(url, params = params, headers = headers)
parsed = json.loads(req.txt)
businsses = parsed['businesses']

i = random.randint(0, len(businesses) - 1)
'''
